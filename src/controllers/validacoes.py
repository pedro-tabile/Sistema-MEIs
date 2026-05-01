from views.opcoes_acoes import opcoes
from views.interface_inicial import escolher_opcao
from views.novo_registro import infos_novo_registro

# Função que garante que a opção escolhida seja uma das opções permitidas; quando for permitida, direciona ao tratamento de ações
def validacao_escolha():
    opcao = escolher_opcao()

    #Enquanto a opção estiver fora do intervalo das opções, solicita novamente a escolha
    while not 0 < opcao <= len(opcoes):
        print('Opção inválida!')
        opcao = escolher_opcao()
    
    #Direciona ao view conforme escolha
    if opcao == 1:
        validacoes_novo_registro()

# Função de validação: garante que todos os campos sejam preenchidos corretamente
def validacoes_novo_registro():
    dados = infos_novo_registro()
    
    #Validação de tipo
    if dados['tipo'] == 'E':
        dados['tipo'] = 'Entrada'
    elif dados['tipo'] == 'S':
        dados['tipo'] = 'Saída'
    else:
        dados['tipo'] = input("\nInsira um tipo válido (E ou S): ")
    
    #Validação de nível
    if dados['tipo'] == 'E':
        dados['tipo'] = 'Empresarial'
    elif dados['tipo'] == 'P':
        dados['tipo'] = 'Pessoal'
    else:
        dados['tipo'] = input("\nInsira um tipo válido (E ou P): ")