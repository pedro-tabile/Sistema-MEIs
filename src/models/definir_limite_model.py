from .manipular_json import ler_dados, gravar_dados

#Função responsável por salvar os dados relacionados ao limite definido
def definir_limite(nivel: str, valor: float):
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json

    dados_json['dados']['limites'][nivel] = valor
    
    return gravar_dados(dados_json["dados"])