from .validadores_campos_registro import validar_data, validar_nivel, validar_strings_comum, validar_tipo

# Função de validação: garante que todos os campos sejam preenchidos corretamente
def validacoes_novo_registro(dados: dict):
    # Atualização de dicionário com os resultados das validações
    dados['Tipo'] = validar_tipo(dados['Tipo'])
    dados['Nível'] = validar_nivel(dados['Nível'])
    dados['Data'] = validar_data(dados['Data'])
    dados['Categoria'] = validar_strings_comum(dados['Categoria'], 'categoria')
    dados['Cliente'] = validar_strings_comum(dados['Cliente'], 'cliente')
    dados['Descrição'] = validar_strings_comum(dados['Descrição'], 'descrição da movimentação')

    return dados

# Função de validação do novo valor ao campo escolhido para edição
def validador_edicao_campo(campo: str, novo_valor: str):
    if campo in ('Categoria', 'Cliente', 'Descrição'):
        novo_valor = validar_strings_comum(novo_valor, campo)
    elif campo == 'Tipo':
        novo_valor = validar_tipo(novo_valor)
    elif campo == 'Nível':
        novo_valor = validar_nivel(novo_valor)
    elif campo == 'Data':
        novo_valor = validar_data(novo_valor)

    return novo_valor

#Função de validação do nível relacionado ao valor limite
def validador_limite(dados_limite: dict):
    # Atualização do dicionário com o resultado da validação
    dados_limite['Nível'] = validar_nivel(dados_limite['Nível'])

    return dados_limite

def validacao_parametro_busca(parametro_escolhido: int):
    pass
