## 2. Python para Estatística

Instalação e configuração do ambiente Python (incluindo bibliotecas NumPy, Pandas, Matplotlib e Seaborn).

- **2.1 Instalação e Configuração do Ambiente Python**

    - **Instalar Python:** Baixe o Python 3.x da página oficial ([**https://www.python.org/downloads/**](https://www.python.org/downloads/)) e siga as instruções de instalação para o seu sistema operacional.
    - **Instalar Bibliotecas Essenciais:**
        - **NumPy:** pip install numpy
        - **Pandas:** pip install pandas
        - **Matplotlib:** pip install matplotlib
        - **Seaborn:** pip install seaborn
        
        > **💡Observação:** Você pode instalar todas as bibliotecas de uma vez usando: pip install numpy pandas matplotlib seaborn

    - **Verificar a Instalação:** Abra o interpretador Python (terminal/prompt de comando e digite python) e importe as bibliotecas. Se não houver erros, a instalação está correta.

- **2.2 Bibliotecas Essenciais**

    NumPy e Pandas são bibliotecas Python que se tornaram fundamentais para qualquer cientista de dados, analista ou programador que trabalha com dados.

    - **2.2.1 NumPy**

        - **Arrays multidimensionais:** NumPy fornece a estrutura de dados "ndarray" (array N-dimensional), que é a base para cálculos numéricos eficientes e poderosos em Python.

        - **Operações matemáticas:** NumPy oferece uma vasta gama de funções para operações matemáticas com arrays, como soma, subtração, multiplicação, divisão, exponenciação, funções trigonométricas, álgebra linear e muito mais.

        - **Eficiência:** NumPy é otimizado para trabalhar com arrays em C e Fortran, tornando-o significativamente mais rápido que operações com listas nativas do Python, especialmente para conjuntos de dados grandes.


    - **2.2.1 Pandas**

        - **DataFrames:** Pandas introduz a estrutura de dados "DataFrame", que é como uma planilha tabular, permitindo manipular e analisar dados estruturados de forma eficiente.
        - **Manipulação de dados:** Pandas oferece ferramentas poderosas para filtrar, ordenar, agrupar, juntar e transformar dados em DataFrames.
        - **Análise:** Pandas fornece funções para cálculos estatísticos, como média, mediana, desvio padrão, e para criação de gráficos simples.

<br>

- **2.3 Demonstração Prática de Manipulação de Dados com NumPy e Pandas**
    
    - **NumPy:**

        ```python
        import numpy as np # Importa a biblioteca NumPy
        from scipy import stats as sts  # Importa a biblioteca SciPy Stats para a função 'mode'
        ```
        - **Criando arrays:**
            ```python
                            arr = np.array([1, 2, 3, 4, 5])
            ```
            - **Explicação:** Essa linha cria um array NumPy chamado arr com os valores 1, 2, 3, 4 e 5. Arrays NumPy são estruturas de dados unidimensionais (vetores) ou multidimensionais (matrizes) que armazenam dados numéricos de forma eficiente.
            
            - **Exemplo:**
                        
                ```python
                        import numpy as np
                        
                        # Criando um array NumPy
                        arr = np.array([1, 2, 3, 4, 5])
                        print(arr)  # Saída: [1 2 3 4 5]
                ```
                        
        - **Calculando a média:**

            ```python
                            media = np.mean(arr)
            ```

            
            - **Exemplo:**
                        
                ```python
                        # Calcula a média dos valores do array
                        media = np.mean(arr)
                        print(media)  # Saída: 3.0
                ```
        - **Calculando a mediana:**

            ```python
                            mediana = np.median(arr)
            ```
            
            - **Exemplo:**
                        
            ```python
                    # Calcula a mediana dos valores do array
                    mediana = np.median(arr)
                    print(f"Mediana: {mediana}")  # Saída: Mediana: 3.0
            ```

        - **Calculando a moda:**

            ```python
                            moda = sts.mode(arr).mode[0]
            ```
            
            - **Exemplo:**
                        
            ```python
                    # Calcula a moda usando a biblioteca SciPy Stats
                    moda = sts.mode(arr).mode[0]
                    print(f"Moda: {moda}")  # Saída: Moda: 1
            ```

        - **Calculando a variância:**

            ```python
                            variancia = np.var(arr)
            ```
            
            - **Exemplo:**
                        
            ```python
                    # Calcula a variância do array
                    variancia = np.var(arr)
                    print(f"Variância: {variancia}")  # Saída: Variância: 2.0
            ```
                         
        - **Calculando o desvio padrão:** 
        
            ```python
                            desvio_padrao = np.std(arr)
            ``` 
            
            - **Exemplo:**
                        
            ```python
                    # Calcula o desvio padrão do array
                    desvio_padrao = np.std(arr)
                    print(f"Desvio Padrão: {desvio_padrao}")  # Saída: Desvio Padrão: 1.4142135623730951
            ```
             
    - **Pandas:**
    
        ```python
        import pandas as pd  # Importa a biblioteca Pandas
        ```

        - **Criando DataFrames:**:
            
            ```python
                            df = pd.DataFrame(data)
            ```
 
            
            - **Exemplo:**
                        
            ```python
                    import pandas as pd

                    # Define um dicionário com os dados
                    data = {'Notas': [20, 25, 30, 35, 40]}

                    # Cria um DataFrame Pandas a partir do dicionário
                    df = pd.DataFrame(data)
                    print(df)
            ```
             
        - **Calculando a média:**:
            
            ```python
                            media = df['Notas'].mean()
            ```
 
            
            - **Exemplo:**
                        
            ```python
                    # Calcula a média dos valores da coluna 'Notas'
                    media = df['Notas'].mean()
                    print(f"Média: {media}")  # Saída: Média: 30.0
            ```
                     
         - **Calculando a mediana:**:
            
            ```python
                            mediana = df['Notas'].median()
            ```

            
            - **Exemplo:**
                        
            ```python
                    # Calcula a mediana dos valores da coluna 'Notas'
                    mediana = df['Notas'].median()
                    print(f"Mediana: {mediana}")  # Saída: Mediana: 30.0
            ```
               
         - **Calculando a moda:**:
            
            ```python
                            moda = df['Notas'].mode()[0]
            ```

            
            - **Exemplo:**
                        
            ```python
                    # Calcula a moda dos valores da coluna 'Notas'
                    moda = df['Notas'].mode()[0]
                    print(f"Moda: {moda}")  # Saída: Moda: 20
            ```
               
         - **Calculando a variância:**:
            
            ```python
                            variancia = df['Notas'].var()
            ```

            
            - **Exemplo:**
                        
            ```python
                    # Calcula a variância dos valores da coluna 'Notas'
                    variancia = df['Notas'].var()
                    print(f"Variância: {variancia}")  # Saída: Variância: 62.5
            ```
                         
         - **Calculando a desvio padrão:**:
            
            ```python
                            variancia = df['Notas'].var()
            ```

            
            - **Exemplo:**
                        
            ```python
                    # Calcula o desvio padrão dos valores da coluna 'Notas'
                    desvio_padrao = df['Notas'].std()
                    print(f"Desvio Padrão: {desvio_padrao}")  # Saída: Desvio Padrão: 7.905694150420949
            ```
              
### **2.4 Em Resumo:**
            
    NumPy e Pandas são ferramentas Python para manipulação de dados. NumPy é ótimo para arrays e Pandas para dados tabulares. Eles oferecem uma gama de operações, como estatísticas, filtragem, ordenação, agrupamento, etc.
            
>
