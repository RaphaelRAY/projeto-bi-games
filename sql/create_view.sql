-- View no BigQuery para consolidar os dados do Mercado de Games
-- Arquitetura: Camada Analytics (Silver/Gold) separada da Camada Raw (Bronze)
-- Requisito 4: Processo para criar a view via Python

CREATE OR REPLACE VIEW `directed-mender-489100-m3.games_analytics.vw_analise_games` AS
SELECT
    g.id AS game_id,
    g.name AS nome_jogo,
    g.released AS data_lancamento,
    g.rating AS nota_usuarios,
    g.metacritic AS nota_critica,
    g.playtime AS tempo_jogo_horas,
    g.ratings_count AS qtd_avaliacoes,
    g.reviews_count AS qtd_reviews,
    p.publisher_name AS distribuidora,
    gen.genre_name AS genero,
    plat.platform_name AS plataforma,
    m.completability_index AS indice_conclusao,
    m.consensus_score AS score_consenso,
    m.time_rating_ratio AS relacao_tempo_nota
FROM
    `directed-mender-489100-m3.games_data.games` g
LEFT JOIN
    `directed-mender-489100-m3.games_data.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)
LEFT JOIN
    `directed-mender-489100-m3.games_data.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)
LEFT JOIN
    `directed-mender-489100-m3.games_data.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)
LEFT JOIN
    `directed-mender-489100-m3.games_data.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING);

-- NOVA VIEW: vw_analise_games_unica (Ideal para KPIs e Médias)
-- Esta view agrupa plataformas e gêneros em uma única linha por jogo, evitando duplicações nas médias industriais.
CREATE OR REPLACE VIEW `directed-mender-489100-m3.games_analytics.vw_analise_games_unica` AS
SELECT
    g.id AS game_id,
    g.name AS nome_jogo,
    g.released AS data_lancamento,
    g.rating AS nota_usuarios,
    g.metacritic AS nota_critica,
    g.playtime AS tempo_jogo_horas,
    g.ratings_count AS qtd_avaliacoes,
    g.reviews_count AS qtd_reviews,
    p.publisher_name AS distribuidora,
    m.completability_index AS indice_conclusao,
    m.consensus_score AS score_consenso,
    m.time_rating_ratio AS relacao_tempo_nota,
    -- Agrupamos plataformas e gêneros para manter 1 linha por jogo
    STRING_AGG(DISTINCT plat.platform_name, ", ") AS plataformas,
    STRING_AGG(DISTINCT gen.genre_name, ", ") AS generos
FROM
    `directed-mender-489100-m3.games_data.games` g
LEFT JOIN `directed-mender-489100-m3.games_data.game_publishers` p ON CAST(g.id AS STRING) = CAST(p.game_id AS STRING)
LEFT JOIN `directed-mender-489100-m3.games_data.game_platforms` plat ON CAST(g.id AS STRING) = CAST(plat.game_id AS STRING)
LEFT JOIN `directed-mender-489100-m3.games_data.game_genres` gen ON CAST(g.id AS STRING) = CAST(gen.game_id AS STRING)
LEFT JOIN `directed-mender-489100-m3.games_data.game_derived_metrics` m ON CAST(g.id AS STRING) = CAST(m.game_id AS STRING)
GROUP BY 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12;
