import os

import pandas as pd


def load_excel(df: pd.DataFrame, output_path: str, filename: str) -> str:
    path = f'{output_path}/{filename}'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    df.to_excel(path, index=False)

    return 'Arquivo salvo com sucesso'