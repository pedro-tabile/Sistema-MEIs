from views.opcoes_view import exibicao_opcoes
from controllers.acoes_controller import direcionar_escolha
from views.mensagens_gerais import msg_inicio, msg_fim

# Fluxo de execução do programa (início, escolha de opções e fim)
def fluxo_execucao():
    msg_inicio()

    opcao_escolhida = -1
    while opcao_escolhida != 0:
        # Referência à primeira interface (opções de ação)
        exibicao_opcoes()

        # Valida e direciona opção escolhida
        opcao_escolhida = direcionar_escolha()
    
    msg_fim()