import pandas as pd
from google.cloud import bigquery
import os

# Configurações do BigQuery - IDs Reais
PROJECT_ID = "directed-mender-489100-m3"
DATASET_RAW = "games_data"             # Dataset com as tabelas originais (Bronze)
DATASET_ANALYTICS = "games_analytics"   # Dataset para a Visão Final (Silver/Gold)

def create_view():
    """Cria ou substitui uma View no BigQuery unindo as tabelas principais em um dataset separado."""
    client = bigquery.Client(project=PROJECT_ID)
    
    # Garante que o dataset de analytics existe
    dataset_ref = client.dataset(DATASET_ANALYTICS)
    try:
        client.get_dataset(dataset_ref)
    except Exception:
        print(f"Criando dataset {DATASET_ANALYTICS}...")
        client.create_dataset(bigquery.Dataset(dataset_ref))

    view_id = f"{PROJECT_ID}.{DATASET_ANALYTICS}.vw_analise_games"
    
    sql_view = f"""
    CREATE OR REPLACE VIEW `{view_id}` AS
    SELECT
        g.id AS game_id,
        g.name AS nome_jogo,
        g.released AS data_lancamento,
        g.rating AS nota_usuarios,
        g.metacritic AS nota_critica,
        g.playtime AS tempo_jogo_horas,
        g.playtime AS tempo_jogo_horas,
        p.publisher_name AS distribuidora,
        gen.genre_name AS genero,
        plat.platform_name AS plataforma,
        m.completability_index AS indice_conclusao,
        m.consensus_score AS score_consenso,
        m.time_rating_ratio AS relacao_tempo_nota
    FROM
        `{PROJECT_ID}.{DATASET_RAW}.games` g
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_RAW}.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_RAW}.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_RAW}.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)
    LEFT JOIN
        `{PROJECT_ID}.{DATASET_RAW}.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING)
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
