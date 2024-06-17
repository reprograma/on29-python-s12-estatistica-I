# Exercício de Casa 🏠 

## Desafio da Semana

**Objetivo:** Realizar uma análise estatística descritiva e criar um histograma para visualizar a distribuição dos valores das vendas.

**Descrição do Desafio:** Você trabalha em uma empresa de varejo e recebeu uma lista de vendas fictícias de diferentes produtos ao longo de vários meses. Seu objetivo é realizar uma análise estatística descritiva dos valores das vendas e criar um histograma para visualizar a distribuição desses valores.

**Conjunto de Dados:** Os dados estão disponíveis em formato de lista de dicionários em Python e contêm as seguintes informações para cada venda:

Data da venda Valor da venda Perguntas para Responder:

Calcular a média, mediana, mínimo, máximo e desvio padrão dos valores das vendas. Criar um histograma para visualizar a distribuição dos valores das vendas. Entrega do Desafio:

Utilize a linguagem de programação Python para realizar a análise dos dados e criar o histograma. Prepare um relatório ou apresentação com suas descobertas e o histograma gerado. Envie seu código fonte, o relatório e a imagem do histograma para avaliação até o final da semana.

os dados:

```jsx
dados_vendas = [
    {"Data da venda": "2023-01-01", "Valor da venda": 100.00, "Produto vendido": "Produto A", "Quantidade vendida": 2, "Método de pagamento": "Cartão", "Região de venda": "Centro"},
    {"Data da venda": "2023-01-02", "Valor da venda": 50.00, "Produto vendido": "Produto B", "Quantidade vendida": 1, "Método de pagamento": "Dinheiro", "Região de venda": "Sul"},
    {"Data da venda": "2023-01-03", "Valor da venda": 120.00, "Produto vendido": "Produto C", "Quantidade vendida": 3, "Método de pagamento": "Cartão", "Região de venda": "Norte"},
    {"Data da venda": "2023-01-04", "Valor da venda": 80.00, "Produto vendido": "Produto A", "Quantidade vendida": 2, "Método de pagamento": "PIX", "Região de venda": "Leste"},
    {"Data da venda": "2023-01-05", "Valor da venda": 150.00, "Produto vendido": "Produto B", "Quantidade vendida": 2, "Método de pagamento": "Cartão", "Região de venda": "Oeste"},
    {"Data da venda": "2023-01-06", "Valor da venda": 70.00, "Produto vendido": "Produto C", "Quantidade vendida": 1, "Método de pagamento": "Dinheiro", "Região de venda": "Centro"},
    {"Data da venda": "2023-01-07", "Valor da venda": 90.00, "Produto vendido": "Produto A", "Quantidade vendida": 2, "Método de pagamento": "PIX", "Região de venda": "Sul"},
    {"Data da venda": "2023-01-08", "Valor da venda": 110.00, "Produto vendido": "Produto B", "Quantidade vendida": 3, "Método de pagamento": "Cartão", "Região de venda": "Norte"},
    {"Data da venda": "2023-01-09", "Valor da venda": 130.00, "Produto vendido": "Produto C", "Quantidade vendida": 2, "Método de pagamento": "Dinheiro", "Região de venda": "Leste"},
    {"Data da venda": "2023-01-10", "Valor da venda": 100.00, "Produto vendido": "Produto A", "Quantidade vendida": 1, "Método de pagamento": "Cartão", "Região de venda": "Oeste"}
]
```

Dica: Utilize as bibliotecas Pandas, NumPy e Matplotlib para manipulação e visualização de dados. Você pode calcular as métricas estatísticas utilizando funções dessas bibliotecas e criar o histograma utilizando o Matplotlib.
