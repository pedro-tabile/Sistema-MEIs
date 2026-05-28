from tabulate import tabulate
from utils.formatacao_real import formatar_valor

# Função responsável pela exibição da tabela de registros
def tabela_registros(dados_exibicao: list):
    lista_dados = []

    # Loop que adiciona os valores de cada chave dos registros (agrupados por listas) em uma lista geral
    for item in dados_exibicao:
        # A linha abaixo formata o valor para o padrão monetário brasileiro
        item['Valor'] = formatar_valor(item['Valor'])
        lista_dados.append(list(item.values()))

    # Adiciona as chaves (comuns para todos os registros) da primeira ocorrência em uma lista para headers
    lista_headers = list(dados_exibicao[0].keys())

    print(f"{tabulate(lista_dados, headers=lista_headers, tablefmt='github', disable_numparse=True)}\n")

# Lista com dicionário contendo id e descrição da opção, de modo a facilitar manipulação de dados no controller e no model
opcoes_params = [
    {
        "id": 1,
        "param": "Nível"
    }, 
    {
        "id": 2,
        "param": "Categoria"
    }, 
    {
        "id": 3,
        "param": "Tipo"
    }
]
    
# Opções para busca parametrizada, solicitando a opção (ou seja, o parâmetro) que o usuário deseja para exibir os registros
def parametros():
    for item in opcoes_params:
        print(f"{item['id']} - Por {item['param']}")

    opcao = input("\nEscolha a opção para filtrar registros: ")
    print()

    return opcao

# Função que solicita que o usuário informe o que deseja filtrar com base no parâmetro escolhido (tipo, nível ou categoria), definindo, 
# assim, a saída adequada para correspondência no arquivo
def retorno_parametro_escolhido(parametro_escolhido: int):
    filtro = None

    if parametro_escolhido == 1:
        nivel = input("Empresarial (E) ou pessoal (P): ").upper()

        if nivel == 'E': 
            filtro = 'Empresarial'
        elif nivel == 'P': 
            filtro = 'Pessoal'

    elif parametro_escolhido == 2:
        filtro = input("Informe a categoria: ")

    else:
        tipo = input("Entrada (E) ou Saída (S): ").upper()

        if tipo == 'E': 
            filtro = 'Entrada'
        elif tipo == 'S': 
            filtro = 'Saída'

    print()

    return filtro