import pandas as pd

def extract_data(path="../data/vendas.csv"):
    df = pd.read_csv(path)
    df["data_venda"] = pd.to_datetime(df["data_venda"])
    return df
