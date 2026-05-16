from .manipular_json import ler_dados

# Lê os dados (registros) existentes no arquivo e os retorna (caso algum exista)
def buscar_registros():
    return ler_dados()

# Busca os registros que correspondem ao filtro e ao parâmetro informados
def buscar_registros_parametros(filtro: str, parametro: int):
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    dados_filtrados = []
    # Faz a correspondência e armazena
    for item in dados_json['dados']['registros']:
        if item[parametro] == filtro:
            dados_filtrados.append(item)

    return {'sucesso': True, 'dados': dados_filtrados}