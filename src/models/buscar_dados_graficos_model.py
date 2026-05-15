from .manipular_json import ler_dados

# Função que busca e soma valores com base nos paramêtros (níveis, tipos e categorias) e retorna os dicionários com as somas correspondentes
def buscar_valores_itens():
    dados_json = ler_dados()

    if dados_json["sucesso"] is False:
        return dados_json

    # Dicionário que armazena os níveis existentes para os valores e a soma dos valores registrados para cada nível
    valores_niveis = {"Empresarial": 0, "Pessoal": 0}

    # Dicionário que armazena os tipos existentes para os valores e a soma dos valores registrados para cada tipo
    valores_tipos = {"Entrada": 0, "Saída": 0}

    # Dicionário que armazena as categorias existentes para os valores e a soma dos valores registrados para cada categoria
    valores_categorias = {}

    for item in dados_json["dados"]["registros"]:
        valor = item["Valor"]

        # Para cada item, soma o valor ao atual da respectiva chave nos dicionários (nível e tipo) 
        valores_niveis[item["Nível"]] += valor
        valores_tipos[item["Tipo"]] += valor

        # Caso não exista como chave, adiciona a categoria no dicionário atribuindo 0 como valor padrão
        valores_categorias.setdefault(item["Categoria"], 0)
        # Depois, soma o valor do registro à categoria 
        valores_categorias[item["Categoria"]] += item["Valor"]

    return {
        "sucesso": True,
        "dados": {
            "valores_niveis": valores_niveis,
            "valores_categorias": valores_categorias,
            "valores_tipos": valores_tipos,
        },
    }
