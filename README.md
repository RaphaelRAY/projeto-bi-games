# Inteligência de Negócios - Análise do Mercado de Games

## Objetivo
Analisar o mercado de games integrando dados de avaliações (como o Metacritic), informações de produtoras (publishers) e disponibilidade nas lojas. O intuito é extrair insights valiosos sobre o desempenho comercial e a recepção dos jogos pelo público e crítica, auxiliando na tomada de decisões estratégicas.

## Tecnologias
- **Linguagem:** Python
- **Armazenamento/Data Warehouse:** Google BigQuery
- **Visualização de Dados:** Looker Studio / Power BI

## Diagrama de Dados
O modelo de dados é estruturado em torno da entidade principal de jogos e as suas respectivas dimensões. As 8 tabelas selecionadas (O Modelo Final) são:

1. **`games`**: Tabela principal de identificação.
2. **`game_metacritic_platforms`**: Notas da crítica especializada (dados numéricos).
3. **`game_publishers`**: As produtoras/empresas que financiam os jogos.
4. **`game_stores`**: Onde o jogo é vendido (Digital ou Físico).
5. **`game_derived_metrics`**: Métricas de tempo de jogo e engajamento.
6. **`game_ratings`**: Preferências e distribuição de notas dos usuários.
7. **`game_genres`**: Categorias de estilo de jogo.
8. **`game_platforms`**: Consoles e hardware compatíveis.

**Relacionamento:** As tabelas dimensionais ligam-se à tabela principal `games` (geralmente por meio da chave `game_id` ou identificador similar), permitindo agregar dados sobre avaliações (metacritic), distribuição (lojas) e autoria (produtoras/desenvolvedoras).

## Estrutura do Projeto
```text
projeto-bi-games/
├── data/                   # Pasta para os arquivos CSV
├── sql/                    # Queries SQL para conferência
│   └── create_view.sql     # Código da View criada no BigQuery
├── notebooks/              # Jupyter Notebooks para testes e exploração
│   └── analise_exploratoria.ipynb
├── src/                    # O "coração" do projeto
│   └── main.py             # Script que carrega dados e gerencia a View no BQ
├── docs/                   # Documentação, apresentações e prints
│   ├── apresentacao.pptx
│   └── dashboard_print.png
├── .gitignore              # Arquivos e pastas a serem ignorados pelo git
├── README.md               # Guia principal do projeto (este arquivo)
└── requirements.txt        # Lista de dependências e bibliotecas
```

## Instruções
Siga os passos abaixo para rodar o script Python e replicar a carga dos dados:

1. **Abra o terminal na raiz do projeto (`projeto-bi-games/`).**
2. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   # No Windows:
   venv\Scripts\activate
   # No Mac/Linux:
   source venv/bin/activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configuração de Credenciais:**
   - Configure o acesso ao Google Cloud no seu ambiente local (usando o comando `gcloud auth application-default login` ou defina a variável de ambiente com o caminho do JSON da sua conta de serviço).
   - Modifique, se necessário, o arquivo `src/main.py` com o nome do seu projeto e dataset no BigQuery.
5. **Execução:**
   - Execute o script principal que processará os dados e os enviará para o BigQuery:
   ```bash
   python src/main.py
   ```
6. Conecte o BigQuery no Looker Studio ou Power BI para explorar as visões criadas.
