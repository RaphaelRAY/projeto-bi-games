import pandas as pd
from google.cloud import bigquery
import os

# Configurações do BigQuery - IDs Reais extraídos do notebook
PROJECT_ID = "directed-mender-489100-m3"
DATASET_ID = "games_data"

def create_view():
    """Cria ou substitui uma View no BigQuery unindo as tabelas principais."""
    client = bigquery.Client(project=PROJECT_ID)
    view_id = f"{PROJECT_ID}.{DATASET_ID}.vw_analise_games"
    
    sql_view = f"""
    CREATE OR REPLACE VIEW `{view_id}` AS
    SELECT
        g.id AS game_id,
        g.name AS nome_jogo,
        g.released AS data_lancamento,
        g.rating AS nota_usuarios,
        g.metacritic AS nota_critica,
        p.publisher_name AS distribuidora,
        gen.genre_name AS genero,
        plat.platform_name AS plataforma,
        m.completability_index AS indice_conclusao,
        m.consensus_score AS score_consenso
    FROM
        `{PROJECT_ID}.{DATASET_ID}.games` g
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_ID}.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_ID}.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_ID}.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_ID}.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING)
    """
    
    # Executa o comando de criação da View
    query_job = client.query(sql_view)
    query_job.result()
    print(f"✅ View {view_id} criada com sucesso no BigQuery!")

def load_data_to_bq():
    # Esta função pode ser expandida se houver novos dados locais
    print(f"Iniciando processo para Projeto: {PROJECT_ID}")
    create_view()
    
if __name__ == "__main__":
    load_data_to_bq()
