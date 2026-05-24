from views.novo_registro_view import novo_input
from utils.conversao_data import string_para_data

# Validação de data a partir da função de conversão e trata erro caso informada incorretamente
def validar_data(data: str):
    # Função interna para tratamento de conversão: caso a data informada seja convertida para datetime corretamente, ela é retornada com o padrão correto
    def tentativa_conversao(data_converter: str):   
        try:
            return string_para_data(data_converter).strftime('%d/%m/%Y')
        except:
            return False
        
    data_final = tentativa_conversao(data)

    while data_final is False:
        data_final = novo_input("data (dd/mm/aaaa)")
        data_final = tentativa_conversao(data_final)

    return data_final


# Validação de nível
def validar_nivel(nivel: str):
    while nivel.upper() not in ['E', 'P']:
        nivel = novo_input("nível (E ou P)")

    if nivel.upper() == 'E':
        return 'Empresarial'
    else:
        return 'Pessoal'
    

# Validação de tipo
def validar_tipo(tipo: str):
    while tipo.upper() not in ['E', 'S']:
        tipo = novo_input("tipo (E ou S)")

    if tipo.upper() == 'E':
        return 'Entrada'
    else:
        return 'Saída'


# Valida o valor informado pela conversão para float (número real)
def validar_valor(valor: str):
    valido = False
    while not valido:
        try:
            valor = float(valor)
            valido = True
        except ValueError:
            valido = False
            valor = novo_input("Valor")

    return valor


# Verifica se os campos de string (descrição, categoria e cliente) não estão vazios
def validar_strings_comum(dado: str, campo: str):
    while dado.strip() == "":
        dado = novo_input(campo)

    return dado