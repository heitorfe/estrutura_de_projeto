from pipeline.extract import extract_from_excel


if __name__ == "__main__":

    path = 'data/input'

    df_list = extract_from_excel(path)
    print(df_list)