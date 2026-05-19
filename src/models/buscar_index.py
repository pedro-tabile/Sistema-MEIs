from .manipular_json import ler_dados

# Busca indíce que correspondente ao id do registro
def buscar_indice(id: int):
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    index_registro = None

    # Laço de repetição para encontrar o índice do id
    for indice, item in enumerate(dados_json['dados']['registros']):
        if item['Id'] == id:
            index_registro = indice
            break

    return index_registro
