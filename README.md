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