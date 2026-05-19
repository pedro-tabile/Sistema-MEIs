# Mensagem de boas-vindas
def msg_inicio():
    # "\033[96m ... \033[m" refere-se à cor
    print('\033[96mBem-vindo ao sistema de gerenciamento monetário dos MEIs!\033[m\n')

# Mensagem de fim de execução do programa
def msg_fim():
    print("\033[96mPrograma finalizado!\033[m")

# Mensagem de erro ao escolher opção de ação
def opcao_invalida():
    print("\033[31mOpção inválida!\033[m\n")

# Mensagem de erro: ação não executada ou falha na execução
def mensagem_erro(erro: str):
    print(f"\033[31mOcorreu um erro ao tentar executar ação: {erro}\033[m\n")

# Mensagem de ação executada com sucesso
def mensagem_sucesso(acao_sucesso: int):
    match acao_sucesso:
        case 1:
            print("\033[92mMovimentação registrada com sucesso!\033[m\n")

        case 2:
            print("\033[92mRegistros encontrados com sucesso!\033[m\n")

        case 3:
            print("\n\033[92mRegistro atualizado com sucesso!\033[m\n")

        case 4:
            print("\n\033[92mRegistro excluído com sucesso!\033[m\n")

        case 5:
            print ("\n\033[92mLimite definido com sucesso!\033[m\n")   
        
        case 6:
            print("\033[92mLimites atuais exibidos com sucesso!\033[m\n")

        case 7:
            print("\033[92mGráficos gerados com sucesso!\033[m\n")

        case 8:
            print("\033[92mRegistros filtrados com sucesso!\033[m\n")
            
# Mensagem exibida caso o Id informado não exista
def registro_inexistente():
    print("\n\033[31mNão foi encontrado nenhum registro com esse Id!\033[m\n")

# Mensagem exibida caso não haja nenhum registro no arquivo
def sem_registros():
    print("\033[31mNenhum registro encontrado!\033[m\n")