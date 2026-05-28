from tabulate import tabulate

# Input que solicita id do registro a ser editado
def msg_id_edicao():
    return input('Informe o ID do registro a ser editado: ')

# Exibe tabela do registro a ser editado
def exibir_tabela(dados: dict, pos_exibicao: str):
    lista_dados = []
    dados_copia = dados.copy()
    
    # Adiciona os valores de cada chave dos registros (agrupados por listas) em uma lista geral linha
    dados_copia['Valor'] = f"{dados_copia['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

    # Formata o valor para o padrão monetário brasileiro
    lista_dados.append(list(dados_copia.values()))

    # Adiciona as chaves (comuns para todos os registros) da primeira ocorrência em uma lista para headers
    lista_headers = list(dados_copia.keys())

    if pos_exibicao == 'Início': print()
    print(f"{tabulate(lista_dados, headers=lista_headers, tablefmt='github', disable_numparse=True)}\n")
    

# Fornece a lista de opções (obtida pelas chaves do dicionário do registro) do campo a ser editado e retorna o valor escolhido
def campos_disponiveis(dados: dict):
    lista_opcoes = list(dados.keys())[1:]
    
    for i, item in enumerate(lista_opcoes):
        print(f"{i} - {item}")
    
    print(f'{len(lista_opcoes)} ou outro - Cancelar ou Sair')
    
    return input('\nCampo a ser editado: ')


# Mensagem de cancelamento de edição
def msg_cancelar_edicao():
    print("\n\033[31mEdição cancelada!\033[m\n")


# Solicitação de novo valor para o campo
def novo_valor(campo: str):
    msg = input(f'\nInforme um novo valor para o campo {campo}: ')
    print()
    return msg