#Fornece os campos para preenchimento de novo registro
def infos_novo_registro():
    print()

    dados = {
        "tipo": input("Tipo (E para entrada ou S para saída): "),
        "valor": float(input("Valor (R$): ")),
        "descricao": input("Descrição da movimentação: "),
        "data": input("Data (dd/mm/aaaa): "),
        "nivel": input("Nível (E para empresarial ou P para pessoal): "),
        "categoria": input("Categoria: "),
        "cliente": input("Cliente: "),
    }

    return dados