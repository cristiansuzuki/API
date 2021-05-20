# API


## Instalação

Inicie um ambiente virtual (deve possuir o Python instalado)

```python
python -m venv venv
```

Após isso, acesse a pasta do ambiente pelo terminal e ative o arquivo "activate.bat"

```bash
venv\Scripts\activate
```

## Instalando dependências do projeto

Use o gerenciador de pacotes do python para baixar as as bibliotecas necessárias do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

## Executando o projeto localmente

Após abrir a pasta raiz do projeto (onde está o arquivo manage.py), com suas devidas dependências instaladas e dentro de um ambiente virtual (de preferência), execute o comando abaixo no terminal.

```bash
python manage.py runserver
```
Isso irá rodar o projeto em um servidor local, caso uma janela do navegador não se inicie sozinha, clique no link gerado no terminal.

## Endpoints

O objetivo dessa API é realizar operações através dos metodos disponíveis com apenas 1 endpoint.

<p>http://127.0.0.1:8000/alunos/</p>

## Contribuições

Pull Requests são bem-vindos.
