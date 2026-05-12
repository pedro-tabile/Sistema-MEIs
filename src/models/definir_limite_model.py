from .manipular_json import ler_dados, gravar_dados

def definir_limite(nivel: str, valor: float):
    dados_json = ler_dados()

    dados_json['dados']['limites'][0][nivel] = valor
    
    return gravar_dados(dados_json["dados"])