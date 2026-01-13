import pandas as pd

def transform_data(df: pd.DataFrame):
    # Converter data
    df["data_venda"] = pd.to_datetime(df["data_venda"])

    # Criar coluna dia do mês
    df["dia_mes"] = df["data_venda"].dt.day

    # Criar períodos do mês
    df["periodo_mes"] = pd.cut(
        df["dia_mes"],
        bins=[0, 10, 20, 31],
        labels=["Início do mês", "Meio do mês", "Fim do mês"]
    )

    # Vendas por período
    vendas_por_periodo = (
        df.groupby("periodo_mes", observed=True)
          .agg(
              total_vendas=("valor_total", "sum"),
              total_itens=("quantidade", "sum"),
              total_transacoes=("valor_total", "count")
          )
          .reset_index()
    )

    # Produtos mais vendidos por período
    produtos_por_periodo = (
        df.groupby(["periodo_mes", "produto"], observed=True)
          .agg(total_quantidade=("quantidade", "sum"))
          .reset_index()
          .sort_values(
              ["periodo_mes", "total_quantidade"],
              ascending=[True, False]
          )
    )

    return vendas_por_periodo, produtos_por_periodo
