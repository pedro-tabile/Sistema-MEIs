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
        "mensagem": "Exibir limites atuais"
    },
    {
        "id": 7,
        "mensagem": "Buscar gráficos",
    },
    {
        "id": 8,
        "mensagem": "Busca parametrizada de registros",
    },
    {
        "id": 9,
        "mensagem": "Análise geral de valores",
    },
)

# Exibição inicial das opções de ações (importadas)
def exibicao_opcoes():
    print("-" * 135)
    print()
    
    for item in opcoes:
        print(f'{item["id"]} - {item["mensagem"]}')

    print()

# Função usada pelo controller para solicitar ação
def escolher_opcao():
    opcao = int(input("\033[93mInforme o número da ação que deseja realizar: \033[m"))
    print()
    
    return opcao