import os
import pandas as pd
import wget
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
import pendulum
from kubernetes.client import models as k8s

path_fileszip = "/opt/airflow/dags/fileszip"
path_datasets = "/opt/airflow/dags/datasets"

url_carga_2017 = "https://web3.antaq.gov.br/ea/txt/2017Carga.zip"
url_atracacao_2017 = "https://web3.antaq.gov.br/ea/txt/2017Atracacao.zip"

url_carga_2018 = "https://web3.antaq.gov.br/ea/txt/2018Carga.zip"
url_atracacao_2018 = "https://web3.antaq.gov.br/ea/txt/2018Atracacao.zip"

url_carga_2019 = "https://web3.antaq.gov.br/ea/txt/2019Carga.zip"
url_atracacao_2019 = "https://web3.antaq.gov.br/ea/txt/2019Atracacao.zip"

lista_urls = [url_carga_2017, url_carga_2018, url_carga_2019, 
              url_atracacao_2017, url_atracacao_2018, url_atracacao_2019]

executor_config = {
    "pod_override": k8s.V1Pod(spec=k8s.V1PodSpec(

        containers=[
            k8s.V1Container(
                name="base",
                volume_mounts=[
                    k8s.V1VolumeMount(mount_path="/data/", name="stock-volume")
                ],
            )
        ],
        volumes=[
            k8s.V1Volume(
                name="stock-volume",
                persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(
                    claim_name="airflow-data-claim"
                )
            )
        ]))
}

def clean_directorys():
    os.chdir(path_fileszip)
    for file1 in os.listdir():
        os.remove(file1)
    os.chdir(path_datasets)
    for file2 in os.listdir():
        os.remove(file2)

cont = 1
@task(executor_config=executor_config)
def download_all_fileszip():
    os.chdir(path_fileszip)
    for url in lista_urls:
        wget.download(url)
        print("\n")
    verify_total_fileszip

def verify_total_fileszip():
    if cont == 3:
        print("Saindo do script, contacte seu administrador de redes\n")
        print("Provável problema de conexão com a internet, bloqueio de portas no firewall, proxy ou os dados estão indisponíveis para consulta!\n")
        return False

    if len(os.listdir()) < 6:
        cont = cont + 1
        download_all_fileszip
    else:
        print("Arquivos Disponíveis")
        return True

def is_valid(ti):
    verify = ti.xcom_pull(task_ids= 'download_all_fileszip')
    if verify is True:
        return 'read_and_save_datasets'
    return 'connection_problem'

def read_and_save_datasets(ti):
    os.chdir(path_fileszip)
    dataframe_final_carga = pd.DataFrame()
    dataframe_final_atracacao = pd.DataFrame()
    
    #Tive que limitar o número de linhas para a tabela carga_fato pq meu computador estava travando, 
    #ele é muito grande, deixei ele com 90k linhas, 30k para cada ano
    for file in os.listdir():
        if file == "2017Carga.zip" or file == "2018Carga.zip" or file == "2019Carga.zip":
            dataframe_carga = pd.read_csv(file, sep=';', compression='zip', encoding='utf-8', nrows=30000, dtype=str)
            dataframe_final_carga = pd.concat([dataframe_carga, dataframe_final_carga])
        else:
            dataframe_atracacao = pd.read_csv(file, sep=';', compression='zip', encoding='utf-8', nrows=30000)
            dataframe_final_atracacao = pd.concat([dataframe_atracacao, dataframe_final_atracacao])

    os.chdir(path_datasets)
    #print(os.getcwd())

    dataframe_final_carga.to_csv('carga_fato.csv', sep=';', encoding='utf-8')
    dataframe_final_carga.to_excel('carga_fato.xlsx')
    dataframe_final_atracacao.to_csv('atracacao_fato.csv', sep=';', encoding='utf-8')
    dataframe_final_atracacao.to_excel('atracacao_fato.xlsx')

with DAG("antaq_stream_etl", start_date=pendulum.datetime(2023, 8, 30, tz="UTC"), 
         schedule_interval="0 5 1 * *", catchup=False) as dag: #Executa todo dia 01 às 5h da manhã
    
    task_1 = PythonOperator(
        task_id= "clean_directorys",
        python_callable=clean_directorys
    )

    task_2 = PythonOperator(
        task_id= "download_all_fileszip",
        python_callable=download_all_fileszip
    )

    task_3 = PythonOperator(
        task_id= "is_valid",
        python_callable=is_valid
    )

    task_4 = PythonOperator(
        task_id= "read_and_save_datasets",
        python_callable=read_and_save_datasets
    )

    task_5 = BashOperator(
        task_id="created_tables",
        bash_command='echo "Arquivos atualizados no diretório de datasets"'
    )

    task_6 = BashOperator(
        task_id="connection_problem",
        bash_command='echo "Problemas de conexão para download dos arquivos"'
    )

    task_7 = EmailOperator(
        task_id="send_email",
        to='test@mail.com',
        subject='Alert Mail',
        html_content=""" Mail Test """,
        dag=dag
    )

    task_1 >> task_2 >> task_3 >> [task_4, task_6]
    task_4 >> task_5
    task_6 >> task_7

    
