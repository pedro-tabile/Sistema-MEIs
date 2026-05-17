# Este é o Controller responsável pelo fluxo das ações do sistema
from views.opcoes_view import opcoes, escolher_opcao
from views.mensagens_gerais import opcao_invalida, mensagem_erro, mensagem_sucesso, registro_inexistente, sem_registros
from views.novo_registro_view import infos_novo_registro
from views.buscar_registros_view import tabela_registros, parametros, retorno_parametro_escolhido
from views.excluir_registro_view import msg_id_exclusao, msg_confirmacao, msg_cancelar_exclusao
from views.editar_registro_view import msg_id_edicao, exibir_tabela, escolha_campo, msg_cancelar_edicao, novo_valor
from views.definir_limite_view import infos_limite
from views.buscar_graficos_view import exibir_graficos
from views.analise_valores_view import lucro_prejuizo, mensagem_movimentacoes, niveis_limites, sem_limite_definido

from models.adicionar_registro_model import registrar_nova_movimentacao
from models.buscar_registros_model import buscar_registros, buscar_registros_parametros
from models.filtrar_id_registros import buscar_filtro_id
from models.excluir_registro_model import exclusao_registro
from models.editar_registro_model import buscar_registro_edicao, editar_dados
from models.definir_limite_model import definir_limite
from models.analise_valores_model import somatorias
from models.buscar_dados_graficos_model import buscar_valores_itens

from .validadores_acoes import validacoes_novo_registro, validador_edicao_campo, validador_limite
from .analises_valores_controller import analise_balanco_geral, analise_balanco_niveis

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
    elif opcao == 6:
        buscar_graficos(opcao)
    elif opcao == 7:
        busca_parametrizada(opcao)
    elif opcao == 8:
        analise_valores()

    return opcao


# Função responsável por direcionar ao registro da nova movimentação
def adicionar_registro(opcao: int):
    # Função responsável por retornar o dicionário com os dados informados pelo usuário e o sucesso (True ou False)
    dados_informados = infos_novo_registro()

    # Realiza tentativa de registrar movimentação a partir dos dados informados e de validações e indica sucesso ou erro
    resultado = registrar_nova_movimentacao(validacoes_novo_registro(dados_informados))
    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if resultado['sucesso']:
        mensagem_sucesso(opcao)
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo 
        mensagem_erro(resultado['erro'])


# Função responsável por direcionar à exibição da lista dos registros
def visualizar_registros(opcao: int):
    # Busca todos os registros do arquivo - retorna um dicionário contendo os dados e o sucesso (True ou False)
    resultado = buscar_registros()

    # Verifica se há algum registro e envia o resultado (dados) para o view de exibição; caso não haja, exibe mensagem de sem registros
    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if resultado['sucesso']:
        if len(resultado['dados']['registros']) > 0:
            mensagem_sucesso(opcao)
            tabela_registros(resultado['dados']['registros'])
        else:
            # Mensagem de inexistência registros
            sem_registros()
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo 
        mensagem_erro(resultado['erro'])


# Função responsável por direcionar à edição dos dados de um registro
def editar_registro(opcao: int):
    # Busca o id informado pelo usuário e, em seguida, compara com os dos registros do arquivo
    filtro_id = buscar_filtro_id('Id')

    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if filtro_id['sucesso']:
        id_escolhido = msg_id_edicao()

        # Verifica se o Id existe; se não existir, mensagem de inexistência é exibida
        if id_escolhido in filtro_id['itens_encontrados']:
            # Retorna os dados do registro e exibe (tabela) ao usuário
            registro_encontrado = buscar_registro_edicao(id_escolhido)
            exibir_tabela(registro_encontrado, 'Início')

            # Solicita o novo campo a ser alterado
            campo_escolhido = escolha_campo(registro_encontrado)

            # Valida o campo e solicita o novo valor (também validado em seguida), enviando-o à função de edição; caso o valor informado para 
            # um campo não corresponda a nenhum, a edição e cancelada 
            if not isinstance(campo_escolhido, int):
                novo_valor_campo = novo_valor(campo_escolhido)
                novo_valor_atualizado = validador_edicao_campo(campo_escolhido, novo_valor_campo)
                # editar_dados retorna um dicionário contendo os dados e o sucesso (True ou False)
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
                # Cancelamento de edição (mensagem)
                msg_cancelar_edicao()
        else:
            # Mensagem de inexistência de Id
            registro_inexistente()
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(filtro_id['erro'])


# Função responsável por direcionar à exclusão de um registro
def excluir_registro(opcao: int):
    # Filtra Ids existentes
    filtro_id = buscar_filtro_id('Id')

    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if filtro_id['sucesso']:
        id_escolhido = msg_id_exclusao()
        
        # Realiza a correspondência entre o id informado pelo usuário e os ids existentes, realizando a exclusão em caso de confirmação 
        # e cancelando operação caso o id não seja encontrado
        if id_escolhido in filtro_id['itens_encontrados']:
            confirmacao = msg_confirmacao()

            if confirmacao.upper() == "T":
                # exclusao_registro retorna um dicionário contendo os dados e o sucesso (True ou False)
                resultado = exclusao_registro(id_escolhido)

                if resultado['sucesso']:
                    mensagem_sucesso(opcao)

                # "Else's" dos condicionais usados para tratamento de erros ou cancelamentos
                else:
                    mensagem_erro(resultado['erro'])
            else:
                # Cancelamento de exclusão (mensagem)
                msg_cancelar_exclusao()
        else:
            # Mensagem de inexistência de Id
            registro_inexistente()
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(filtro_id['erro'])


#Função responsável por direcionar o valor relacionado ao limite e seu nível
def adicionar_limite(opcao: int):
    dados_limite = infos_limite()
    dados_limite = validador_limite(dados_limite)
    
    nivel = dados_limite["Nível"]
    valor = dados_limite["Valor"]

    resultado = definir_limite(nivel, valor)

    if resultado["sucesso"]:
        mensagem_sucesso(opcao)
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(resultado['erro'])


# Função responsável por direcionar a exibição dos gráficos: pega os valores identificados e os envia à view de exibição dos gráficos 
def buscar_graficos(opcao: int):
    # Inicialmente, verirfica se tem algum registro (Id) para prosseguir; caso não haja, retorna mensagem de inexistência
    filtro_id = buscar_filtro_id('Id')

    if filtro_id['quantidade'] == 0:
        sem_registros()
        return

    # Chama a função que retorna um dicionário com todos os valores por níveis, tipos e categorias; caso a busca ocorra normalmente, os 
    # gráficos são exibidos; caso contrário, uma mensagem de erro é exibida.
    valores_itens = buscar_valores_itens()

    if valores_itens['sucesso']:
        # Exibe os gráficos e a mensagem de sucesso
        exibir_graficos(valores_itens['dados'])

        mensagem_sucesso(opcao)
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(valores_itens['erro'])


# Função responsável por controlar a busca parametrizada de registros
def busca_parametrizada(opcao: int):
    # Resgata o parâmetro escolhido pelo usuário e valida se a opção é inválida
    parametro = parametros()
    if parametro is False:
        opcao_invalida()
        return
    
    # Resgata o filtro de pesquisa escolhido pelo usuário e valida se é inválido
    filtro_pesquisa = retorno_parametro_escolhido(parametro['id'])
    if filtro_pesquisa is None:
        opcao_invalida()
        return

    # Chama a função que retorna os registros correspondentes à busca do usuário
    resultado_dados = buscar_registros_parametros(filtro_pesquisa, parametro['param'])

    # Condicional padrão do resultado da operação: mensagem de sucesso caso a ação ocorra normalmente; caso contrário, resposta de erro
    if resultado_dados['sucesso']:
        # Faz a validação da correspondência de registros e exibe-os na tabela caso existam
        if len(resultado_dados['dados']) > 0:
            mensagem_sucesso(opcao)
            tabela_registros(resultado_dados['dados'])
        else:
            # Mensagem de inexistência registros
            sem_registros()
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(resultado_dados['erro'])


# Função responsável pelas ações de análise de valores movimentados
def analise_valores():
    # Variável que armazena um dict com todos os cálculos envolvidos nas análises
    dados_calculos = somatorias()

    if dados_calculos['sucesso']:
        # Exibição das mensagens de total movimentado geral e total movimentado em entradas e saídas, junto às porcentagens
        mensagem_movimentacoes(dados_calculos['dados'])
        
        # Trecho que chama função de análise de balanço geral (definição de lucro, prejuízo ou equilíbrio) e envia à view (lucro_prejuizo) valor, 
        # balanço e porcentagem
        resultado_balanco_geral = analise_balanco_geral(dados_calculos['dados'])
        lucro_prejuizo(resultado_balanco_geral)

        # Trecho que chama função de análise de balanço por níveis e limites, enviando à view valores de balanço, limites e porcentagem dos níveis.
        resultado_balanco_niveis = analise_balanco_niveis(dados_calculos['dados'])
        niveis_limites(resultado_balanco_niveis)
        # Caso algum limite não esteja definido (sem correspondência no dicionário retornado na análise), chama-se uma view (sem_limite_definido) 
        # que informa a impossibilidade de análise
        if resultado_balanco_niveis.get('Pessoal') is None:
            sem_limite_definido('Pessoal')
        if resultado_balanco_niveis.get('Empresarial') is None:
            sem_limite_definido('Empresarial')

        #valores_categorias(dados_calculos['dados']['valores_categoria'])
    else:
        # Mensagem para possível erro de leitura ou gravação de dados no arquivo
        mensagem_erro(dados_calculos['erro'])