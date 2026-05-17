from utils.formatacao_real import formatar_valor

# Mensagem geral da análise, informando o total movimentado e o total de entradas e saídas, junto às porcentagens com relação ao total
def mensagem_movimentacoes(dados: dict):
    total_entradas, total_saidas = formatar_valor(dados['totais']['total_entradas']), formatar_valor(dados['totais']['total_saidas'])
    porc_entradas, porc_saidas = dados['porcentagens']['entradas'], dados['porcentagens']['saidas']

    print("-" * 80)

    print(f"Você já movimentou R$ {formatar_valor(dados['totais']['total_geral'])}!")
    print(f"R$ {total_entradas} em entradas ({porc_entradas:.2f}%) e R$ {total_saidas} em saídas ({porc_saidas:.2f}%).")

# Função que define qual mensagem é exibida conforme balanço (diferença entre entradas e saídas) - Lucro, prejuízo ou equilíbrio
def lucro_prejuizo(resultado_balanco: dict):
    porc = resultado_balanco['porcentagem']
    balanco = resultado_balanco['balanco']

    if resultado_balanco['constatacao_balanco'] == "Lucro":
        print(f"\nVocê teve um lucro de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    elif resultado_balanco['constatacao_balanco'] == "Prejuízo":
        print(f"\nVocê teve um prejuízo de R$ {formatar_valor(balanco)}! Isso representa {porc:.2f}% do total movimentado.")
    else:
        print("\nVocê teve um equilíbrio de gastos e receitas!")

# Função que define balanço das saídas e limites empresarial e pessoal (caso algum limite seja 0 - ou não informado - a mensagem de impossibilidade)
# de análise é informada
def niveis_limites(dados_niveis: dict):
    print("-" * 80)

    # Laço responsável por exibir as mensagens (comuns) para os 2 níveis, garantindo a exibição do(s) que existir(em).
    for item in dados_niveis:
        # Pega valores da chave (Empresarial ou Pessoal)
        dados = dados_niveis.get(item)

        # Mensagens, para ambos os níveis, de quanto foi gasto e do limite de gastos, informando, em sequência, o balanço (excedeu, dentro ou igual ao limite) 
        # e a porcentagem com relação ao limite. Além disso, exibe as informações somente caso haja algum limite (ou seja, se o dicionário recebido tem 
        # alguma chave equivalente ao nível Empresarial ou Pessoal)
        print(f"Nível {item}:")
        print(f"  - Você teve um gasto de R$ {formatar_valor(dados['total_gasto'])} para um limite de R$ {formatar_valor(dados['limite'])}.")
        if dados['constatacao_balanco'] == 'Excedeu':
            print(f"  - Você excedeu o limite em R$ {formatar_valor(dados['balanco_limite'])} - {(dados['porcentagem'] - 100):.2f}% a mais que o limite!")
        elif dados['constatacao_balanco'] == 'Dentro':
            print(f"  - Você ficou dentro do limite, sobrando R$ {formatar_valor(dados['balanco_limite'])} - com gastos de {dados['porcentagem']:.2f}% do limite!")
        else:
            print("Você atingiu o limite!")

        print()

# Mensagem exibida em caso de limite indefinido para algum nível
def sem_limite_definido(nivel_limite: str):
    print(f"Nível {nivel_limite}:")
    print("  - Sem análise: limite é 0 ou não há limite definido!")
    print()



# def valores_categorias(valores_categorias: dict):
#     print("-" * 80)

#     print("Entradas por categoria:")
#     for chave, valor in valores_categorias['Entradas'].items():
#         print(f"  - {chave}: R$ {formatar_valor(valor)}")

#     print("\nSaídas por categoria:")
#     for chave, valor in valores_categorias['Saídas'].items():
#         print(f"  - {chave}: R$ {formatar_valor(valor)}")

#     print()