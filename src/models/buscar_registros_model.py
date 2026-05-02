from .manipular_json import ler_dados

# Lê os dados (registros) existentes no arquivo e os retorna (caso algum exista)
def buscar_registros():
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    return dados_json