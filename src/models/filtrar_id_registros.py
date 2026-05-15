from models.manipular_json import ler_dados

# Busca as correspondências (itens) de determinado campo nos registros do arquivo, retornado a quantidade e os itens encontrados
def buscar_filtro_id(campo: str):
    registros_json = ler_dados()

    if registros_json['sucesso'] is False:
        return registros_json

    itens_encontrados = []

    for item in registros_json['dados']['registros']:
        itens_encontrados.append(item[campo])

    return {"sucesso": True, "quantidade": len(itens_encontrados), "itens_encontrados": itens_encontrados}