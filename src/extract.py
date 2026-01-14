import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # raiz do projeto

def extract_data(path="data/vendas.csv"):
    full_path = BASE_DIR / path
    df = pd.read_csv(full_path)
    df["data_venda"] = pd.to_datetime(df["data_venda"])
    return df
