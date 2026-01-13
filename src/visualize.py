import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../output/vendas_por_periodo_mes.csv")

plt.bar(df["periodo_mes"], df["total_vendas"])
plt.title("Total de Vendas por Período do Mês")
plt.xlabel("Período do mês")
plt.ylabel("Total de vendas (R$)")

plt.show()
