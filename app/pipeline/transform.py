from typing import List

import pandas as pd

"""
função para transformar uma lista de datagframes em um único dataframe
"""

def concat_dfs(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(df_list).reset_index(drop=True)