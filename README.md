# 1. Passo a Passo Para Gerar o Ambiente Virtual

Instale o virtualenv:

```bash
pip3 install virtualenv
```

Crie um ambiente virtual de python 3:

```bash
virtualenv .\venv -p python3
```

Ative o ambiente:

```bash
.\venv\Scripts\activate
```

Atualize a versão do pip:

```bash
python -m pip install --upgrade pip
```

Instale os requirements:

```bash
pip install -r requirements.txt
```

# 2. Passo a Passo Para Gerar o executável

Instale o pyinstaller:

```bash
pip install pyinstaller
```

Execute o comando na pasta:

```bash
pyinstaller --onefile Main.py
```

Caso o antivirus impeça a produção do arquivo Main.exe, pause o antivirus e repita o último passo.

# 3. Download Chrome Driver

1. Verifique sua versão atual do Chrome (Abra as configurações do Chrome -> Sobre o Google Chrome);
2. Acesse o [link](https://googlechromelabs.github.io/chrome-for-testing/);
3. Faça o download do chromedriver estável compativel com a sua versão;

# 4. Airflow

O passo a passo desse item tem como objetivo mostrar como executar o airflow utilizando o docker

## 4.1 Configuração Arquivo docker-compose.yml

As chaves com o nome `FERNET_KEY` devem ser preenchidas com uma chave que pode ser obtida com o código abaixo:

```python
# Instalar lib se necessário
#!pip install cryptography
from cryptography.fernet import Fernet
fernet_key = Fernet.generate_key()
print(fernet_key.decode())
```

## 4.2 Comandos para inicializar o Airflow

Os comandos a seguir devem ser executados na pasta do projeto do Airflow

Na primeira vez, rodar:

```bash
docker-compose up airflow-init
```

Rodar o Airflow forçando o build da imagem:

```bash
docker-compose up --build
```

Após essa execução o airflow pode ser acessado através da porta 8080

## 4.3 Adicionando usuário

Para acesso no Airflow é necessário adicionar um usuário administrador, use o comando a seguir para fazê-lo:

```bash
docker-compose exec webserver airflow users create --username user --firstname Name --lastname LastName --role Admin --email example@example.com --password password
```

## 4.4 Comandos adicionais do docker para uso geral

Os comandos a seguir podem ajudar na utilização do Docker:

Sobe o container em modo detached, ou seja, em segundo plano:

```bash
docker-compose up -d
```

Mostra os status dos container em execução:

```bash
docker-compose ps -a
```

Para os serviços dos containers:

```bash
docker-compose down
```

Para os serviços dos containers e também deleta os volumes:

```bash
docker-compose down -v
```

Para os serviços dos containers, deleta os volumes, imagens e redes:

```bash
docker-compose down --rmi all --volumes --remove-orphans
```

Comando para navegar no diretório criado pelo docker

```bash
docker exec -it container_name_or_id sh
```

Copiar arquivo de dentro do container para fora

```bash
docker cp <container_name_or_id>:/opt/airflow/resultado_202410281842.xlsx C:/Users/Erivan/Documents/precatorio-work/Projeto_Airflow/resultado.xlsx
```
