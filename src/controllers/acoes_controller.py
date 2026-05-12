# Controller responsável pelo fluxo das ações do sistema
from views.opcoes_view import opcoes, escolher_opcao
from views.mensagens_gerais import opcao_invalida, mensagem_erro, mensagem_sucesso, registro_inexistente
from views.novo_registro_view import infos_novo_registro
from views.buscar_registros_view import tabela_registros, sem_registros
from views.excluir_registro_view import msg_id_exclusao, msg_confirmacao, msg_cancelar_exclusao
from views.editar_registro_view import msg_id_edicao, exibir_tabela, escolha_campo, msg_cancelar_edicao, novo_valor
from views.definir_limite_view import infos_limite, novo_input
from models.adicionar_registro_model import registrar_nova_movimentacao
from models.buscar_registros_model import buscar_registros
from models.filtrar_registros import buscar_filtro
from models.excluir_registro_model import exclusao_registro
from models.editar_registro_model import buscar_registro_edicao, editar_dados
from models.definir_limite_model import definir_limite
from .validadores_acoes import validacoes_novo_registro, validador_edicao_campo, validacoes_limite

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
    elif opcao == 3:
        editar_registro(opcao)
    elif opcao == 4:
        excluir_registro(opcao)
    elif opcao == 5:
        adicionar_limite(opcao)

    return opcao

# Função responsável por direcionar ao registro da nova movimentação
def adicionar_registro(opcao: int):
    # Função responsável por retornar o dicionário com os dados informados pelo usuário
    dados_informados = infos_novo_registro()

    # Realiza tentativa de registrar movimentação a partir dos dados informados e de validações e indica sucesso ou erro
    resultado = registrar_nova_movimentacao(validacoes_novo_registro(dados_informados))
    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if resultado['sucesso']:
        mensagem_sucesso(opcao)
    else:
        mensagem_erro(resultado['erro'])

# Função responsável por direcionar à exibição da lista dos registros
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

# Função responsável por direcionar à edição dos dados de um registro
def editar_registro(opcao: int):
    # Busca o id informado pelo usuário e, em seguida, compara com os dos registros do arquivo
    filtro_id = buscar_filtro('Id')

    if filtro_id['sucesso']:
        id_escolhido = msg_id_edicao()

        if id_escolhido in filtro_id['itens_encontrados']:
            # Retorna os dados do registro e exibe (tabela) ao usuário
            registro_encontrado = buscar_registro_edicao(id_escolhido)
            exibir_tabela(registro_encontrado, 'Início')

            # Solicita o novo campo a ser alterado
            campo_escolhido = escolha_campo(registro_encontrado)

                # Valida o campo e solicita o novo valor (também validado em seguida), enviando-o à função de edição
            if not isinstance(campo_escolhido, int):
                novo_valor_campo = novo_valor(campo_escolhido)
                novo_valor_atualizado = validador_edicao_campo(campo_escolhido, novo_valor_campo)
                resultado_edicao = editar_dados(registro_encontrado, campo_escolhido, novo_valor_atualizado)

                # "Else's" dos condicionais usados para tratamento de erros ou cancelamentos
                if resultado_edicao['sucesso']:
                    mensagem_sucesso(opcao)
                    # Exibe a tabela com o registro cotendo os dados atualizados a partir das alterações feitas na referência 
                    # ao dicionário (registro_encontrado) na função de edição (editar_dados)
                    exibir_tabela(registro_encontrado, 'Fim')
                else:
                    mensagem_erro(resultado_edicao['erro'])
            else:
                msg_cancelar_edicao()
        else:
            registro_inexistente()
    else:
        mensagem_erro(filtro_id['erro'])

# Função responsável por direcionar à exclusão de um registro
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

                # "Else's" dos condicionais usados para tratamento de erros ou cancelamentos
                else:
                    mensagem_erro(resultado['erro'])
            else:
                msg_cancelar_exclusao()
        else:
            registro_inexistente()
    else:
        mensagem_erro(filtro_id['erro'])

#Função responsável por direcionar o valor relacionado ao limite e seu tipo
def adicionar_limite(opcao: int):
    dados_limite = infos_limite()
    dados_limite = validacoes_limite(dados_limite)
    
    nivel = dados_limite["Nível"]
    valor = dados_limite["Valor"]

    definir_limite(nivel, valor)

    resultado = definir_limite(nivel, valor)

    if resultado["sucesso"] == True:
        mensagem_sucesso(opcao)
    else:
        mensagem_erro('erro')