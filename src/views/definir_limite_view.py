#Função responsável por solicitar ao usuário o valor limite e seu tipo (empresarial ou pessoal)
def infos_limite():
    dados_limite = {
        "Nível": input("Nível (E para empresarial ou P para pessoal): "),
        "Valor": input("Valor limite (R$): "),
    }

    print()

    return dados_limite