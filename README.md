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

