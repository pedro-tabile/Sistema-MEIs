from utils.formatacao_real import formatar_valor

# Mensagem geral da análise, informando o total movimentado e o toal de entradas e saídas, junto às porcentagens com relação ao total
def mensagem_movimentacoes(dados: dict):
    total_entradas, total_saidas = formatar_valor(dados['total_entradas']), formatar_valor(dados['total_saidas'])
    porc_entradas, porc_saidas = dados['porcentagens']['entradas'], dados['porcentagens']['saidas']

    print(f"Você já movimentou R$ {formatar_valor(dados['total_geral'])}!")
    print(f"R$ {total_entradas} em entradas ({porc_entradas:.2f}%) e R$ {total_saidas} em saídas ({porc_saidas:.2f}%).")

# Função que define qual mensagem é exibida conforme balanço (diferença entre entradas e saídas)
def lucro_prejuizo(resultado_balanco: dict):
    porc = resultado_balanco['porcentagem']
    balanco = resultado_balanco['balanco']

    if resultado_balanco['constatacao_balanco'] == "Lucro":
        print(f"\nVocê teve um lucro de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    elif resultado_balanco['constatacao_balanco'] == "Prejuízo":
        print(f"\nVocê teve um prejuízo de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    else:
        print("\nVocê teve um equilíbrio de gastos e receitas!")


def valores_categorias(valores_categorias: dict):
    print("-" * 60)

    print("Entradas por categoria:")
    for chave, valor in valores_categorias['Entradas'].items():
        print(f"  - {chave}: R$ {formatar_valor(valor)}")

    print("\nSaídas por categoria:")
    for chave, valor in valores_categorias['Saídas'].items():
        print(f"  - {chave}: R$ {formatar_valor(valor)}")

    print()