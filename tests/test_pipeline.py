import pandas as pd
from app.pipeline.transform import concat_dfs


df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]} )
df_2 = pd.DataFrame({'col1': [9,8], 'col2': [7,6]} )

def test_df_list_concat():

    arrange = pd.concat([df_1, df_2], ignore_index=True)

    act = concat_dfs([df_1, df_2])

    assert arrange == act