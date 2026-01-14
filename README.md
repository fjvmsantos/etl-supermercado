# ETL de Vendas – Supermercado

Este projeto implementa um pipeline ETL (Extract, Transform, Load) em Python para análise de vendas de um supermercado, incluindo a geração de visualizações para apoio à tomada de decisão.

## 🎯 Objetivo

Analisar o comportamento de vendas do supermercado, identificando:

- Quais períodos do mês concentram maior volume de vendas  
- Quais produtos são mais vendidos em cada período  

Os resultados auxiliam decisões relacionadas a:
- planejamento de estoque  
- definição de promoções  
- análise de desempenho comercial  

---

## 🏗️ Estrutura do Projeto

etl-supermercado/

├── data/ # Dados de entrada (CSV)

├── output/ # Resultados gerados pelo ETL

├── src/ # Código-fonte

│ ├── extract.py

│ ├── transform.py

│ ├── load.py

│ ├── pipeline.py

│ └── visualize.py

├── requirements.txt

└── README.md

---

## 🔄 Pipeline ETL

### Extract
- Leitura de dados de vendas a partir de um arquivo CSV
- Campos utilizados:
  - data_venda
  - produto
  - categoria
  - quantidade
  - valor_total

### Transform
- Conversão de datas
- Criação de períodos do mês:
  - Início do mês
  - Meio do mês
  - Fim do mês
- Agregação de métricas por período
- Identificação dos produtos mais vendidos em cada período

### Load
- Geração de arquivos CSV analíticos
- Dados prontos para uso em Excel, BI ou dashboards

---

## 📈 Visualização dos Dados

Após a execução do pipeline ETL, é possível gerar visualizações a partir dos dados processados.

O arquivo `visualize.py` é responsável por criar um gráfico de barras com o **total de vendas por período do mês**, facilitando a identificação de padrões e sazonalidade.

### Executar a visualização
```bash
python src/visualize.py

O gráfico exibido apresenta:

eixo X: período do mês (início, meio, fim)

eixo Y: valor total de vendas

📊 Resultados Gerados

O pipeline gera automaticamente os seguintes arquivos:

output/vendas_por_periodo_mes.csv

output/produtos_por_periodo_mes.csv

Esses arquivos servem como base para análises adicionais e visualizações.

🛠️ Tecnologias Utilizadas

Python

Pandas

NumPy

Matplotlib

Visual Studio Code

Google Colab (compatível)

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/fjvmsantos/etl-supermercado.git
cd etl-supermercado

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

3️⃣ Instalar as dependências
pip install -r requirements.txt

4️⃣ Executar o pipeline ETL
python src/pipeline.py

5️⃣ Gerar o gráfico
python src/visualize.py

📌 Observações

O projeto foi estruturado para funcionar corretamente tanto em ambiente local quanto no Google Colab.

O pipeline ETL é independente da camada de visualização, seguindo boas práticas de separação de responsabilidades.