import json

notebook_path = r'c:\Users\rapha\Documents\Maua\Pos Ciencie e IA\Inteligência de Negócios\Projeto Final\projeto-bi-games\notebooks\02_criar_view.ipynb'

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The cell we want to modify is the one starting with "# Garante que o dataset de analytics existe"
# Based on previous view_file, it's the last code cell.

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and '# Garante que o dataset de analytics existe' in ''.join(cell['source']):
        cell['source'] = [
            "# Garante que o dataset de analytics existe\n",
            "dataset_ref = client.dataset(dataset_analytics)\n",
            "try:\n",
            "    client.get_dataset(dataset_ref)\n",
            "    print(f\"Dataset {dataset_analytics} já existe.\")\n",
            "except Exception:\n",
            "    print(f\"Criando dataset {dataset_analytics}...\")\n",
            "    client.create_dataset(bigquery.Dataset(dataset_ref))\n",
            "\n",
            "# 1. View Detalhada (para filtros de plataforma/gênero)\n",
            "view_id = f\"{project_id}.{dataset_analytics}.vw_analise_games\"\n",
            "\n",
            "sql_view = f\"\"\"\n",
            "CREATE OR REPLACE VIEW `{view_id}` AS\n",
            "SELECT\n",
            "    g.id AS game_id,\n",
            "    g.name AS nome_jogo,\n",
            "    g.released AS data_lancamento,\n",
            "    g.rating AS nota_usuarios,\n",
            "    g.metacritic AS nota_critica,\n",
            "    g.playtime AS tempo_jogo_horas,\n",
            "    p.publisher_name AS distribuidora,\n",
            "    gen.genre_name AS genero,\n",
            "    plat.platform_name AS plataforma,\n",
            "    m.completability_index AS indice_conclusao,\n",
            "    m.consensus_score AS score_consenso,\n",
            "    m.time_rating_ratio AS relacao_tempo_nota\n",
            "FROM\n",
            "    `{project_id}.{dataset_raw}.games` g\n",
            "LEFT JOIN\n",
            "    `{project_id}.{dataset_raw}.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)\n",
            "LEFT JOIN\n",
            "    `{project_id}.{dataset_raw}.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)\n",
            "LEFT JOIN\n",
            "    `{project_id}.{dataset_raw}.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)\n",
            "LEFT JOIN\n",
            "    `{project_id}.{dataset_raw}.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING)\n",
            "\"\"\"\n",
            "\n",
            "# 2. View Única (para KPIs e Médias sem duplicidade)\n",
            "view_kpi_id = f\"{project_id}.{dataset_analytics}.vw_analise_games_unica\"\n",
            "\n",
            "sql_view_kpi = f\"\"\"\n",
            "CREATE OR REPLACE VIEW `{view_kpi_id}` AS\n",
            "SELECT\n",
            "    g.id AS game_id,\n",
            "    g.name AS nome_jogo,\n",
            "    g.released AS data_lancamento,\n",
            "    g.rating AS nota_usuarios,\n",
            "    g.metacritic AS nota_critica,\n",
            "    g.playtime AS tempo_jogo_horas,\n",
            "    p.publisher_name AS distribuidora,\n",
            "    m.completability_index AS indice_conclusao,\n",
            "    STRING_AGG(DISTINCT plat.platform_name, ', ') AS plataformas,\n",
            "    STRING_AGG(DISTINCT gen.genre_name, ', ') AS generos\n",
            "FROM\n",
            "    `{project_id}.{dataset_raw}.games` g\n",
            "LEFT JOIN `{project_id}.{dataset_raw}.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)\n",
            "LEFT JOIN `{project_id}.{dataset_raw}.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)\n",
            "LEFT JOIN `{project_id}.{dataset_raw}.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)\n",
            "LEFT JOIN `{project_id}.{dataset_raw}.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING)\n",
            "GROUP BY 1, 2, 3, 4, 5, 6, 7, 8\n",
            "\"\"\"\n",
            "\n",
            "print(f\"Criando as views no dataset {dataset_analytics}...\")\n",
            "client.query(sql_view).result()\n",
            "client.query(sql_view_kpi).result()\n",
            "print(f\"✅ Sucesso! Views criadas e prontas para uso.\\nDetail View: {view_id}\\nKPI View: {view_kpi_id}\")"
        ]
        break

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2, ensure_ascii=False)
