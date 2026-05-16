# Tupla com todas as opções de ações e suas respectivas correspondências
opcoes = (
    {
        "id": 0,
        "mensagem": "Sair do programa",
    },
    {
        "id": 1,
        "mensagem": "Fazer novo registro",
    },
    {
        "id": 2,
        "mensagem": "Visualizar registros",
    },
    {
        "id": 3,
        "mensagem": "Editar registro",
    },
    {
        "id": 4,
        "mensagem": "Excluir registro",
    },
    {
        "id": 5,
        "mensagem": "Definir limite",
    },
    {
        "id": 6,
        "mensagem": "Buscar gráficos",
    },
    {
        "id": 7,
        "mensagem": "Busca parametrizada de registros",
    },
)

# Exibição inicial das opções de ações (importadas)
def exibicao_opcoes():
    for item in opcoes:
        print(f'{item["id"]} - {item["mensagem"]}')

    print()

# Função usada pelo controller para solicitar ação
def escolher_opcao():
    opcao = int(input("Informe o número da ação que deseja realizar: "))
    print()
    
    return opcao