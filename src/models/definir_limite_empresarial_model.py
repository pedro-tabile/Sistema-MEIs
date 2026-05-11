from .manipular_json import ler_dados, gravar_dados

def definir_limite(nivel: str, valor: float):
    dados_json = ler_dados()

    dados_json['dados']['Limites'][0][nivel] = valor
    
    return gravar_dados(dados_json["dados"])


"""def definir_limite(valor: float):
    dados_json = ler_dados()
    
    dados_json['dados']['limites'][0][tipo: str] = valor
    
    return gravar_dados(dados_json["dados"])
    """