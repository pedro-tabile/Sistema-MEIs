from .manipular_json import ler_dados

# Função responsável por realizar a somatória dos valores para entradas, saídas e categorias, além do total geral movimentado e das 
# porcentagens envolvidas
def somatorias():
    dados = ler_dados()

    if dados['sucesso'] is False:
        return dados
    
    somatoria_entradas, somatoria_saidas = 0, 0
    categorias_movimentacoes = {
        "Entradas": {},
        "Saídas": {},
        "Total": {}
    }

    # Soma o valor das categorias por tipo e total
    for item in dados['dados']['registros']:
        if item['Tipo'] == 'Entrada':
            somatoria_entradas += item['Valor']

            # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
            categorias_movimentacoes['Entradas'].setdefault(item['Categoria'], 0)
            categorias_movimentacoes['Entradas'][item['Categoria']] += item['Valor']
        else:
            somatoria_saidas += item['Valor']

            # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
            categorias_movimentacoes['Saídas'].setdefault(item['Categoria'], 0)
            categorias_movimentacoes['Saídas'][item['Categoria']] += item['Valor']
        
        # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
        categorias_movimentacoes['Total'].setdefault(item['Categoria'], 0)
        categorias_movimentacoes['Total'][item['Categoria']] += item['Valor']

    # Definição de indicadores e porcentagens com relação ao total movimentado
    balanco = abs(somatoria_entradas - somatoria_saidas)
    total_geral = somatoria_entradas + somatoria_saidas

    porcentagem_entrada = somatoria_entradas / total_geral * 100
    porcentagem_saida = somatoria_saidas / total_geral * 100
    porcentagem_fluxo = balanco / total_geral * 100

    # Retorno de todos os totais
    return {
        "sucesso": True,
        "dados":{
            "total_geral": total_geral,
            "total_entradas": somatoria_entradas,
            "total_saidas": somatoria_saidas,
            "balanco": balanco,
            "valores_categoria": categorias_movimentacoes,
            "porcentagens": {
                "entradas": porcentagem_entrada,
                "saidas": porcentagem_saida,
                "fluxo": porcentagem_fluxo
            }
        }
    }