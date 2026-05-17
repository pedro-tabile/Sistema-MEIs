from .manipular_json import ler_dados

# Função responsável por realizar a somatória dos valores para entradas, saídas e categorias, além do total geral movimentado e das 
# porcentagens envolvidas
def somatorias():
    dados = ler_dados()

    if dados['sucesso'] is False:
        return dados
    
    somatoria_entradas, somatoria_saidas = 0, 0
    somatoria_saidas_pessoais, somatoria_saidas_empresariais = 0, 0
    categorias_movimentacoes = {
        "Entradas": {},
        "Saídas": {},
        "Total": {}
    }

    # Leva em consideração os tipos (entrada ou saída) e soma os totais, categorias e saídas por nível (empresarial ou pessoal)
    for item in dados['dados']['registros']:
        if item['Tipo'] == 'Entrada':
            somatoria_entradas += item['Valor']

            # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
            categorias_movimentacoes['Entradas'].setdefault(item['Categoria'], 0)
            categorias_movimentacoes['Entradas'][item['Categoria']] += item['Valor']
        else:
            somatoria_saidas += item['Valor']

            # Soma de saídas por nível
            if item['Nível'] == 'Empresarial':
                somatoria_saidas_empresariais += item['Valor']
            else:
                somatoria_saidas_pessoais += item['Valor']

            # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
            categorias_movimentacoes['Saídas'].setdefault(item['Categoria'], 0)
            categorias_movimentacoes['Saídas'][item['Categoria']] += item['Valor']
        
        # Caso a categoria não exista, é criada e recebe 0 como padrão para permitir o início da soma
        categorias_movimentacoes['Total'].setdefault(item['Categoria'], 0)
        categorias_movimentacoes['Total'][item['Categoria']] += item['Valor']

    # Definição de indicadores e porcentagens com relação ao total geral movimentado (ou por limites)
    balanco_geral = abs(somatoria_entradas - somatoria_saidas)
    total_geral = somatoria_entradas + somatoria_saidas

    porcentagem_entrada, porcentagem_saida, porcentagem_fluxo = 0, 0, 0
    balanco_limite_pessoal, balanco_limite_empresarial = 0, 0
    porcentagem_limite_pessoal, porcentagem_limite_empresarial = 0, 0
    # Verifica também se o total movimentado e os limites são diferentes de 0 para calcular divisões
    if dados['dados']['limites']['Pessoal'] > 0:
        balanco_limite_pessoal = dados['dados']['limites']['Pessoal'] - somatoria_saidas_pessoais
        porcentagem_limite_pessoal = somatoria_saidas_pessoais / dados['dados']['limites']['Pessoal'] * 100 

    if dados['dados']['limites']['Empresarial'] > 0:
        porcentagem_limite_empresarial = somatoria_saidas_empresariais / dados['dados']['limites']['Empresarial'] * 100
        balanco_limite_empresarial = dados['dados']['limites']['Empresarial'] - somatoria_saidas_empresariais

    if total_geral != 0:
        porcentagem_entrada = somatoria_entradas / total_geral * 100
        porcentagem_saida = somatoria_saidas / total_geral * 100
        porcentagem_fluxo = balanco_geral / total_geral * 100

    # Retorno de todos os valores envolvendo totais, limites e porcentagens
    return {
        "sucesso": True,
        "dados":{
            "totais": {
                "total_geral": total_geral,
                "total_entradas": somatoria_entradas,
                "total_saidas": somatoria_saidas,
                "total_saidas_pessoal": somatoria_saidas_pessoais,
                "total_saidas_empresarial": somatoria_saidas_empresariais,
                "balanco_geral": balanco_geral,
            },
            "limites": {
                **dados['dados']['limites'],
                "balanco_pessoal": balanco_limite_pessoal,
                "balanco_empresarial": balanco_limite_empresarial,
            },
            "valores_categoria": categorias_movimentacoes,
            "porcentagens": {
                "entradas": porcentagem_entrada,
                "saidas": porcentagem_saida,
                "fluxo": porcentagem_fluxo,
                "limite_pessoal": porcentagem_limite_pessoal,
                "limite_empresarial": porcentagem_limite_empresarial,
            }
        }
    }