from .opcoes_acoes import opcoes

# Exibição inicial das opções de ações (importadas)
def exibicao_inicial():
    print('Bem-vindo ao sistema de finanças para Microempreendedores Individuais (MEIs)!\n')

    for item in opcoes:
        print(f'{item["id"]} - {item["mensagem"]}')

    print()


#Função usada pelo controller para solicitar ação
def escolher_opcao():
    opcao = int(input("Informe o número da ação que deseja realizar: "))
    return opcao