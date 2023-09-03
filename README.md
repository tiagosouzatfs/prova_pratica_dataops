# Prova prática Engenheiro de Dados com foco em DevOps

### Repositório destinado aos itens da prova de engenheiro de dados com foco em devops

##### 1) Auto Avaliação 
Auto-avalie suas habilidades nos requisitos de acordo com os níveis especificados usando o
link abaixo.

Qual o seu nível de domínio nas técnicas/ferramentas listadas abaixo, onde:
* 0, 1, 2 - não tem conhecimento e experiência;
* 3, 4 ,5 - conhece a técnica e tem pouca experiência;
* 6 - domina a técnica e já desenvolveu vários projetos utilizando-a.

**Tópicos de Conhecimento:**
* Manipulação e tratamento de dados com Python: **6**
* Manipulação e tratamento de dados com Pyspark: **3**
* Desenvolvimento de data workflows em Ambiente Azure com databricks: **0**
* Desenvolvimento de data workflows com Airflow: **4**
* Manipulação de bases de dados NoSQL: **3**
* Web crawling e web scraping para mineração de dados: **4**
* Construção de APIs: REST, SOAP e Microservices: **3**

##### 2) Desenvolvimento de pipelines de ETL de dados com Python, Apache Airflow, Hadoop e Spark.

a) Olhando para todos os dados disponíveis na fonte citada acima, em qual
estrutura de banco de dados você orienta guardá-los no nosso Data Lake? SQL
ou NoSQL? Discorra sobre sua orientação. (1 pts)

**Resposta:** A escolha entre bancos de dados relacionais e não relacionais em um projeto de dados depende das 
necessidades específicas do projeto, como o tipo de dados, volume, velocidade de acesso e escalabilidade. 
Fazendo uma análise isolada nos arquivos, eles parecem estar bem definidos com relação às colunas e os registros apresentados,
podendo ser uma opção analisar estruturadamente desde que se tenha tempo, porém, fazendo uma análise geral com todos os dados disponíveis pela fonte, 
**o melhor será armazená-los num Data Lake NoSQL**. Os bancos de dados NoSQL tem em suas melhores utilizações em grandes
volumes de dados, na maioria das vezes  não estruturados, e também, em virtude de sua escalabilidade, e que para este caso 
estas características parecem ser essenciais.

b) [Diretório da tarefa 2b](https://google.com.br)
##### Requerimentos para utilização do script
* `pip install wget openpyxl`

c) [Diretório da tarefa 2c](https://google.com.br)
##### Requerimentos para utilização do script
* Docker e Docker-compose instalados na máquina
* Entrar no diretório do script docker-compose e executar o comando: `docker-compose up -d`
* Será inicializado um container Docker do banco de dados MySQL Server 2019, e o acesso se dará ao banco da forma que quiser, podendo ser via alguma ferramenta visual de conexão com o banco de dados como o HeideSQL ou o SQL Server Management Studio, como também por linha de comando, através do binário sqlcmd. A ideia é que se utilize os datasets em **.csv** ou **.xlsx** gerados no passo anterior e importemos eles no SQL Server, como tabelas, após criarmos o banco.
* Para esta atividade foi utilizada a ferramenta SQL Server Management Studio, porém também podemos utilizar a linha de comando para isso, seguindo o ninário do sqlcmd e para acessá-lo, faça conforme os passos abaixo:
  * `docker exec -it -u root sql_server bash`
  * `cd /opt/mssql-tools/bin/`
  * `./sqlcmd -S localhost -U SA -P 'Sqlserver!P4ssw0rd'`
##### Query desenvolvida
* [Link da query](https://google.com.br)
* SELECT COUNT(Município) AS Numero_Atracacoes, Município AS Localidade_Município, UF AS Localidade_UF, [Região Geográfica], DATEDIFF(HOUR, CONVERT(datetime, [Data Chegada], 105), CONVERT(datetime, [Data Atracação], 105)) AS Tempo_Espera_Horas, DATEDIFF(HOUR, CONVERT(datetime, [Data Atracação], 105), CONVERT(datetime, [Data Desatracação], 105)) AS Tempo_Atracado_Horas, Mes, Ano FROM [dbo].[atracacao_fato$] WHERE UF = 'Ceará' AND (Ano = 2018 OR Ano = 2019) GROUP BY Município, UF, [Região Geográfica], [Data Chegada], [Data Atracação], [Data Desatracação], Mes, Ano ORDER BY Mes, Ano;

##### 3) Criação de ambiente de desenvolvimento com Linux e Docker.
[Diretório da tarefa 3](https://google.com.br)
##### Requerimentos para utilização do script
* O arquivo python com o desenvolvimento da DAG com as tasks já se encontra no diretório **/dags** desta tarefa
* Docker e Docker-compose instalados na máquina
* `pip install "apache-airflow[celery]==2.7.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.0/constraints-3.8.txt"`
* `docker-compose up airflow-init`
* `docker-compose up`
* Como este script python necessita de bibliotecas externas, então:
  * `docker exec -it -u root task3_airflow-scheduler_1 bash`
  * `apt update`
  * `exit`
  * `docker exec -it task3_airflow-scheduler_1 bash`
  * `pip install wget openpyxl`
  * `exit`

##### 4) Configuração de pipelines de CI/CD com Gitlab ou Github.
**Não Feita**

##### 5) Implantação de aplicações com Kubernetes.
[Diretório da tarefa 5](https://google.com.br)
**Para as opções de infraestrutura local, foram desenvolvidas 3 opções:**
  * Solução containeriza com docker-compose de 3 conainers com a flag privileged para rodar docker dind, baseada em rancher
  * Solução virtualizada com vagrant, 3 servidores com o box do ubuntu server 20.04, baseada em k3s
  * Solução virtualizada com minikube (microframework k8s), 3 nodes adicionados já no cluster (solução utilizada para esse exercício)
##### Requerimentos para utilização do script
* O arquivo python com o desenvolvimento da DAG com as tasks já se encontra no diretório **/dags** desta tarefa
* Docker e Docker-compose instalados na máquina
* Terminal 1: iniciar o script dentro do diretório da tarefa: `./create_environment.sh`
* [Link do script para automação](https://google.com.br)
  * Ao finalizar o script acima, utilizar os comandos abaixo, 1 para cada terminal, pois esses comandos ocupam um terminal por comando
  * Terminal 2: `minikube mount ./dags/:/data/dags`
  * Terminal 3: `minikube mount ./data/:/data/data`
  * Terminal 4: `minikube mount ./logs/:/data/logs`
* [Link dos comandos executados](https://google.com.br)
* Terminal 5: acessar o dashboard do minikube para ver o que foi criado, pods, deployments, namespaces, persistent volumes, persistent volumes clain
  * `minikube dashboard`
  * O comando acima irá gerar um link para **127.0.0.1** para acesso web ao minikube
* Se tudo ocorreu bem, acessar a página do airflow, em: **localhost:8080**

##### 6) Implantação de Data Lake com Hadoop.
* link da pasta 6
