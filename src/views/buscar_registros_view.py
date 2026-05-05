from tabulate import tabulate

# Função responsável pela exibição da tabela de registros
def tabela_registros(dados_exibicao: dict):
    lista_dados = []

    # Loop que adiciona os valores de cada chave dos registros (agrupados por listas) em uma lista geral
    for item in dados_exibicao:
        # A linha abaixo formata o valor para o padrão monetário brasileiro
        item['Valor'] = f"{item['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        lista_dados.append(list(item.values()))

    # Adiciona as chaves (comuns para todos os registros) da primeira ocorrência em uma lista para headers
    lista_headers = list(dados_exibicao[0].keys())

    print(f"{tabulate(lista_dados, headers=lista_headers, tablefmt='github', disable_numparse=True)}\n")

# Mensagem exibida caso não haja nenhum registro no arquivo
def sem_registros():
    print('Nenhum registro encontrado!\n')