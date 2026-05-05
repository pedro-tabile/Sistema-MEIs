from models.buscar_registros_model import buscar_registros

# Busca as correspondências (itens) de determinado campo nos registros do arquivo, retornado a quantidade e os itens encontrados
def buscar_filtro(campo: str):
    registros_json = buscar_registros()

    if registros_json['sucesso'] is False:
        return registros_json

    itens_encontrados = []

    for item in registros_json['dados']['registros']:
        itens_encontrados.append(item[campo])

    return {"sucesso": True, "qntd": len(itens_encontrados), "itens_encontrados": itens_encontrados}