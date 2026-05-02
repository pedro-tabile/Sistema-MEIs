from .manipular_json import gravar_dados, ler_dados

# Função que faz o novo registro: chama a função (ler_dados) que realiza leitura de dados e adiciona um id ao registro (dados) a ser gravado
# (gerar_id); após, adiciona os novos dados no fim da lista dos registros existentes e chama a função gravar_dados passando como parâmetro
# a lista atualizada (que agora contém todos os registros - incluindo o novo - e dados que estavam armazenados no antigo arquivo json)
def registrar_nova_movimentacao(dados_gravacao: dict[str, float, str, str, str, str, str]):
    #Chama a função que lê os dados do arquivo
    dados_json = ler_dados()

    if dados_json['sucesso'] is False:
        return dados_json

    # Gera id e salva para o novo registro
    id = gerar_id(dados_json['dados']['registros'])
    dados_gravacao['Id'] = id

    # Adiciona novo registro na lista dos registros
    dados_json['dados']['registros'].append(dados_gravacao)

    # Chama função para gravar os dados e retorna true ou false
    return gravar_dados(dados_json['dados'])
    
# Gera um id sequencial para o registro que será adicionado. Para isso, analisa o valor do último id criado e gera o próximo da 
# sequência (adiciona 1 ao último valor)
def gerar_id(dados_existentes: list):
    if len(dados_existentes) > 0:
        return dados_existentes[-1]['Id'] + 1
    else:
        return 1