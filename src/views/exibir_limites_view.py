from utils.formatacao_real import formatar_valor

# Função para exibição de limites registrados
def exibir_limites(valores: dict):
    print (f'Limite Empresarial: R$ {formatar_valor(valores['Empresarial'])}')
    print (f'Limite Pessoal: R$ {formatar_valor(valores['Pessoal'])}\n')