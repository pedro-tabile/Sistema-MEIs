# Input que solicita id do registro a ser excluído
def msg_id_exclusao():
    return int(input('Informe o ID do registro a ser excluído: '))

# Mensagem de solicitação de confirmação para exclusão
def msg_confirmacao():
    return input("\nTem certeza que deseja excluir esse registro? (Pressione T para confirmar): ")

# Mensagem de cancelamento de exclusão
def msg_cancelamento():
    print("\nExclusão cancelada!\n")

# Mensagem exibida caso o Id informado não exista
def registro_inexistente():
    print("\nNão foi encontrado nenhum registro com esse Id!\n")