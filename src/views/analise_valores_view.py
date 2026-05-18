from tabulate import tabulate
from utils.formatacao_real import formatar_valor

# Mensagem geral da análise, informando o total movimentado e o total de entradas e saídas, junto às porcentagens com relação ao total
def mensagem_movimentacoes(dados: dict):
    total_entradas, total_saidas = formatar_valor(dados['totais']['total_entradas']), formatar_valor(dados['totais']['total_saidas'])
    porc_entradas, porc_saidas = dados['porcentagens']['entradas'], dados['porcentagens']['saidas']

    print(f"Você já movimentou R$ {formatar_valor(dados['totais']['total_geral'])}!")
    print(f"R$ {total_entradas} em entradas ({porc_entradas:.2f}%) e R$ {total_saidas} em saídas ({porc_saidas:.2f}%).")


# Função que define qual mensagem é exibida conforme balanço (diferença entre entradas e saídas) - Lucro, prejuízo ou equilíbrio
def lucro_prejuizo(resultado_balanco: dict):
    porc = resultado_balanco['porcentagem']
    balanco = resultado_balanco['balanco']

    # Conteúdo de exibição abaixo:
    if resultado_balanco['constatacao_balanco'] == "Lucro":
        print(f"  - Você teve um lucro de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    elif resultado_balanco['constatacao_balanco'] == "Prejuízo":
        print(f"  - Você teve um prejuízo de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    else:
        print("  - Você teve um equilíbrio de gastos e receitas!")


# Exibição de total de entrada e saída, balanço, total movimentado e porcentagem do total movimentado em relação ao total geral por categoria 
# em formato de tabela 
def valores_categorias(valores_categorias: dict):
    lista_headers = ['Categoria', 'Entradas', 'Saídas', 'Balanço', 'Total movimentado (porcentagem do total geral)']
    lista_dados = []

    # Separador
    print("-" * 115)

    # Laço que percorre item do dicionário das categorias e adiciona à lista de dados uma lista com o nome da categoria e os valores envolvidos
    # depois de formatados
    for chave, item in valores_categorias.items():
        # Adiciona à lista da categoria (definida pela chave) os valores e porcentagem formatados
        lista_items = [
            chave, 
            formatar_valor(item['entrada']), 
            formatar_valor(item['saida']), 
            formatar_valor(item['balanco']), 
            f"{formatar_valor(item['movimentado'])} ({item['porc_movimentacao']:.2f})"
        ]

        lista_dados.append(lista_items)
        
    print("Tabela de análise de valores por categoria - Valores em reais (R$)\n")
    print(tabulate(lista_dados, headers=lista_headers, tablefmt='github', disable_numparse=True))

    # Separador
    print("-" * 115)

# Função que define exibição de valores, balanço e limite dos níveis (empresarial e pessoal)
def niveis_limites(dados_nivel: dict, nivel: str):
    # Mensagens, para ambos os níveis, de quanto foi gasto e do limite de gastos, informando, em sequência, o balanço (excedeu, dentro ou igual ao limite) 
    # e a porcentagem com relação ao limite.
    print(f"Nível {nivel}:")
    print(f"  - Você teve um gasto de R$ {formatar_valor(dados_nivel['total_gasto'])} para um limite de R$ {formatar_valor(dados_nivel['limite'])}.")
    if dados_nivel['constatacao_balanco'] == 'Excedeu':
        print(f"  - Você excedeu o limite em R$ {formatar_valor(dados_nivel['balanco_limite'])} - {(dados_nivel['porcentagem'] - 100):.2f}% a mais que o limite!")
    elif dados_nivel['constatacao_balanco'] == 'Dentro':
        print(f"  - Você ficou dentro do limite, sobrando R$ {formatar_valor(dados_nivel['balanco_limite'])} - com gastos de {dados_nivel['porcentagem']:.2f}% do limite!")
    else:
        print("Você atingiu o limite!") 

    print()

# Mensagem exibida em caso de limite indefinido para algum nível
def sem_limite_definido(nivel_limite: str):
    print(f"Nível {nivel_limite}:")
    print("  - Sem análise: limite é 0 ou não há limite definido!")

    print()