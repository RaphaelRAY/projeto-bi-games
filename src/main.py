import pandas as pd
from google.cloud import bigquery
import os

# Configurações do BigQuery - IDs Reais
PROJECT_ID = "directed-mender-489100-m3"
DATASET_RAW = "games_data"             # Dataset com as tabelas originais (Bronze)
DATASET_ANALYTICS = "games_analytics"   # Dataset para a Visão Final (Silver/Gold)

def create_view():
    """Lê o arquivo SQL e cria as Views no BigQuery."""
    client = bigquery.Client(project=PROJECT_ID)
    
    # Garante que o dataset de analytics existe
    dataset_ref = client.dataset(DATASET_ANALYTICS)
    try:
        client.get_dataset(dataset_ref)
    except Exception:
        print(f"Criando dataset {DATASET_ANALYTICS}...")
        client.create_dataset(bigquery.Dataset(dataset_ref))

    # Caminho do arquivo SQL
    sql_file_path = os.path.join(os.path.dirname(__file__), "..", "sql", "create_view.sql")
    
    with open(sql_file_path, "r", encoding="utf-8") as f:
        sql_script = f.read()

    print(f"Executando script SQL de: {sql_file_path}")
    
    # Executa o script (pode conter múltiplas declarações)
    query_job = client.query(sql_script)
    query_job.result()
    
    print(f"✅ Views criadas/atualizadas com sucesso no projeto {PROJECT_ID}")

def load_data_to_bq():
    # Esta função pode ser expandida se houver novos dados locais
    print(f"Iniciando processo para Projeto: {PROJECT_ID}")
    create_view()
    
if __name__ == "__main__":
    load_data_to_bq()
