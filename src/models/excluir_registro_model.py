from .manipular_json import ler_dados, gravar_dados
from .buscar_index import buscar_indice

# Exclui registro a partir do id
def exclusao_registro(id: int):
    # Lê os registros existentes e busca o índice do registro com o id informado
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    index = buscar_indice(id)

    if type(index) is dict:
        return index

    # Exclui o registro com o id e faz a gravação da lista atualizada
    del dados_json['dados']['registros'][index]
    resultado_exclusao = gravar_dados(dados_json['dados'])

    return resultado_exclusao