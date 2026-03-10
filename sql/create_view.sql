-- View no BigQuery para consolidar os dados

CREATE OR REPLACE VIEW `seu_projeto.seu_dataset.vw_games_consolidados` AS
SELECT
    g.game_id,
    g.name,
    g.release_date,
    p.publisher_name,
    m.metascore,
    m.user_score
FROM
    `seu_projeto.seu_dataset.games` g
LEFT JOIN
    `seu_projeto.seu_dataset.game_publishers` p ON g.game_id = p.game_id
LEFT JOIN
    `seu_projeto.seu_dataset.game_metacritic_platforms` m ON g.game_id = m.game_id
-- Adicionar os demais JOINs conforme as 8 tabelas definidas:
-- 1. games
-- 2. game_metacritic_platforms
-- 3. game_publishers
-- 4. game_stores
-- 5. game_derived_metrics
-- 6. game_ratings
-- 7. game_genres
-- 8. game_platforms
;
