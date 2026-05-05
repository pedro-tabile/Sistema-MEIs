# Input que solicita id do registro a ser excluído
def msg_id_exclusao():
    return int(input('Informe o ID do registro a ser excluído: '))

# Mensagem de solicitação de confirmação para exclusão
def msg_confirmacao():
    return input("\nTem certeza que deseja excluir esse registro? (Pressione T para confirmar): ")

# Mensagem de cancelamento de exclusão
def msg_cancelar_exclusao():
    print("\nExclusão cancelada!\n")