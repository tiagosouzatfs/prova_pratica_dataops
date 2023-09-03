import os
import pandas as pd
import wget

path_fileszip = "fileszip"
path_datasets = "datasets"

url_carga_2017 = "https://web3.antaq.gov.br/ea/txt/2017Carga.zip"
url_atracacao_2017 = "https://web3.antaq.gov.br/ea/txt/2017Atracacao.zip"

url_carga_2018 = "https://web3.antaq.gov.br/ea/txt/2018Carga.zip"
url_atracacao_2018 = "https://web3.antaq.gov.br/ea/txt/2018Atracacao.zip"

url_carga_2019 = "https://web3.antaq.gov.br/ea/txt/2019Carga.zip"
url_atracacao_2019 = "https://web3.antaq.gov.br/ea/txt/2019Atracacao.zip"

lista_urls = [url_carga_2017, url_carga_2018, url_carga_2019, 
              url_atracacao_2017, url_atracacao_2018, url_atracacao_2019]

def clean_files():
    os.chdir(f"./{path_fileszip}")
    for file1 in os.listdir():
        os.remove(file1)
    os.chdir(f"../{path_datasets}")
    for file2 in os.listdir():
        os.remove(file2)

cont = 1
def download_all_fileszip():
    for url in lista_urls:
        wget.download(url)
        print("\n")
    verify_total_fileszip

def verify_total_fileszip():
    if cont == 3:
        print("Saindo do script, contacte seu administrador de redes\n")
        print("Provável problema de conexão com a internet, bloqueio de portas no firewall, proxy ou os dados estão indisponíveis para consulta!\n")
        exit

    if len(os.listdir()) < 6:
        cont = cont + 1
        download_all_fileszip
    else:
        print("Arquivos Disponíveis")

def read_datasets_and_save_datasets_finals():
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

    os.chdir(f"../{path_datasets}")
    #print(os.getcwd())

    dataframe_final_carga.to_csv('carga_fato.csv', sep=';', encoding='utf-8')
    dataframe_final_carga.to_excel('carga_fato.xlsx')
    dataframe_final_atracacao.to_csv('atracacao_fato.csv', sep=';', encoding='utf-8')
    dataframe_final_atracacao.to_excel('atracacao_fato.xlsx')

if __name__ == "__main__":

    #print(os.getcwd())
    
    clean_files()

    os.chdir(f"../{path_fileszip}")
    #print(os.getcwd())

    download_all_fileszip()

    read_datasets_and_save_datasets_finals()
    
