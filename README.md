# API Integration Test

Este repositório contém um teste de integração para validar a coleta de dados de uma API conectada ao banco de dados do **Centro Paula Souza** e sua exibição correta na aplicação.

## 📂 Estrutura do Repositório

```
├── test_api_integration.py   # Script de automação do teste usando Python
├── testeAPI.md               # Descrição do procedimento e resultados do teste
└── README.md                 # Descrição geral do projeto
```

---

## 🚀 Objetivo

Garantir que a integração entre a API e o repositório do projeto funcione corretamente, trazendo dados diretamente do banco e exibindo-os na página HTML conforme as rotas configuradas.

---

## 🧪 Como rodar o teste automatizado

1. **Pré-requisitos:**
   - Python 3.x instalado
   - Biblioteca `requests` instalada:
     ```bash
     pip install requests
     ```

2. **Configuração:**
   - Edite o arquivo `test_api_integration.py` e ajuste:
     - `BASE_URL`: URL do backend.
     - `ROUTE`: Rota específica a ser testada.
     - `TOKEN`: Token Bearer para autenticação.

3. **Execução:**

   No terminal, rode:

   ```bash
   python test_api_integration.py
   ```

   O teste irá:
   - Realizar a requisição para a API.
   - Validar se os dados retornados são corretos.
   - Confirmar a integração e exibição dos dados.

---

## 📄 Documentação detalhada

Para mais informações sobre o teste manual, pré-condições, resultados esperados e pós-condições, consulte o arquivo:

📄 **[testeAPI.md](./testeAPI.md)**
