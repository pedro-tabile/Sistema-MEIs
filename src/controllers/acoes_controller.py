# Controller responsável pelo fluxo das ações do sistema
from views.opcoes_view import opcoes, escolher_opcao
from views.mensagens_gerais import opcao_invalida, mensagem_erro, mensagem_sucesso
from views.novo_registro_view import infos_novo_registro
from views.buscar_registros_view import tabela_registros, sem_registros
from views.excluir_registro_view import msg_id_exclusao, msg_confirmacao, registro_inexistente, msg_cancelamento
from models.registrar_movimentacao_model import registrar_nova_movimentacao
from models.buscar_registros_model import buscar_registros
from models.filtrar_registros import buscar_filtro
from models.excluir_registro_model import exclusao_registro
from .validadores_acoes import validacoes_novo_registro

# Função que garante que a opção escolhida seja uma das opções permitidas; quando for permitida, direciona às ações correspondentes
def direcionar_escolha():
    opcao = escolher_opcao()

    # Enquanto a opção estiver fora do intervalo das opções, solicita novamente a escolha
    while not 0 <= opcao <= len(opcoes) - 1:
        opcao_invalida()
        opcao = escolher_opcao()
    
    # Direciona à função correspondente conforme escolha
    if opcao == 1:
        adicionar_registro(opcao)
    elif opcao == 2:
        visualizar_registros(opcao)
    elif opcao == 4:
        excluir_registro(opcao)

    return opcao

# Função responsável por direcionar o registro da nova movimentação
def adicionar_registro(opcao: int):
    # Função responsável por retornar o dicionário com os dados informados pelo usuário
    dados_informados = infos_novo_registro()

    # Realiza tentativa de registrar movimentação a partir dos dados informados e de validações e indica sucesso ou erro
    resultado = registrar_nova_movimentacao(validacoes_novo_registro(dados_informados))
    if resultado['sucesso']:
        mensagem_sucesso(opcao)
    else:
        mensagem_erro(resultado['erro'])

# Função responsável por direcionar a exibição da lista dos registros
def visualizar_registros(opcao: int):
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

# Função responsável por direcionar a exclusão de um registro
def excluir_registro(opcao: int):
    # Filtra Ids existentes
    filtro_id = buscar_filtro('Id')

    if filtro_id['sucesso']:
        id_escolhido = msg_id_exclusao()
        
        # Realiza a correspondência entre o id informado pelo usuário e os ids existentes, realizando a exclusão em caso de confirmação
        if id_escolhido in filtro_id['itens_encontrados']:
            confirmacao = msg_confirmacao()

            if confirmacao.upper() == "T":
                resultado = exclusao_registro(id_escolhido)

                if resultado['sucesso']:
                    mensagem_sucesso(opcao)
                else:
                    mensagem_erro(resultado['erro'])
            else:
                msg_cancelamento()
        else:
            registro_inexistente()
    else:
        mensagem_erro(filtro_id['erro'])