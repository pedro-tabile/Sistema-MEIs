#Função responsável por solicitar ao usuário o valor limite e seu tipo (empresarial ou pessoal)
def infos_limite():
    dados_limite = {
        "Nível": str(input("Nível (E para empresarial ou P para pessoal): ")),
        "Valor": float(input("Valor limite (R$): ")),
    }

    return dados_limite