# Função responsável por constatar lucro ou prejuízo e retornar informações de balanço e porcentagem a partir do condicional
def analise_balanco_geral(dados_valores: dict):
    balanco = dados_valores['totais']['balanco_geral']

    if balanco > 0:
        return {
            "constatacao_balanco": "Lucro",
            "balanco": balanco,
            "porcentagem": dados_valores['porcentagens']['fluxo']
        }
    elif balanco < 0:
        return {
            "constatacao_balanco": "Prejuízo",
            "balanco": abs(balanco),
            "porcentagem": abs(dados_valores['porcentagens']['fluxo'])
        }
    else:
        return {
            "constatacao_balanco": "Equilíbrio",
        }


# Função responsável por comparar limites com valores de cada nível (pessoal e empresarial) e retornar o balanço e as informações de cada um
def analise_balanco_niveis(dados_valores: dict):
    balanco_pessoal = dados_valores['limites']['balanco_pessoal']
    balanco_empresarial = dados_valores['limites']['balanco_empresarial']

    # Inicia o dicionário para retorno
    retorno = {}

    # Verifica se os limites existem (ou seja, se já foram definidos pelo usuário) e, caso existam (ou pelo menos um), adiciona ao dicionário 
    # as informações do nível e o resultado do balanço (excedeu o limite, dentro do limite ou igual ao limite) a partir do condicional.
    if dados_valores['limites']['Pessoal'] > 0:
        retorno['Pessoal'] = {
            "total_gasto": dados_valores["totais"]["total_saidas_pessoal"],
            "limite": dados_valores["limites"]["Pessoal"],
            "balanco_limite": abs(dados_valores["limites"]["balanco_pessoal"]),
            "porcentagem": dados_valores["porcentagens"]["limite_pessoal"]
        }

        if balanco_pessoal < 0:
            retorno["Pessoal"]["constatacao_balanco"] = "Excedeu"
        elif balanco_pessoal > 0:
            retorno["Pessoal"]["constatacao_balanco"] = "Dentro"
        else:
            retorno["Pessoal"]["constatacao_balanco"] = "Equilíbrio"

    if dados_valores['limites']['Empresarial'] > 0:
        retorno["Empresarial"] =  {
            "total_gasto": dados_valores["totais"]["total_saidas_empresarial"],
            "limite": dados_valores["limites"]["Empresarial"],
            "balanco_limite": abs(dados_valores["limites"]["balanco_empresarial"]),
            "porcentagem": dados_valores["porcentagens"]["limite_empresarial"]
        }

        if balanco_empresarial < 0:
            retorno["Empresarial"]["constatacao_balanco"] = "Excedeu"
        elif balanco_empresarial > 0:
            retorno["Empresarial"]["constatacao_balanco"] = "Dentro"
        else:
            retorno["Empresarial"]["constatacao_balanco"] = "Equilíbrio"

    return retorno