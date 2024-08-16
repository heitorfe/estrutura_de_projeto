import os
from typing import List
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from app.pipeline.extract import extract_from_excel
from app.pipeline.load import load_excel
from app.pipeline.transform import concat_dfs

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]} )
df_2 = pd.DataFrame({'col1': [9,8], 'col2': [7,6]} )

def test_df_list_concat():

    df_list = [df_1, df_2]
    arrange = pd.concat(df_list, ignore_index=True)
    act = concat_dfs(df_list)

    assert act.shape == (4,2)
    # assert arrange.equals(act)

def test_extract_from_excel_no_files(mocker):
    mocker.patch('glob.glob', return_value=[])
    
    with pytest.raises(ValueError, match="No Excel files found in the specified folder"):
        extract_from_excel("some_path")

# Teste quando há arquivos Excel na pasta e a função funciona corretamente
def test_extract_from_excel_with_files(mocker):
    # Simula o retorno de arquivos Excel
    mocker.patch('glob.glob', return_value=["file1.xlsx", "file2.xlsx"])
    
    # Simula a leitura de arquivos Excel e o retorno de dataframes
    mock_read_excel = mocker.patch('pandas.read_excel', side_effect=[
        pd.DataFrame({'A': [1, 2, 3]}),
        pd.DataFrame({'B': [4, 5, 6]})
    ])
    
    result = extract_from_excel("some_path")
    
    # Verifica se o pandas.read_excel foi chamado duas vezes (uma para cada arquivo)
    assert mock_read_excel.call_count == 2
    
    # Verifica se o resultado contém dois dataframes
    assert len(result) == 2
    assert isinstance(result[0], pd.DataFrame)
    assert isinstance(result[1], pd.DataFrame)
    
    # Verifica os dados dentro dos dataframes
    pd.testing.assert_frame_equal(result[0], pd.DataFrame({'A': [1, 2, 3]}))
    pd.testing.assert_frame_equal(result[1], pd.DataFrame({'B': [4, 5, 6]}))

# Teste para o caso onde o diretório não existe ou há algum problema no caminho
def test_extract_from_excel_invalid_path(mocker):
    mocker.patch('glob.glob', side_effect=OSError("Invalid directory"))
    
    with pytest.raises(OSError, match="Invalid directory"):
        extract_from_excel("invalid_path")


def test_concat_dfs_success():
    # Simula uma lista de DataFrames
    df1 = pd.DataFrame({'A': [1, 2, 3]})
    df2 = pd.DataFrame({'A': [4, 5, 6]})
    df_list = [df1, df2]
    
    # Chama a função
    result = concat_dfs(df_list)
    
    # Verifica se o DataFrame final é a concatenação correta
    expected = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]})
    pd.testing.assert_frame_equal(result, expected)

def test_concat_dfs_empty_list():
    # Simula uma lista vazia de DataFrames
    df_list = []
    
    # Chama a função e espera uma exceção
    with pytest.raises(ValueError):
        concat_dfs(df_list)

def test_concat_dfs_mixed_columns():
    # Simula uma lista de DataFrames com colunas diferentes
    df1 = pd.DataFrame({'A': [1, 2, 3]})
    df2 = pd.DataFrame({'B': [4, 5, 6]})
    df_list = [df1, df2]
    
    # Chama a função
    result = concat_dfs(df_list)
    
    # Verifica se o DataFrame final contém NaNs onde as colunas não coincidem
    expected = pd.DataFrame({'A': [1, 2, 3, None, None, None], 'B': [None, None, None, 4, 5, 6]})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)

def test_load_excel_success(mocker):
    # Simula um DataFrame
    df = pd.DataFrame({'A': [1, 2, 3]})
    
    # Mock para verificar se o diretório existe
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock para a função pd.DataFrame.to_excel
    mock_to_excel = mocker.patch.object(pd.DataFrame, 'to_excel')

    # Chama a função
    result = load_excel(df, "some_path", "output.xlsx")
    
    # Verifica se o arquivo foi salvo corretamente
    mock_to_excel.assert_called_once_with('some_path/output.xlsx', index=False)
    assert result == 'Arquivo salvo com sucesso'

def test_load_excel_create_directory(mocker):
    # Simula um DataFrame
    df = pd.DataFrame({'A': [1, 2, 3]})
    
    # Mock para verificar se o diretório não existe
    mocker.patch('os.path.exists', return_value=False)
    
    # Mock para criar diretório
    mock_makedirs = mocker.patch('os.makedirs')
    
    # Mock para a função pd.DataFrame.to_excel
    mock_to_excel = mocker.patch.object(pd.DataFrame, 'to_excel')

    # Chama a função
    result = load_excel(df, "some_path", "output.xlsx")
    
    # Verifica se o diretório foi criado e o arquivo foi salvo
    mock_makedirs.assert_called_once_with("some_path")
    mock_to_excel.assert_called_once_with('some_path/output.xlsx', index=False)
    assert result == 'Arquivo salvo com sucesso'