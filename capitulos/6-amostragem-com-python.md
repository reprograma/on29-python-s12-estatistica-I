## 6. Amostragem com Python:**

- **6.1 Implementação de Métodos de Amostragem com Pandas e NumPy**
                
    - **Exemplo:**
        
        ```python
            # Importa a biblioteca NumPy para trabalhar com arrays
            import numpy as np
            # Importa a biblioteca Pandas para trabalhar com DataFrames
            import pandas as pd

            # # Cria um array com números de 1 a 100
            populacao = np.arange(1, 101)

            # Seleciona 10 elementos aleatórios da população sem repetição
            amostra_aleatoria_simples = list(np.random.choice(populacao, size=10, replace=False)) 

            # Preenche o restante da lista com 'None'
            amostra_aleatoria_simples.extend([None] * (len(populacao) - len(amostra_aleatoria_simples)))
        
            # Amostragem estratificada (dividindo em dois estratos: 1-50 e 51-100)

            # Cria um estrato com os elementos de 1 a 50
            estrato1 = populacao[0:50]

            # Cria um estrato com os elementos de 51 a 100
            estrato2 = populacao[50:100]

            # Seleciona 5 elementos aleatórios de cada estrato sem repetição
            amostra_estratificada = list(np.concatenate((np.random.choice(estrato1, size=5, replace=False),
                                                np.random.choice(estrato2, size=5, replace=False))))
            
            # # Preenche o restante da lista com 'None'
            amostra_estratificada.extend([None] * (len(populacao) - len(amostra_estratificada)))

            # Amostragem sistemática (selecionando cada 5º elemento)

            # Seleciona cada 5º elemento da população
            amostra_sistematica = list(populacao[::5])

            # Preenche o restante da lista com 'None'
            amostra_sistematica.extend([None] * (len(populacao) - len(amostra_sistematica))) 
        
            # # Cria um DataFrame com as colunas 'População', 'Amostra Aleatória Simples', 'Amostra Estratificada' e 'Amostra Sistemática'
            df = pd.DataFrame({'População': populacao,
                            'Amostra Aleatória Simples': amostra_aleatoria_simples,
                            'Amostra Estratificada': amostra_estratificada,
                            'Amostra Sistemática': amostra_sistematica})
            print(df)
        ```

- **6.2 Cálculo de Estatísticas Descritivas e Intervalos de Confiança**

    - **Exemplo:**
            
        ```python
            # Importa a biblioteca NumPy para trabalhar com arrays
            import numpy as np
            # Importa a biblioteca SciPy Stats para cálculos estatísticos
            import scipy.stats as stats
            
            # Dados da população (simulando uma população de 100 elementos)

            # Cria um array com números de 1 a 100
            populacao = np.arange(1, 101)
            
            # Amostragem aleatória simples (selecionando 10 elementos aleatórios)

            # Seleciona 10 elementos aleatórios da população sem repetição
            amostra_aleatoria_simples = np.random.choice(populacao, size=10, replace=False)
            
            # Calculando a média e o desvio padrão da amostra

            # Calcula a média da amostra
            media_amostra = np.mean(amostra_aleatoria_simples)

            # Calcula o desvio padrão da amostra
            desvio_padrao_amostra = np.std(amostra_aleatoria_simples)
            
            # Calculando o intervalo de confiança de 95% para a média populacional

            # Calcula o intervalo de confiança usando a distribuição t de Student
            intervalo_confianca = stats.t.interval(confidence=0.95,
            df=len(amostra_aleatoria_simples)-1,
            loc=media_amostra, scale=desvio_padrao_amostra / np.sqrt(len(amostra_aleatoria_simples)))
            print(f"Intervalo de Confiança de 95%: {intervalo_confianca}")
        ```
            
- **6.3 Visualização de Dados com Matplotlib**
    - **Exemplo:**
            
        ```python
            # Importa a biblioteca Matplotlib para criar gráficos
            import matplotlib.pyplot as plt
            
            # Cria o histograma com 10 bins e bordas pretas
            plt.hist(amostra_aleatoria_simples, bins=10, edgecolor='black')
            
            # Define o rótulo do eixo x
            plt.xlabel('Valores da Amostra')
            
            # Define o rótulo do eixo y
            plt.ylabel('Frequência')

            # Define o título do gráfico
            plt.title('Histograma da Amostra Aleatória Simples')

            # Exibe o histograma
            plt.show()
        ```
            
>

