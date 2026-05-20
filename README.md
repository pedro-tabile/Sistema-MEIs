<div align="center">

# 💼 Sistema para Gestão Financeira de MEIs

*Um sistema simples e eficiente para auxiliar Microempreendedores Individuais no controle de suas movimentações financeiras.*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Projeto%20Acadêmico-F2C811?style=for-the-badge)
![Fatec](https://img.shields.io/badge/Fatec-São%20Paulo-B20000?style=for-the-badge)

</div>

<br>

## 📖 Sobre o projeto

Muitos MEIs têm dificuldade para separar as finanças pessoais das finanças do negócio, acompanhar entradas e saídas e entender se estão tendo lucro ou prejuízo. Este sistema foi criado para apoiar esse controle de forma simples, usando uma interface via terminal e armazenamento local em arquivo JSON.

**O projeto busca facilitar:**
* O registro de movimentações financeiras.
* A separação entre valores pessoais e empresariais.
* A análise de entradas, saídas e saldo geral.
* O acompanhamento de limites de gastos.
* A visualização dos dados em tabelas e gráficos.

---

## ✨ Funcionalidades

- **Gestão de Registros:** Cadastro, edição e exclusão (por ID) de movimentações financeiras.
- **Classificação Inteligente:** Divisão por tipo (**Entrada** ou **Saída**) e nível (**Pessoal** ou **Empresarial**).
- **Detalhamento:** Inclusão de valor, descrição, data, categoria e cliente.
- **Busca Parametrizada:** Filtros por nível, categoria ou tipo.
- **Controle de Gastos:** Definição e exibição de limites financeiros para gastos pessoais e empresariais.
- **Visualização Clara:** Exibição dos registros em formato de tabela no terminal.
- **Geração de Gráficos:** Visualização interativa com valores por nível, tipo e categoria.
- **Análise Financeira Completa:** - Total movimentado, entradas e saídas.
  - Balanço geral (indicação de lucro, prejuízo ou equilíbrio).
  - Análise por categoria e comparação entre gastos e limites.

---

## 🛠️ Tecnologias utilizadas

* **Python:** Linguagem principal do projeto.
* **JSON:** Armazenamento local dos dados financeiros.
* **Tabulate:** Exibição dos registros em formato de tabela no terminal.
* **Plotly:** Geração de gráficos interativos.
* **Arquitetura MVC:** Separação estrutural entre modelos, visualizações e controladores.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/pedro-tabile/Sistema-MEIs.git


### 2. Crie um ambiente virtual

**No Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate

```

**No Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate

```

### 3. Instale as dependências

```bash
pip install -r requirements.txt

```

> **Dica:** Caso queira instalar apenas as bibliotecas principais manualmente, utilize: `pip install tabulate plotly`

### 4. Execute a aplicação

Navegue até a pasta `src` e execute o arquivo principal:

```bash
cd src
python main.py

```

> ⚠️ **Observação:** A execução dentro da pasta `src` é estritamente recomendada porque o sistema utiliza o arquivo `data/dados.json` por meio de caminho relativo.

---

## 📌 Menu principal

Ao iniciar o sistema, a seguinte interface de opções será apresentada:

| Opção | Ação correspondente |
| --- | --- |
| **0** | Sair do programa |
| **1** | Fazer novo registro |
| **2** | Visualizar registros |
| **3** | Editar registro |
| **4** | Excluir registro |
| **5** | Definir limite |
| **6** | Exibir limites atuais |
| **7** | Buscar gráficos |
| **8** | Busca parametrizada de registros |
| **9** | Análise geral de valores |

---

## 🗂️ Estrutura do projeto

```text
Sistema-MEIs-main/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── controllers/
    │   ├── acoes_controller.py
    │   ├── analises_valores_controller.py
    │   ├── fluxo_execucao_main.py
    │   ├── validadores_acoes.py
    │   └── validadores_campos_registro.py
    ├── data/
    │   └── dados.json
    ├── models/
    │   ├── adicionar_registro_model.py
    │   ├── analise_valores_model.py
    │   ├── buscar_dados_graficos_model.py
    │   ├── buscar_limites_model.py
    │   ├── buscar_registros_model.py
    │   ├── definir_limite_model.py
    │   ├── editar_registro_model.py
    │   ├── excluir_registro_model.py
    │   └── manipular_json.py
    ├── utils/
    │   ├── conversao_data.py
    │   └── formatacao_real.py
    └── views/
        ├── analise_valores_view.py
        ├── buscar_graficos_view.py
        ├── buscar_registros_view.py
        ├── definir_limite_view.py
        ├── editar_registro_view.py
        ├── excluir_registro_view.py
        ├── exibir_limites_view.py
        ├── mensagens_gerais.py
        ├── novo_registro_view.py
        └── opcoes_view.py

```

---

## 💾 Armazenamento dos dados

Os dados são armazenados localmente de forma leve no arquivo `src/data/dados.json`. Esse arquivo armazena a lista de registros financeiros e os limites definidos.

**Exemplo de registro interno:**

```json
{
  "Id": 1,
  "Tipo": "Entrada",
  "Valor": 1500.00,
  "Descrição": "Pagamento de serviço",
  "Data": "20/05/2026",
  "Nível": "Empresarial",
  "Categoria": "Serviços",
  "Cliente": "Cliente Exemplo"
}

```

Para iniciar o sistema do zero (sem dados de exemplo), o arquivo `dados.json` deve seguir a seguinte base:

```json
{
  "registros": [],
  "limites": {
    "Empresarial": 0,
    "Pessoal": 0
  }
}

```

---

## 🏛️ Arquitetura

O projeto foi organizado com base no robusto padrão **MVC (Model-View-Controller)**:

* **Models:** Responsáveis pela leitura, gravação, busca, edição, exclusão e análise dos dados.
* **Views:** Responsáveis pela interação direta com o usuário, exibição de menus, tabelas, mensagens e gráficos.
* **Controllers:** Responsáveis por controlar o fluxo do sistema, validar entradas e orquestrar as ações escolhidas pelo usuário.

Essa separação ajuda a deixar o código mais organizado, modular e infinitamente mais fácil de manter.

---

## 🎯 Objetivos acadêmicos

Este projeto tem como finalidade aplicar conceitos fundamentais estudados durante o curso, como:

* Lógica de programação e manipulação de arquivos.
* Estruturas de dados e validação de *inputs*.
* Modularização de código e organização em camadas (MVC).
* Análise de dados e visualização de informações financeiras.

---

## 🔮 Melhorias futuras

* [ ] Criar interface gráfica (GUI) ou versão web.
* [ ] Adicionar sistema de autenticação de usuário.
* [ ] Migrar para um banco de dados relacional (Ex: SQLite, PostgreSQL).
* [ ] Exportar relatórios gerenciais em PDF ou Excel.
* [ ] Criar *dashboard* financeiro em tela única.
* [ ] Adicionar filtros de busca avançados por período/data.
* [ ] Suporte multi-tenant (separar múltiplos MEIs ou empresas no mesmo sistema).
* [ ] Implementação de testes automatizados (Unitários e Integração).

---

## 👥 Integrantes

Projeto desenvolvido como requisito acadêmico para a **Fatec São Paulo**.

* Vinicius Kaolo Futema Sonoda
* Wesley Santos Souza
* Theo Figueiredo de Aquino
* Matheus Zelante Cavalcante
* Pedro Henrique Tabile Piovezani

---

## 📄 Licença

Este projeto foi desenvolvido estritamente para fins acadêmicos e está licenciado sob a licença **MIT**. Veja o arquivo `LICENSE` para mais detalhes.

```

```
