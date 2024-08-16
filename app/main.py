from pipeline.extract import extract_from_excel
from pipeline.transform import concat_dfs
from pipeline.load import load_excel


if __name__ == "__main__":

    path = 'data/input'
    df_list = extract_from_excel(path)
    df = concat_dfs(df_list=df_list)
    load_excel(df, 'data/output', 'concatenated_data.xlsx')