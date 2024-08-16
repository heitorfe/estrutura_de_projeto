import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler arquivos de uma 
    pasta input e retornar uma lista de dataframes
    args: input_path(str): caminho da pasta com os arquivos

    return: lista com os dataframes
    """
    files = glob.glob(os.path.join(path, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    
    all_data = [pd.read_excel(file) for file in files]

    return all_data

