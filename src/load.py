from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # raiz do projeto

def load_data(vendas_por_periodo, produtos_por_periodo, output_dir="output"):
    output_path = BASE_DIR / output_dir
    output_path.mkdir(exist_ok=True)

    vendas_por_periodo.to_csv(
        output_path / "vendas_por_periodo_mes.csv",
        index=False,
        encoding="utf-8-sig"
    )

    produtos_por_periodo.to_csv(
        output_path / "produtos_por_periodo_mes.csv",
        index=False,
        encoding="utf-8-sig"
    )
