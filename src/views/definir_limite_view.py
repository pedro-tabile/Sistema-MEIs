#Função responsável por solicitar ao usuário o valor limite e seu tipo (empresarial ou pessoal)
def infos_limite():
    dados_limite = {
        "Tipo": str(input("Tipo (E para entrada ou S para saída): ")),
        "Valor": float(input("Valor limite (R$): ")),
    }
    
    print()

    return dados_limite

# Função de validação/correção geral
def novo_input(tipo: str):
    input_new = input(f"Insira um valor válido para {tipo}: ")
    print()

    return input_new