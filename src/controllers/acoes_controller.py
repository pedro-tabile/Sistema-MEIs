from views.opcoes_view import opcoes, escolher_opcao
from views.mensagens_gerais import opcao_invalida, mensagem_erro, mensagem_sucesso
from views.novo_registro_view import infos_novo_registro
from views.buscar_registros_view import tabela_registros, sem_registros
from models.registrar_movimentacao_model import registrar_nova_movimentacao
from models.buscar_registros_model import buscar_registros
from .validadores_acoes import validacoes_novo_registro

# Função que garante que a opção escolhida seja uma das opções permitidas; quando for permitida, direciona às ações correspondentes
def direcionar_escolha():
    opcao = escolher_opcao()

    # Enquanto a opção estiver fora do intervalo das opções, solicita novamente a escolha
    while not 0 <= opcao <= len(opcoes) - 1:
        opcao_invalida()
        opcao = escolher_opcao()
    
    # Direciona ao model e ao view conforme escolha
    if opcao == 1:
        # Chama a função que retorna o dicionário com os dados informados pelo usuário
        dados_informados = infos_novo_registro()

        # Realiza tentativa de registrar movimentação a partir dos dados informados e de validações e indica sucesso ou erro
        resultado = registrar_nova_movimentacao(validacoes_novo_registro(dados_informados))
        if resultado['sucesso']:
            mensagem_sucesso(opcao)
        else:
            mensagem_erro(resultado['erro'])
    elif opcao == 2:
        # Busca todos os registros do arquivo
        resultado = buscar_registros()

        # Verifica se há algum registro e envia o resultado (dados) para o view de exibição; caso não haja, exibe mensagem de sem registros
        if resultado['sucesso']:
            if len(resultado['dados']['registros']) > 0:
                mensagem_sucesso(opcao)
                tabela_registros(resultado['dados']['registros'])
            else:
                sem_registros()
        else:
            mensagem_erro(resultado['erro'])

    return opcao