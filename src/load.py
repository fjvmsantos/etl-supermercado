import os

def load_data(vendas_por_periodo, produtos_por_periodo, output_dir="../output"):
    os.makedirs(output_dir, exist_ok=True)

    vendas_por_periodo.to_csv(
        f"{output_dir}/vendas_por_periodo_mes.csv",
        index=False,
        encoding="utf-8-sig"
    )

    produtos_por_periodo.to_csv(
        f"{output_dir}/produtos_por_periodo_mes.csv",
        index=False,
        encoding="utf-8-sig"
    )
