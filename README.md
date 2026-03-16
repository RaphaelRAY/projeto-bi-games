# Inteligência de Negócios - Análise do Mercado de Games

## Objetivo
Analisar o mercado de games integrando dados de avaliações (como o Metacritic), informações de produtoras (publishers) e disponibilidade nas lojas. O intuito é extrair insights valiosos sobre o desempenho comercial e a recepção dos jogos pelo público e crítica, auxiliando na tomada de decisões estratégicas.

## Tecnologias
- **Linguagem:** Python
- **Armazenamento/Data Warehouse:** Google BigQuery
- **Visualização de Dados:** Looker Studio / Power BI

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
├── notebooks/              # Jupyter Notebooks (Cloud & Local)
│   ├── 01_importar_dados.ipynb
│   └── 02_criar_view.ipynb
├── src/                    # Scripts Python
│   └── main.py             # Automação da Carga e View
├── docs/                   # Documentação e Apresentação
│   ├── apresentacao.pptx
│   └── dashboard_print.png
├── .gitignore              # Arquivo de ignore do Git
├── README.md               # Guia do Projeto (Este arquivo)
└── requirements.txt        # Bibliotecas Python
```

### Links Rápidos (Execução no Cloud)
Para rodar os processos diretamente no navegador via Google Colab:

1. **Passo 1: Importação**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RaphaelRAY/projeto-bi-games/blob/main/notebooks/01_importar_dados.ipynb)  
2. **Passo 2: Criar View**: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RaphaelRAY/projeto-bi-games/blob/main/notebooks/02_criar_view.ipynb)

## Como Rodar Localmente
1. **Instale as dependências**: `pip install -r requirements.txt`
2. **Execute o processo**:
   ```bash
   python src/main.py
   ```
3. **Dashboard**: Conecte o BigQuery no Looker Studio e aponte para a View `vw_analise_games`.
