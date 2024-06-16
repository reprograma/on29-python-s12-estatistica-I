# DESAFIO DA SEMANA
# Objetivo: Realizar uma análise estatística descritiva e criar um histograma para visualizar a distribuição dos valores das vendas.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dados_vendas = [

    {"Data da venda": "2023-01-01", "Valor da venda": 100.00, "Produto vendido": "Produto A",
        "Quantidade vendida": 2, "Método de pagamento": "Cartão", "Região de venda": "Centro"},

    {"Data da venda": "2023-01-02", "Valor da venda": 50.00, "Produto vendido": "Produto B",
        "Quantidade vendida": 1, "Método de pagamento": "Dinheiro", "Região de venda": "Sul"},

    {"Data da venda": "2023-01-03", "Valor da venda": 120.00, "Produto vendido": "Produto C",
        "Quantidade vendida": 3, "Método de pagamento": "Cartão", "Região de venda": "Norte"},

    {"Data da venda": "2023-01-04", "Valor da venda": 80.00, "Produto vendido": "Produto A",
        "Quantidade vendida": 2, "Método de pagamento": "PIX", "Região de venda": "Leste"},

    {"Data da venda": "2023-01-05", "Valor da venda": 150.00, "Produto vendido": "Produto B",
        "Quantidade vendida": 2, "Método de pagamento": "Cartão", "Região de venda": "Oeste"},

    {"Data da venda": "2023-01-06", "Valor da venda": 70.00, "Produto vendido": "Produto C",
        "Quantidade vendida": 1, "Método de pagamento": "Dinheiro", "Região de venda": "Centro"},

    {"Data da venda": "2023-01-07", "Valor da venda": 90.00, "Produto vendido": "Produto A",
        "Quantidade vendida": 2, "Método de pagamento": "PIX", "Região de venda": "Sul"},

    {"Data da venda": "2023-01-08", "Valor da venda": 110.00, "Produto vendido": "Produto B",
        "Quantidade vendida": 3, "Método de pagamento": "Cartão", "Região de venda": "Norte"},

    {"Data da venda": "2023-01-09", "Valor da venda": 130.00, "Produto vendido": "Produto C",
        "Quantidade vendida": 2, "Método de pagamento": "Dinheiro", "Região de venda": "Leste"},

    {"Data da venda": "2023-01-10", "Valor da venda": 100.00, "Produto vendido": "Produto A", "Quantidade vendida": 1, "Método de pagamento": "Cartão", "Região de venda": "Oeste"}]

df = pd.DataFrame(dados_vendas)
print(df)


def analise_descritiva(df):
    media_venda = df['Valor da venda'].mean()
    mediana_venda = df['Valor da venda'].median()
    minimo_venda = df['Valor da venda'].min()
    maximo_venda = df['Valor da venda'].max()
    desvio_venda = df['Valor da venda'].std()
    return media_venda, mediana_venda, minimo_venda, maximo_venda, desvio_venda


def grafico_regiao(df):
    analise_regiao = df.groupby('Região de venda')['Valor da venda'].sum()
    plt.bar(analise_regiao.index, analise_regiao.values)
    plt.xlabel('Região da venda')
    plt.ylabel('R$ venda')
    plt.title('Valor da venda por Região')
    plt.legend(['Valores de venda'], loc='upper left')
    for i, valor in enumerate(analise_regiao.values):
        plt.text(i, valor, f'{valor:.2f}', ha='center', va='bottom')
    plt.show()


def grafico_venda(df):
    analise_venda = df.groupby(['Produto vendido', 'Método de pagamento'])[
        'Valor da venda'].sum().unstack(fill_value=0)
    bar_width = 0.35
    num_bars = len(analise_venda.index)
    indices = np.arange(num_bars)
    cores = ['red', 'green', 'violet']
    for i, metodo in enumerate(analise_venda.columns):
        plt.bar(indices + i * bar_width,
                analise_venda[metodo], bar_width, color=cores[i], label=metodo)

    plt.xlabel('Produto vendido')
    plt.ylabel('R$ venda')
    plt.title('Valor da venda por Produto e Método de pagamento')
    plt.xticks(indices + bar_width/2, analise_venda.index)
    plt.legend(title='Método de pagamento',
               loc='upper right', bbox_to_anchor=(1.15, 1.02))
    for i, metodo in enumerate(analise_venda.columns):
        for j, valor in enumerate(analise_venda[metodo]):
            plt.text(indices[j]+i*bar_width, valor,
                     f'{valor:.2f}', ha='center', va='bottom')

    plt.tight_layout()
    plt.show()


while True:
    print("Escolha a o calculo para análise:")
    print("1. Média valor de vendas")
    print("2. Mediana valor de vendas")
    print("3. Mínimo valor de vendas")
    print("4. Máximo valor de vendas")
    print("5. Desvio padrão dos valores das vendas")
    print("0. Para sair do programa")

    opt = input('Digite a opão desejada: ')

    if opt == '1':
        resultado = analise_descritiva(df)
        media_venda = resultado[0]
        print(f'A média do valor das vendas é: {media_venda}')
    elif opt == '2':
        resultado = analise_descritiva(df)
        mediana_venda = resultado[1]
        print(f'A mediana do valor das vendas é: {mediana_venda}')
    elif opt == '3':
        resultado = analise_descritiva(df)
        minimo_venda = resultado[2]
        print(f'O mínimo do valor das vendas é: {minimo_venda}')
    elif opt == '4':
        resultado = analise_descritiva(df)
        maximo_venda = resultado[3]
        print(f'O máximo do valor das vendas é: {maximo_venda}')
    elif opt == '5':
        resultado = analise_descritiva(df)
        desvio_venda = resultado[4]
        print(f'O desvio padrão do valor das vendas é: {desvio_venda}')
    elif opt == '6':
        grafico_regiao(df)
    elif opt == '7':
        grafico_venda(df)
    elif opt == '0':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Escolha uma opção válida')
