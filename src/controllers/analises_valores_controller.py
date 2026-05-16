# Função responsável por definir lucro ou prejuízo e retornar informações
def analise_balanco(dados_valores: dict):
    balanco = dados_valores['balanco']

    if balanco > 0:
        return {
            "constatacao_balanco": "Lucro",
            "balanco": balanco,
            "porcentagem": dados_valores['porcentagens']['fluxo']
        }
    elif balanco < 0:
        return {
            "constatacao_balanco": "Prejuízo",
            "balanco": balanco,
            "porcentagem": dados_valores['porcentagens']['fluxo']
        }
    else:
        return {
            "constatacao_balanco": "Equilíbrio",
        }