from .manipular_json import ler_dados

# Função que retorna ao controller os dados dos limites do arquivo
def valores_limite():
    dados = ler_dados()

    if dados['sucesso'] is False:
        return dados

    return {
        "sucesso": True,
        "limites": dados['dados']['limites']
    }