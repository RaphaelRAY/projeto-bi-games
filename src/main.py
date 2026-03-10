import pandas as pd
from google.cloud import bigquery
import os

# Configurações do BigQuery
# Lembre-se de configurar a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS
PROJECT_ID = "seu_projeto"
DATASET_ID = "seu_dataset"

def load_data_to_bq():
    client = bigquery.Client(project=PROJECT_ID)
    
    # Exemplo de carregamento de um arquivo CSV
    # file_path = "../data/games.csv"
    # table_id = f"{PROJECT_ID}.{DATASET_ID}.games"
    # df = pd.read_csv(file_path)
    # job = client.load_table_from_dataframe(df, table_id)
    # job.result()
    # print(f"Tabela {table_id} carregada com sucesso.")
    
    print("Script principal de carga de dados.")
    
if __name__ == "__main__":
    load_data_to_bq()
