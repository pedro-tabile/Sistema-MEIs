from .manipular_json import ler_dados, gravar_dados

def definir_limite_empresarial(valor: float):
    dados_json = ler_dados()

    dados_json['dados']['Limites'][0]['Empresarial'] = valor
    
    return gravar_dados(dados_json["dados"])
    