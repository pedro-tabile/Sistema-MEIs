# Fornece os campos para preenchimento de novo registro
def infos_novo_registro():
    dados = {
        "Id": None,
        "Tipo": input("Tipo (E para entrada ou S para saída): "),
        "Valor": (input("Valor (R$): ")),
        "Descrição": input("Descrição da movimentação: "),
        "Data": input("Data (dd/mm/aaaa): "),
        "Nível": input("Nível (E para empresarial ou P para pessoal): "),
        "Categoria": input("Categoria: "),
        "Cliente": input("Cliente: "),
    }
    print()
    
    return dados

# Função de validação/correção geral
def novo_input(tipo: str):
    input_new = input(f"Insira um valor válido para {tipo}: ")

    return input_new