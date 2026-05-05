from .manipular_json import ler_dados, gravar_dados

# Busca registro a ser editado no arquivo
def buscar_registro_edicao(id_registro: int):
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    dados_registro = {}

    # Busca e retorna o dicionário do registro correspondente ao id escolhido
    for item in dados_json['dados']['registros']:
        if item['Id'] == id_registro:
            dados_registro = item

    return dados_registro

# Edita o campo e salva o arquivo com todos os dados atualizados
def editar_dados(dados_registro: dict, campo_edicao: str, novo_valor: str | float):
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json
    
    # Busca o registro do arquivo que corresponde ao do id escolhido e atualiza o campo com o novo valor
    for index, item in enumerate(dados_json['dados']['registros']):
        if item['Id'] == dados_registro['Id']:
            dados_registro[campo_edicao] = novo_valor
            dados_json['dados']['registros'][index] = dados_registro
            break

    gravacao = gravar_dados(dados_json['dados'])
    return gravacao