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