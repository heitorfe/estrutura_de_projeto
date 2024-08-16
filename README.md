## 1. Usar Pyenv para escolher a versão do Python

`pyenv install 3.11.5`

## 2. Criar o ambiente virtual com o poetry

Cria ambiente virtual poetry

`poetry config virtualenvs.in-project true` 

Inicializa projeto poetry

`poetry init`

Seleciona a versão do Python a ser utilizada

`poetry env use 3.11.5`

Cria o ambiente virtual

`poetry shell`

Adicionar bibliotecas

`poetry add pandas`

Sair do ambiente virtual

`deactivate`

## 3. Versionar no GitHub

Criar o repositório para o projeto. Criar as branches, configurar necessidade ou não de PR. Versionar o código. 

Site para encontrar o .gitignore: https://www.toptal.com/developers/gitignore

## 4. Padrões de projeto

PEP8 org.

Libs:
* black
* blue
* isort
`isort .` 
* autopep8

## 5. Taskipy

Ajuda a automatizar comandos CLI. Evita overhead de ter que lembrar de vários comandos.

```
[tool.taskipy.tasks]
format = """
isort .
black .
"""
kill = "kill -9 $(lsof -t -i :8000)"
test = "pytest -v"
run = """
python3 app/main.py
"""
doc = "mkdocs serve"
```