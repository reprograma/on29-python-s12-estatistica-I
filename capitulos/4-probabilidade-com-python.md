## 4. Probabilidade com Python

- **4.1 Simulação de Eventos Aleatórios com Python**
    - **Biblioteca random:** A biblioteca random em Python fornece funções para gerar números aleatórios e simular eventos aleatórios.
    - **Exemplo:**
            
        ```python
            # Importa a biblioteca 'random' para gerar números aleatórios
            import random
            
            # Escolhe aleatoriamente entre 'Cara' e 'Coroa'
            resultado = random.choice(['Cara', 'Coroa'])
            print(resultado)
        ```
            
- **4.2 Cálculo de Probabilidade com Funções da Biblioteca NumPy**
    - **Exemplo:**
            
         ```python
            # Importa a biblioteca 'numpy' para trabalhar com arrays
            import numpy as np
            
            # # Cria um array com os números de 1 a 6
            numeros = np.arange(1, 7)
            
            # # Filtra o array para obter apenas os números pares
            numeros_pares = numeros[numeros % 2 == 0]
            
            # # Calcula a probabilidade dividindo a quantidade de números pares pela quantidade total de números
            probabilidade = len(numeros_pares) / len(numeros)
            print(probabilidade)  # Saída: 0.5
        ```
            
- **4.3 Criação de Gráficos de Probabilidade com Matplotlib**
    - **Exemplo:**
            
        ```python
            # Importa a biblioteca 'matplotlib.pyplot' para criar gráficos
            import matplotlib.pyplot as plt
            
            # # Cria um array com probabilidades iguais para cada face do dado
            probabilidades = np.ones(6) / 6
            
            # Cria um gráfico de barras com as probabilidades
            plt.bar(np.arange(1, 7), probabilidades)
            
            # Define o rótulo do eixo x
            plt.xlabel('Faces do Dado')
            
            # Define o rótulo do eixo y
            plt.ylabel('Probabilidade')
            
            # Define o título do gráfico
            plt.title('Distribuição de Probabilidade de um Dado')
            
            # Exibe o gráfico
            plt.show()
        ```
            

>
