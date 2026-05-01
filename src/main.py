from views.interface_inicial import exibicao_inicial
from controllers.validacoes import validacao_escolha

def main():
    #Referencia a primeira interface (opções de ação)
    exibicao_inicial()

    #Valida opção escolhida
    validacao_escolha()

#Garante que a função main sempre seja a executada
if __name__ == "__main__":
    main()