from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Função que exibe os gráficos com os valores - biblioteca Plotly
def exibir_graficos(dados: dict):
    # Atribui os valores passados por parâmetro (correspondência de dados por categorias, níveis e tipos) às variáveis
    valores_niveis, valores_tipos, valores_categorias = dados['valores_niveis'], dados['valores_tipos'], dados['valores_categorias']

    # Cria uma figura (grade de linhas e colunas) para organizar/abranger os gráficos (1 x 3)
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'domain'}, {'type': 'domain'}, {'type': 'domain'}]])
    
    # Configuração dos 3 gráficos com dados, legendas e informações necessárias
    fig.add_trace(go.Pie(values=list(valores_niveis.values()), labels=list(valores_niveis.keys()), title="Valores por nível", textinfo='percent+value'), 1, 1)
    fig.add_trace(go.Pie(values=list(valores_tipos.values()), labels=list(valores_tipos.keys()), title="Valores por tipo", textinfo='percent+value'), 1, 2)
    fig.add_trace(go.Pie(values=list(valores_categorias.values()), labels=list(valores_categorias.keys()), title="Valores por categoria", textinfo='percent+value'), 1, 3)

    # Configurações de layout
    fig.update_layout(title_text="Gráficos de Valores Movimentados por Níveis, Tipos e Categorias")
    fig.update_traces(hoverinfo="percent+label+value", hovertemplate="%{label}<br>%{percent}<br>%{value:.2f}<extra></extra>", texttemplate="%{percent}<br>%{value:.2f}")
    fig.update_traces(title_font=dict(size=16))

    # Renderização (exibição) da figura com os gráficos no navegador
    fig.show(renderer="browser")