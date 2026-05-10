from .manipular_json import ler_dados, gravar_dados

# Função responsável por ler o arquivo JSON,
# alterar os valores e salvá-los novamente com as alterações realizadas.
def definir_limite_pessoal(valor: float):
    dados_json = ler_dados()
    
    dados_json['dados']['limites'][0]['Pessoal'] = valor
    
    return gravar_dados(dados_json["dados"])