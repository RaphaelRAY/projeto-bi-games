# Inteligência de Negócios - Análise do Mercado de Games

[![YouTube](https://img.shields.io/badge/▶%20Apresentação-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=1iNsk7gmoC8)
[![Looker Studio](https://img.shields.io/badge/📊%20Dashboard-Looker%20Studio-4285F4?logo=google)](https://lookerstudio.google.com/reporting/25f30f16-95a1-4712-ad4e-61f5bb8d4407)

## Objetivo
Analisar o mercado de games integrando dados de avaliações (como o Metacritic), informações de produtoras (publishers) e disponibilidade nas lojas. O intuito é extrair insights valiosos sobre o desempenho comercial e a recepção dos jogos pelo público e crítica, auxiliando na tomada de decisões estratégicas.

## Tecnologias
- **Linguagem:** Python
- **Armazenamento/Data Warehouse:** Google BigQuery
- **Visualização de Dados:** Looker Studio

## Diagrama de Dados
O modelo de dados é estruturado em torno da entidade principal de jogos e as suas respectivas dimensões:
1. **`games`**: Tabela principal de identificação.
2. **`game_metacritic_platforms`**: Notas da crítica especializada.
3. **`game_publishers`**: Produtoras/empresas.
4. **`game_stores`**: Lojas de venda.
5. **`game_derived_metrics`**: Métricas de tempo e engajamento.
6. **`game_ratings`**: Preferências e distribuição de notas.
7. **`game_genres`**: Categorias de estilo.
8. **`game_platforms`**: Hardwares compatíveis.

## Estrutura do Projeto
```text
projeto-bi-games/
├── data/                   # Pasta para os arquivos CSV
├── sql/                    # Queries SQL para conferência
│   └── create_view.sql     # Código SQL da View (Nomes em Português)
├── notebooks/              # Jupyter Notebooks (Google Colab)
│   ├── 01_importar_dados.ipynb
│   └── 02_criar_view.ipynb
├── docs/                   # Documentação e Apresentação
│   ├── apresentacao.pptx
│   └── dashboard_print.png
├── .gitignore              # Arquivo de ignore do Git
├── README.md               # Guia do Projeto (Este arquivo)
└── requirements.txt        # Bibliotecas Python
```

### 🚀 Como Executar (Google Colab)
Rode os processos diretamente no navegador, sem instalação local:

1. **Passo 1: Importação**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RaphaelRAY/projeto-bi-games/blob/main/notebooks/01_importar_dados.ipynb)
2. **Passo 2: Criar View**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RaphaelRAY/projeto-bi-games/blob/main/notebooks/02_criar_view.ipynb)

## 📊 Dashboard
Acesse o dashboard interativo diretamente no Looker Studio:

👉 **[Abrir Dashboard](https://lookerstudio.google.com/reporting/25f30f16-95a1-4712-ad4e-61f5bb8d4407)**

O projeto oferece duas visões no dataset **`games_analytics`**:
- `vw_analise_games`: Visão detalhada para filtros de plataforma/gênero.
- `vw_analise_games_unica`: Visão consolidada (1 linha por jogo) para Scorecards e Médias.

## 🎥 Apresentação em Vídeo
Assista à apresentação completa do projeto:

👉 **[Assistir no YouTube](https://www.youtube.com/watch?v=1iNsk7gmoC8)**

Para um roteiro completo de como montar seu dashboard, consulte o [Plano de Dashboard](docs/plano_dashboard_looker.md).
