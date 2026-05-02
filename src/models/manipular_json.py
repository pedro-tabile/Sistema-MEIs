import json

# Grava os dados no arquivo dados.json da pasta data com tratamento de erros e retorna true ou false para exibição de mensagem. A função 
# recebe todo o antigo arquivo json com os novos dados, uma vez que o parâmetro "w" indica que o arquivo será sobrescrito
def gravar_dados(dados: dict):
    try:
        with open('data/dados.json', 'w', encoding='UTF-8') as file:
            json.dump(dados, file, indent=4)
            return {"sucesso": True}
    except Exception as erro:
        return {"sucesso": False, "erro": str(erro)}

# Lê os dados existentes no arquivo dados.json da pasta data e os retorna. O parâmetro "r" indica leitura (read)
def ler_dados():
    try:
        with open('data/dados.json', 'r', encoding='UTF-8') as file:
            return {"sucesso": True, "dados": json.load(file)}
    except Exception as erro:
        return {"sucesso": False, "erro": str(erro)}