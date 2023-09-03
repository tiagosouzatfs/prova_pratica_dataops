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
* Manipulação e tratamento de dados com Python: 6
* Manipulação e tratamento de dados com Pyspark: 3
* Desenvolvimento de data workflows em Ambiente Azure com databricks: 0
* Desenvolvimento de data workflows com Airflow: 4
* Manipulação de bases de dados NoSQL: 4
* Web crawling e web scraping para mineração de dados: 3
* Construção de APIs: REST, SOAP e Microservices: 3

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

b) **Requerimentos para utilização do script**
'pip install wget openpyxl'
link da pasta 2b

c) **Requerimentos para utilização do script**
* Docker-compose instalado na máquina;
* Entrar no diretório do script docker-compose e executar o comando: **docker-compose up -d**
link da pasta 2c


##### 3) Criação de ambiente de desenvolvimento com Linux e Docker.
link

##### 4) Configuração de pipelines de CI/CD com Gitlab ou Github.
**Não Feita**

##### 5) Implantação de aplicações com Kubernetes.
link

##### 6) Implantação de Data Lake com Hadoop.
link
