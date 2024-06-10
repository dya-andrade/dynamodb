# dynamodb
CRUD com DynamoDB, LocalStack e Java 21.

### Dependências

* Instalar o LocalStack 
<p>Disponibilizando um ambiente de teste na máquina local, onde a aplicação está a ser desenvolvida. Este ambiente 
oferece a mesma funcionalidade e APIs do ambiente cloud da AWS. Utilizando como dependência o Docker.</p>

<a href="https://docs.localstack.cloud/getting-started/installation/">Instalar LocalStack</a>

```shell
brew install localstack/tap/localstack-cli
localstack --version
```

* Instalar Docker
* Instalar AWS CLI

## Inicializando e testando o LocalStack 

* Inicialize o container do LocalStack

```shell
localstack start
```

* Faça login ou crie uma conta no site da LocalStack

<a href="https://app.localstack.cloud/sign-in">Login na LocalStack</a>

* No site do LocalStack, vá em **LocalStack Instances** e de depois em **Status**

<p>O LocalStack vai detectar qual instância (container) está rodando dentro do computador, e vai mostrar quais serviços 
da AWS estão disponíveis em <b>Status</b>.</p>

<p>Todas as alterações em serviços que faríamos na AWS, podemos fazer localmente sem custo</p>

### Alternativa caso não consiga rodar o container do LocalStack localmente

* Crie um arquivo docker-compose.yaml

```yaml
version: '3.8'
services:
  localstack:
    image: localstack/localstack:latest
    ports:
      - "4566:4566"
      - "4571:4571"
    environment:
      - SERVICES=s3,lambda,ec2,cloudwatch,iam,dynamodb
      - DEBUG=1
      - DATA_DIR=/tmp/localstack/data
      - LAMBDA_EXECUTOR=docker
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
```
* E suba o container localmente, o mesmo será reconhecido no site do LocalStack

```shell
brew install docker-compose
docker-compose up
```
* Cria um bucket no S3 do site LocalStack, como teste.

## Instalação e Teste do AWS CLI

* No Linux, você pode instalar a AWS CLI usando o Homebrew:

```shell
brew install awscli
aws --version
```
* Vinculando o CLI com LocalStack

  * Lista todos os buckets disponíveis
  
    ```shell
    aws --endpoint="http://localhost:4566" s3 ls
    ```
    
  * Cria uma fila SQS
  
    ```shell
    aws --endpoint="http://localhost:4566" sqs create-queue --queue-name minha-fila-teste
    ```
    
## Inicializar o projeto

* Inicializa um projeto no site do **Spring Initializr**
  * Com a dependência **Spring Web**

<a href="https://start.spring.io/">Start.spring.io</a>

* Importar as dependências do Spring Cloud AWS

<a href="https://docs.awspring.io/spring-cloud-aws/docs/3.1.0/reference/html/index.html#starter-dependencies">
Documentação sobre o Spring Cloud AWS</a>

* No pom.xml do projeto:

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>io.awspring.cloud</groupId>
      <artifactId>spring-cloud-aws-dependencies</artifactId>
      <version>{project-version}</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

```xml
<dependency>
    <groupId>io.awspring.cloud</groupId>
    <artifactId>spring-cloud-aws-starter-dynamodb</artifactId>
</dependency>
```

## Configurando o projeto

### Configure o DynamoDB client

* Siga o exemplo que está no projeto na pasta config

### Configure a entidade do DynamoDB

* Siga o exemplo que está no projeto na pasta entity

### Crie o CRUD

* Siga o exemplo que está no projeto na pasta