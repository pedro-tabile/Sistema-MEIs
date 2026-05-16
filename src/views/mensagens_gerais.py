# Mensagem de boas-vindas
def msg_inicio():
    print('Bem-vindo ao sistema de gerenciamento monetário dos MEIs!\n')

# Mensagem de fim de execução do programa
def msg_fim():
    print("Programa finalizado!")

# Mensagem de erro ao escolher opção de ação
def opcao_invalida():
    print("Opção inválida!\n")

# Mensagem de erro: ação não executada ou falha na execução
def mensagem_erro(erro: str):
    print(f"Ocorreu um erro ao tentar executar ação: {erro}\n")

# Mensagem de ação executada com sucesso
def mensagem_sucesso(acao_sucesso: int):
    match acao_sucesso:
        case 1:
            print("Movimentação registrada com sucesso!\n")

        case 2:
            print("Registros encontrados com sucesso!\n")

        case 3:
            print("\nRegistro atualizado com sucesso!\n")

        case 4:
            print("\nRegistro excluído com sucesso!\n")

        case 5:
            print("Gráficos gerados com sucesso!\n")

        case 6:
            print("Registros filtrados com sucesso!\n")

# Mensagem exibida caso o Id informado não exista
def registro_inexistente():
    print("\nNão foi encontrado nenhum registro com esse Id!\n")

# Mensagem exibida caso não haja nenhum registro no arquivo
def sem_registros():
    print("Nenhum registro encontrado!\n")