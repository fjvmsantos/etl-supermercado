from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    df = extract_data()
    vendas_por_periodo, produtos_por_periodo = transform_data(df)
    load_data(vendas_por_periodo, produtos_por_periodo)

if __name__ == "__main__":
    run_pipeline()
