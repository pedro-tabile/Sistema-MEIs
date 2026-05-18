# Função que formata o valor informado para o padrão brasileiro: 1.000,00
def formatar_valor(valor: float):
    return f"{valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')