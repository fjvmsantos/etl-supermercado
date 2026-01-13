# ETL de Vendas – Supermercado

## Objetivo
Este projeto tem como objetivo analisar o comportamento de vendas de um supermercado,
identificando:
- Quais períodos do mês concentram maior volume de vendas
- Quais produtos são mais vendidos em cada período

Os resultados apoiam decisões de estoque, promoções e planejamento comercial.

---

## Estrutura do Projeto

## 🔄 Pipeline ETL

### Extract
Leitura de dados de vendas a partir de um arquivo CSV contendo:
- Data da venda
- Produto
- Categoria
- Quantidade
- Valor total

### Transform
- Conversão de datas
- Criação de períodos do mês (início, meio e fim)
- Agregação de vendas por período
- Identificação dos produtos mais vendidos por período

### Load
- Geração de arquivos CSV analíticos
- Dados prontos para BI, Excel ou dashboards

---

## 📊 Resultados
Os principais resultados gerados são:
- `vendas_por_periodo_mes.csv`
- `produtos_por_periodo_mes.csv`

Esses arquivos permitem identificar padrões de consumo e sazonalidade mensal.

---

## Tecnologias Utilizadas
- Python
- Pandas
- NumPy
- Visual Studio Code

---

## Como executar o projeto

1. Criar e ativar o ambiente virtual
2. Instalar dependências:
```bash
pip install -r requirements.txt

##Executar
python src/extract.py
python src/transform.py
python src/load.py