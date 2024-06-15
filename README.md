<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

# Aula de Estatística com Python: Probabilidade e Amostragem

Turma ON29 | Python | Semana 12 | 2024 | Professora Camila Ribeiro


**Conteúdo:**

**Parte 1: Introdução à Estatística**

- **Conceitos Básicos:**
    - **1.1.1 Estatística: Definição e Importância**
        
        **Importância de Estudar Estatística:**
        
        - Nos ajuda a entender o mundo, tomar decisões embasadas, melhorar a qualidade de produtos/serviços, realizar pesquisas científicas e é valiosa no mercado de trabalho.
        
        **Vantagens de Estudar Estatística:**
        
        - Aprimora o pensamento crítico, auxilia na compreensão da incerteza, favorece decisões racionais e amplia oportunidades profissionais.
        
        **Desvantagens de Estudar Estatística:**
        
        - Complexidade, necessidade de softwares/ferramentas, a importância da interpretação correta e suas limitações.
        
        **Preconceitos:**
        
        - **Interpretação enviesada:** Dados podem ser mal interpretados, gerando conclusões errôneas e preconceitos. O contexto e metodologia devem ser considerados.
        - **Generalizações perigosas:** O uso inadequado de estatísticas pode gerar generalizações sobre grupos. Lembrar-se que estatísticas mostram tendências, não realidades individuais.
        - **Discriminação algorítmica:** Algoritmos treinados com dados enviesados podem discriminar grupos. Garantir representatividade e justiça nos dados é essencial.
        
        **Estatística em Tecnologia:**
        
        - **Desafios:** Tecnologia enfrenta problemas com preconceitos, especialmente em machine learning e reconhecimento facial.
        - **Soluções:** Empresas devem adotar práticas éticas e responsáveis, coletar dados representativos, auditar algoritmos e ser transparentes.
        
        **Conclusão:**
        
        **Aprender Estatística requer esforço, mas traz benefícios profissionais e pessoais.** Nos permite lidar com dados de forma crítica e inteligente, tomar decisões efetivas e abre oportunidades. É importante usar a estatística com responsabilidade para promover igualdade e justiça.
        
    - **Tipos de Dados (qualitativos e quantitativos)**
        
        Existem dois tipos principais de dados:
        
        - **Dados Qualitativos (Categóricos):** Representam categorias ou características não numéricas, como cor dos olhos ou tipo de carro. Podem ser **nominais** (sem ordem, como cores) ou **ordinais** (com ordem, como graus de satisfação).
        - **Dados Quantitativos (Numéricos):** Representam quantidades mensuráveis. Podem ser **discretos** (contagens, valores inteiros, como número de filhos) ou **contínuos** (medidas que podem assumir qualquer valor, como altura ou temperatura).
        
        Entender a diferença entre os tipos de dados é fundamental para a escolha de ferramentas estatísticas adequadas para análise e interpretação.
        
      
    - **Medidas Descritivas: Média, Mediana, Moda, Variância e Desvio Padrão**
        
        As medidas descritivas são ferramentas essenciais na Estatística, pois nos permitem resumir e representar características importantes de um conjunto de dados de forma concisa e informativa. Elas nos ajudam a entender a tendência central dos dados (onde a maioria dos valores se concentra) e a dispersão (quão espalhados os dados estão em torno do centro).
        
        As principais medidas descritivas são:
        
        - **Média:** A média é a soma de todos os valores de um conjunto de dados dividido pelo número de observações. É uma medida de tendência central.
            - **1. A Média: O Ponto de Encontro dos Dados**
                - **A analogia:** Imagine um grupo de amigos que decide se encontrar em um restaurante para jantar. A média das horas de chegada de cada amigo representa o horário médio de encontro.
                - **A definição:** A média é como encontrar o ponto de equilíbrio de um conjunto de dados. Ela representa o "valor típico" ou "valor central" dos dados.
                - **Como calcular:** Somamos todos os valores do conjunto de dados e dividimos pelo número total de valores.
                  - **Fórmula:** Média = Soma dos valores / Número de observações
                  - **Exemplo:** Se as idades de cinco amigos são 20, 25, 30, 35 e 40, a média das idades é (20 + 25 + 30 + 35 + 40) / 5 = 30 anos.
                  - **Interpretação:** A média nos diz que, em média, os amigos têm 30 anos.
            
- **Mediana:** A mediana é o valor que divide um conjunto de dados ordenado em duas partes iguais. É outra medida de tendência central.
                
**Definição:** A mediana divide um conjunto de dados ordenado em duas partes iguais.
- **Como calcular:** Ordenamos os dados e encontramos o valor do meio.
- **Exemplo:** Em (20, 25, 30, 35, 40), a mediana é 30, pois é o valor do meio.
- **Interpretação:** A mediana indica que metade dos valores está abaixo de 30 e metade está acima.
- **Moda:** É o valor mais frequente em um conjunto de dados.
- **Exemplo:** Se as notas são 7, 8, 8, 9, 9, 9, 10, a moda é 9, pois aparece mais vezes.
- **Observação:** Um conjunto pode ter mais de uma moda ou nenhuma (se todos os valores aparecem uma única vez).
                      
- **Variância:** Mede a dispersão dos dados em relação à média.
- **Como calcular:** Calculamos a média, subtraímos a média de cada valor, elevamos ao quadrado essa diferença e somamos todos os quadrados. Dividimos essa soma pelo número de valores menos 1.
- **Exemplo:** Se a variância das idades é alta, as idades são muito diferentes entre si.
- **Interpretação:** Alta variância indica que os dados estão mais espalhados ao redor da média.
        
- **Desvio Padrão:** É a raiz quadrada da variância.
- **Como calcular:** Calculamos a raiz quadrada da variância.
- **Exemplo:** Para as idades do exemplo: Desvio Padrão = √10 ≈ 3,16
- **Interpretação:** Alto desvio padrão indica que os dados estão mais espalhados ao redor da média.
                        
**Em Resumo:**
                        
As medidas descritivas fornecem uma visão geral dos dados, revelando sua tendência central e dispersão. A média, mediana e moda indicam o "centro" dos dados, enquanto a variância e o desvio padrão quantificam a dispersão.
                        
**Exemplo Completo:**
                        
Idades: 25, 28, 30, 32, 35.
                        
- **Média:** 30
- **Mediana:** 30
- **Moda:** Nenhuma
- **Variância:** 10
- **Desvio Padrão:** √10 ≈ 3,16
                
- **1.1.4 Exemplos Práticos e Exercícios**
- **Exemplo 1:** Um grupo de amigos está planejando uma viagem e deseja saber o preço médio dos voos para um determinado destino. Para isso, eles pesquisam os preços de diferentes companhias aéreas e registram os valores em uma tabela. Em seguida, eles usam a média para calcular o preço médio dos voos.
- **Exemplo 1:**
- **Justificativa:** A média é uma medida de tendência central que representa o valor típico de um conjunto de dados. Ao calcular a média dos preços dos voos, o grupo de amigos consegue ter uma ideia do custo médio das passagens aéreas para o destino desejado, ajudando-os a planejar seu orçamento.
 - **Exemplo 2:** Uma empresa está analisando o desempenho de seus vendedores e deseja identificar o vendedor que vendeu mais produtos no último mês. Para isso, eles usam a moda para determinar o vendedor com maior número de vendas.
- **Exemplo 2:**
- **Justificativa:** A moda é uma medida de tendência central que indica o valor mais frequente em um conjunto de dados. Neste caso, a empresa usa a moda para identificar o vendedor com maior número de vendas, ou seja, o vendedor que mais vendeu produtos no último mês.
- **Exercício 1:** Calcule a média, mediana, moda, variância e desvio padrão dos seguintes dados: 10, 15, 20, 25, 30.
 - **Exercício 1:**
 - **Dados:** 10, 15, 20, 25, 30
- **Média:** (10 + 15 + 20 + 25 + 30) / 5 = 20
- **Mediana:** 20 (o valor do meio do conjunto ordenado)
 - **Moda:** Não há moda, pois todos os valores aparecem apenas uma vez.
 - **Variância:**
 - [(10-20)² + (15-20)² + (20-20)² + (25-20)² + (30-20)²] / 5 = 50
  - **Desvio Padrão:** √50 ≈ 7.07
  - **Exercício 2:** Determine qual tipo de dado (qualitativo ou quantitativo) cada uma das seguintes variáveis representa:
            - Cor do carro
            - Altura de uma pessoa
            - Número de alunos em uma sala de aula
            - Temperatura de um ambiente
            - Gênero
            
**Exercício 2:**
            
            - **Cor do carro:** **Qualitativo** (representa uma categoria, não um valor numérico).
            - **Altura de uma pessoa:** **Quantitativo Contínuo** (pode assumir qualquer valor dentro de um intervalo).
            - **Número de alunos em uma sala de aula:** **Quantitativo Discreto** (representa uma contagem, valores inteiros).
            - **Temperatura de um ambiente:** **Quantitativo Contínuo** (pode assumir qualquer valor dentro de um intervalo).
            - **Gênero:** **Qualitativo** (representa uma categoria, não um valor numérico).
         
        
    
- **Introdução ao Python para Estatística:**
    - Instalação e configuração do ambiente Python (incluindo bibliotecas NumPy, Pandas, Matplotlib e Seaborn).
    - **1.2.1 Instalação e Configuração do Ambiente Python**
        - **Instalar Python:** Baixe o Python 3.x da página oficial ([**https://www.python.org/downloads/**](https://www.python.org/downloads/)) e siga as instruções de instalação para o seu sistema operacional.
        - **Instalar Bibliotecas Essenciais:**
            - **NumPy:** pip install numpy
            - **Pandas:** pip install pandas
            - **Matplotlib:** pip install matplotlib
            - **Seaborn:** pip install seaborn
            - Você pode instalar todas as bibliotecas de uma vez usando: pip install numpy pandas matplotlib seaborn
        - **Verificar a Instalação:** Abra o interpretador Python (terminal/prompt de comando e digite python) e importe as bibliotecas. Se não houver erros, a instalação está correta.
    - Demonstração prática de manipulação de dados com NumPy e Pandas.
    - **1.2.3 Demonstração Prática de Manipulação de Dados com NumPy e Pandas**
        - **NumPy:**
            - Criando arrays: arr = np.array([1, 2, 3, 4, 5])
                - **arr = np.array([1, 2, 3, 4, 5])**
                    - **Explicação:** Essa linha cria um array NumPy chamado arr com os valores 1, 2, 3, 4 e 5. Arrays NumPy são estruturas de dados unidimensionais (vetores) ou multidimensionais (matrizes) que armazenam dados numéricos de forma eficiente.
                    - **Exemplo:**
                        
                        ```jsx
                        import numpy as np
                        
                        arr = np.array([1, 2, 3, 4, 5])
                        print(arr)  # Saída: [1 2 3 4 5]
                        ```
                        
            - Calculando a média: media = np.mean(arr)
                - **media = np.mean(arr)**
                    - **Explicação:** Essa linha calcula a média dos valores do array arr e armazena o resultado na variável media. A função np.mean() é uma função do NumPy que calcula a média de um array.
                    - **Exemplo:**
                        
                        ```jsx
                        import numpy as np
                        
                        arr = np.array([1, 2, 3, 4, 5])
                        media = np.mean(arr)
                        print(media)  # Saída: 3.0
                        ```
                        
            - Calculando o desvio padrão: desvio_padrao = np.std(arr)
                - **desvio_padrao = np.std(arr)**
                    - **Explicação:** Essa linha calcula o desvio padrão dos valores do array arr e armazena o resultado na variável desvio_padrao. A função np.std() é uma função do NumPy que calcula o desvio padrão de um array.
                    - **Exemplo:**
                        
                        ```jsx
                        import numpy as np
                        
                        arr = np.array([1, 2, 3, 4, 5])
                        desvio_padrao = np.std(arr)
                        print(desvio_padrao)  # Saída: 1.5811388300841898
                        ```
                        
            - **Pandas:**
                - **1. Criando DataFrames:**: df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]})
                    - **df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]})**
                        - **Explicação:** Essa linha cria um DataFrame Pandas chamado df com duas colunas: 'Nome' e 'Idade'. O DataFrame é uma estrutura de dados tabular (como uma planilha) que organiza dados em linhas e colunas.
                        - **Exemplo:**
                            
                            ```jsx
                            import pandas as pd
                            
                            df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]})
                            print(df)
                            # Saída:
                            #       Nome  Idade
                            # 0    Alice     25
                            # 1      Bob     30
                            # 2  Charlie     35
                            ```
                            
                - **2. Acessando colunas:**: df['Nome']
                        - **Explicação:** Essa linha acessa a coluna 'Nome' do DataFrame df. O resultado é uma Série Pandas, que é uma estrutura de dados unidimensional.
                        - **Exemplo:**
                            
                            ```jsx
                            print(df['Nome'])
                            # Saída:
                            # 0      Alice
                            # 1        Bob
                            # 2    Charlie
                            # Name: Nome, dtype: object
                            ```
                            
                    - **3. Calculando a média de uma coluna:**
                    - **df['Idade'].mean()**
                        - **Explicação:** Essa linha calcula a média dos valores da coluna 'Idade' do DataFrame df. A função mean() é um método da Série Pandas que calcula a média dos seus valores.
                        - **Exemplo:**
                            
                            ```jsx
                            print(df['Idade'].mean())  # Saída: 30.0
                            ```
                            
                    - **4. Filtrando linhas:**
                    - **df[df['Idade'] > 30]**
                        - **Explicação:** Essa linha filtra as linhas do DataFrame df onde o valor da coluna 'Idade' é maior que 30. A condição df['Idade'] > 30 cria uma máscara booleana (True/False) para cada linha, selecionando apenas as linhas que atendem à condição.
                        - **Exemplo:**
                            
                            ```jsx
                            print(df[df['Idade'] > 30])
                            # Saída:
                            #       Nome  Idade
                            # 2  Charlie     35
                            ```
                            
            
            ## Resumo
            
            NumPy e Pandas são ferramentas Python para manipulação de dados. NumPy é ótimo para arrays e Pandas para dados tabulares. Eles oferecem uma gama de operações, como estatísticas, filtragem, ordenação, agrupamento, etc.
            
    - **1.2.4 Exercícios Práticos com Python**

        - **Exercício 1:** Crie um array NumPy com os seguintes valores: 10, 15, 20, 25, 30. Calcule a média, mediana, moda, variância e desvio padrão usando as funções do NumPy.

            
           ```jsx
           import numpy as np
            
            # Criando o array NumPy
            arr = np.array([10, 15, 20, 25, 30])
            
            # Calculando a média
            media = np.mean(arr)
            print(f"Média: {media}")  # Saída: Média: 20.0
            
            # Calculando a mediana
            mediana = np.median(arr)
            print(f"Mediana: {mediana}")  # Saída: Mediana: 20.0
            
            # Calculando a moda (não há moda, pois todos os valores são distintos)
            moda = np.argmax(np.bincount(arr))  # Retorna o índice do valor mais frequente
            print(f"Moda: {moda}")  # Saída: Moda: 0 (pois o índice 0 corresponde ao valor 10, que não é a moda)
            
            # Calculando a variância
            variancia = np.var(arr)
            print(f"Variância: {variancia}")  # Saída: Variância: 50.0
            
            # Calculando o desvio padrão
            desvio_padrao = np.std(arr)
            print(f"Desvio Padrão: {desvio_padrao}")  # Saída: Desvio Padrão: 7.0710678118654755
            ```
            
            **Justificativa:** O código utiliza as funções do NumPy para calcular as medidas descritivas do array.
            
            - np.mean(): Calcula a média dos valores do array.
            - np.median(): Calcula a mediana do array.
            - np.bincount(): Conta a frequência de cada valor no array. np.argmax() encontra o índice do valor mais frequente (moda).
            - np.var(): Calcula a variância do array.
            - np.std(): Calcula o desvio padrão do array.
              
        - **Exercício 2:** Crie um DataFrame Pandas com os nomes e idades de cinco pessoas. Calcule a média das idades e filtre as pessoas com mais de 30 anos.
            
            ```jsx
            import pandas as pd
            
            # Criando o DataFrame Pandas
            df = pd.DataFrame({'Nome': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'], 
                               'Idade': [25, 30, 35, 28, 40]})
            
            # Calculando a média das idades
            media_idades = df['Idade'].mean()
            print(f"Média das Idades: {media_idades}")  # Saída: Média das Idades: 31.6
            
            # Filtrando as pessoas com mais de 30 anos
            pessoas_mais_velhas = df[df['Idade'] > 30]
            print(pessoas_mais_velhas)
            # Saída:
            #       Nome  Idade
            # 2  Charlie     35
            # 4    Emily     40
             ```
            
            **Justificativa:** O código utiliza o Pandas para criar um DataFrame e realizar operações com ele.
            
            - pd.DataFrame(): Cria um DataFrame a partir de um dicionário.
            - df['Idade'].mean(): Calcula a média dos valores da coluna 'Idade'.
            - df[df['Idade'] > 30]: Filtra as linhas do DataFrame onde o valor da coluna 'Idade' é maior que 30.
        - **Exercício 3:** Utilize a biblioteca Matplotlib para criar um histograma que represente a distribuição das idades do DataFrame criado no exercício anterior.
            - **Exercício 3:**
            
            ```jsx
            import matplotlib.pyplot as plt
            
            # Criando o histograma
            plt.hist(df['Idade'], bins=5, edgecolor='black')
            plt.xlabel('Idade')
            plt.ylabel('Frequência')
            plt.title('Distribuição de Idades')
            plt.show()
            ```
            
            **Justificativa:** O código utiliza o Matplotlib para criar um histograma.
            
            - plt.hist(): Cria um histograma da coluna 'Idade' do DataFrame, com 5 barras (bins).
            - plt.xlabel(), plt.ylabel(), plt.title(): Define os rótulos dos eixos e o título do gráfico.
            - plt.show(): Exibe o gráfico.
            
            O histograma mostra a distribuição das idades, com o número de pessoas em cada faixa de idade.
            

**Parte 2: Probabilidade**

- **Conceitos Fundamentais:**
    - **2.1.1 Definição de Probabilidade e Eventos**
        - **Probabilidade:** A probabilidade é a medida da chance de um evento ocorrer. É um número entre 0 e 1, onde 0 representa a impossibilidade do evento e 1 representa a certeza do evento.
         - **Evento:** Um evento é um resultado específico ou um conjunto de resultados possíveis em um experimento aleatório.
        - **Exemplo:**
        - **Experimento:** Lançar um dado de seis faces.
        - **Evento:** Obter um número par.
                
    - **2.1.2 Espaço Amostral**
        - **Definição:** O espaço amostral é o conjunto de todos os resultados possíveis de um experimento aleatório.
        - **Exemplo:**
            - **Experimento:** Lançar uma moeda.
            - **Espaço Amostral:** {Cara, Coroa}
    - **2.1.3 Tipos de Probabilidade**
        - **Probabilidade Clássica:** A probabilidade clássica é calculada como a razão entre o número de resultados favoráveis a um evento e o número total de resultados possíveis, assumindo que todos os resultados são igualmente prováveis.
            - **Exemplo:** A probabilidade de obter cara ao lançar uma moeda é 1/2, pois há um resultado favorável (cara) e dois resultados possíveis (cara ou coroa).
        - **Probabilidade Frequentista:** A probabilidade frequentista é estimada observando a frequência relativa de um evento em um grande número de repetições do experimento.
            - **Exemplo:** Se lançarmos uma moeda 100 vezes e obtermos cara 52 vezes, a probabilidade frequentista de obter cara é 52/100 = 0,52.
        - **Probabilidade Subjetiva:** A probabilidade subjetiva é baseada na opinião, crença ou experiência pessoal de um indivíduo.
            - **Exemplo:** A probabilidade de um time de futebol vencer um jogo, baseada na análise de um torcedor.
    - **2.1.4 Regras de Probabilidade**
        - **Regra da Soma:** A probabilidade da união de dois eventos mutuamente exclusivos (que não podem ocorrer ao mesmo tempo) é a soma das probabilidades dos eventos individuais.
            - **Exemplo:** A probabilidade de obter cara ou coroa ao lançar uma moeda é 1/2 + 1/2 = 1.
        - **Regra da Multiplicação:** A probabilidade da interseção de dois eventos independentes (a ocorrência de um evento não afeta a ocorrência do outro) é o produto das probabilidades dos eventos individuais.
            - **Exemplo:** A probabilidade de obter cara em dois lançamentos consecutivos de uma moeda é 1/2 * 1/2 = 1/4.
        - **Probabilidade Condicional:** A probabilidade condicional é a probabilidade de um evento ocorrer dado que outro evento já ocorreu.
            - **Fórmula:** P(A|B) = P(A e B) / P(B), onde P(A|B) é a probabilidade de A ocorrer dado que B já ocorreu.
            - **Exemplo:** Se temos um baralho de 52 cartas, a probabilidade de tirar um ás dado que a carta retirada é de copas é 1/13, pois há um ás de copas e 13 cartas de copas no baralho.
    - **2.1.5 Exemplos Práticos e Exercícios**
        - **Exemplo 1:** Qual a probabilidade de tirar um número par ao lançar um dado de seis faces?
            - **Resposta:** 3/6 = 1/2, pois há três números pares (2, 4, 6) e seis resultados possíveis.
        - **Exemplo 2:** Qual a probabilidade de tirar cara em dois lançamentos consecutivos de uma moeda?
            - **Resposta:** 1/2 * 1/2 = 1/4.
        - **Exercício 1:** Se temos um saco com 5 bolas vermelhas, 3 bolas azuis e 2 bolas verdes, qual a probabilidade de tirar uma bola azul?
        - **Exercício 2:** Qual a probabilidade de tirar um rei ou uma dama de um baralho de 52 cartas?

- **Probabilidade com Python:**
    - **2.2.1 Simulação de Eventos Aleatórios com Python**
        - **Biblioteca random:** A biblioteca random em Python fornece funções para gerar números aleatórios e simular eventos aleatórios.
        - **Exemplo:**
            
            ```jsx
            import random
            
            # Simular o lançamento de uma moeda
            resultado = random.choice(['Cara', 'Coroa'])
            print(resultado)  # Imprime 'Cara' ou 'Coroa' aleatoriamente
            ```
            
    - **2.2.2 Cálculo de Probabilidade com Funções da Biblioteca NumPy**
        - **Exemplo:**
            
            ```jsx
            import numpy as np
            
            # Números possíveis ao lançar um dado
            numeros = np.arange(1, 7)
            
            # Números pares entre os possíveis números
            numeros_pares = numeros[numeros % 2 == 0]
            
            # Probabilidade de obter um número par
            probabilidade = len(numeros_pares) / len(numeros)
            print(probabilidade)  # Saída: 0.5
            ```
            
    - **2.2.3 Criação de Gráficos de Probabilidade com Matplotlib**
        - **Exemplo:**
            
            ```jsx
            import matplotlib.pyplot as plt
            
            # Distribuição de probabilidade de um dado de seis faces
            probabilidades = np.ones(6) / 6
            plt.bar(np.arange(1, 7), probabilidades)
            plt.xlabel('Faces do Dado')
            plt.ylabel('Probabilidade')
            plt.title('Distribuição de Probabilidade de um Dado')
            plt.show()
            ```
            
    - Exercícios práticos com Python.
    - **2.2.4 Exercícios Práticos com Python**
        - **Exercício 1:** Simule 100 lançamentos de um dado e calcule a probabilidade frequentista de obter um número par.
        - **Exercício 2:** Crie um gráfico de barras que represente a distribuição de probabilidade de tirar uma carta de um baralho de 52 cartas (considerando as figuras).

**Parte 3: Amostragem** 

- **Métodos de Amostragem :**
- Em muitas situações, é inviável ou caro analisar toda a população de interesse. Por isso, recorremos à amostragem: selecionamos uma parte representativa da população para realizar a análise.

    - **3.1.1 Amostragem Aleatória Simples**
        - **Definição:** Cada elemento da população tem a mesma chance de ser selecionado para a amostra. É como sortear um bilhete em uma loteria: todos os bilhetes têm a mesma chance de serem sorteados.
        - **Exemplo:** Imaginemos uma pesquisa de opinião sobre a preferência por um novo produto. Se a população é de 10.000 pessoas, podemos selecionar uma amostra aleatória simples de 1.000 pessoas, onde cada pessoa tem 1/10 chance de ser escolhida.
        - **Vantagens:** Fácil de implementar, boa representatividade se a população for homogênea.
        - **Desvantagens:** Pode ser difícil obter uma amostra aleatória verdadeira, especialmente em populações grandes.

    - **3.1.2 Amostragem Estratificada**
        - **Definição:** A população é dividida em subgrupos (estratos) com características homogêneas, e uma amostra aleatória simples é selecionada dentro de cada estrato.
        - **Exemplo:** Imagine uma pesquisa sobre o nível de satisfação dos alunos em uma escola. Podemos dividir os alunos em estratos por série (fundamental I, fundamental II, ensino médio), e selecionar uma amostra aleatória simples dentro de cada série.
        - **Vantagens:** Melhor representação de subgrupos da população, garante que cada grupo seja devidamente amostrado.
        - **Desvantagens:** Exige conhecimento da população e sua divisão em estratos.

    - **3.1.3 Amostragem por Conglomerados**
        - **Definição:** A população é dividida em grupos naturais (conglomerados), e alguns conglomerados são selecionados aleatoriamente. Em seguida, todos os elementos dentro dos conglomerados selecionados são incluídos na amostra.
        - **Exemplo:** Imagine uma pesquisa sobre as condições de saúde de estudantes universitários. Podemos dividir os estudantes por curso, selecionar alguns cursos aleatoriamente e entrevistar todos os alunos dos cursos escolhidos.
        - **Vantagens:** Útil quando a população está dispersa geograficamente, reduz custos de coleta de dados.
        - **Desvantagens:** Menos precisa que a amostragem aleatória simples se os conglomerados não forem homogêneos.

    - **3.1.4 Amostragem Sistemática**
        - **Definição:** Selecionamos o primeiro elemento da amostra aleatoriamente e, a partir dele, selecionamos os outros elementos a intervalos regulares.
        - **Exemplo:** Imagine uma pesquisa sobre a qualidade de um produto em uma linha de produção. Podemos selecionar o primeiro produto aleatoriamente e, a partir dele, selecionar cada décimo produto da linha.
        - **Vantagens:** Fácil de implementar, pode ser mais eficiente que a amostragem aleatória simples em algumas situações.
        - **Desvantagens:** Pode ser enviesada se houver um padrão cíclico nos dados.

    - **3.1.5 Erros Amostrais e Intervalos de Confiança**
        - **Erro Amostral:** A diferença entre a estatística da amostra (média, proporção) e o parâmetro populacional correspondente.
        - **Intervalo de Confiança:** Um intervalo de valores que provavelmente contém o parâmetro populacional, com um determinado nível de confiança.
        - **Exemplo:** Imagine uma pesquisa sobre a altura média dos alunos de uma escola. Se a altura média da amostra é 1,65m, o intervalo de confiança de 95% para a altura média da população pode ser de 1,60m a 1,70m. Isso significa que há 95% de chance de a altura média da população estar nesse intervalo.

    - **3.1.6 Exemplos Práticos e Exercícios**
        - **Exemplo:** Uma empresa de alimentos deseja saber a preferência dos consumidores por um novo sabor de iogurte. Para isso, ela pode usar a amostragem aleatória simples para selecionar uma amostra de consumidores.
        - **Exercício:** Um pesquisador deseja estudar as condições de moradia em uma cidade. Ele pode usar a amostragem por conglomerados, dividindo a cidade em bairros e selecionando aleatoriamente alguns bairros para estudo.

- **Amostragem com Python:**

    - **3.2.1 Implementação de Métodos de Amostragem com Pandas e NumPy**
        
        
        - **Exemplo:**
        
        ```jsx
        import numpy as np
        import pandas as pd
        
        # Dados da população
        populacao = np.arange(1, 101)
        
        # Amostragem aleatória simples
        amostra_aleatoria_simples = list(np.random.choice(populacao, size=10, replace=False)) 
        amostra_aleatoria_simples.extend([None] * (len(populacao) - len(amostra_aleatoria_simples)))  # Preenche o restante com None
        
        # Amostragem estratificada (dividindo em dois estratos: 1-50 e 51-100)
        estrato1 = populacao[0:50]
        estrato2 = populacao[50:100]
        amostra_estratificada = list(np.concatenate((np.random.choice(estrato1, size=5, replace=False),
                                                np.random.choice(estrato2, size=5, replace=False))))
        amostra_estratificada.extend([None] * (len(populacao) - len(amostra_estratificada)))  # Preenche o restante com None
        
        # Amostragem sistemática (selecionando cada 5º elemento)
        amostra_sistematica = list(populacao[::5])
        amostra_sistematica.extend([None] * (len(populacao) - len(amostra_sistematica)))  # Preenche o restante com None
        
        # Criando um DataFrame com os dados
        df = pd.DataFrame({'População': populacao,
                           'Amostra Aleatória Simples': amostra_aleatoria_simples,
                           'Amostra Estratificada': amostra_estratificada,
                           'Amostra Sistemática': amostra_sistematica})
        print(df)
        ```

    - **3.2.2 Cálculo de Estatísticas Descritivas e Intervalos de Confiança**
        - **Exemplo:**
            
            ```jsx
            import numpy as np
            import scipy.stats as stats
            
            # Dados da população (simulando uma população de 100 elementos)
            populacao = np.arange(1, 101)
            
            # Amostragem aleatória simples (selecionando 10 elementos aleatórios)
            amostra_aleatoria_simples = np.random.choice(populacao, size=10, replace=False)
            
            # Calculando a média e o desvio padrão da amostra
            media_amostra = np.mean(amostra_aleatoria_simples)
            desvio_padrao_amostra = np.std(amostra_aleatoria_simples)
            
            # Calculando o intervalo de confiança de 95% para a média populacional
            intervalo_confianca = stats.t.interval(confidence=0.95,  # Adicionando o argumento 'confidence'
            df=len(amostra_aleatoria_simples)-1,
            loc=media_amostra, scale=desvio_padrao_amostra / np.sqrt(len(amostra_aleatoria_simples)))
            print(f"Intervalo de Confiança de 95%: {intervalo_confianca}")
            ```
            
    - **3.2.3 Visualização de Dados com Matplotlib**
        - **Exemplo:**
            
            ```jsx
            import matplotlib.pyplot as plt
            
            plt.hist(amostra_aleatoria_simples, bins=10, edgecolor='black')
            plt.xlabel('Valores da Amostra')
            plt.ylabel('Frequência')
            plt.title('Histograma da Amostra Aleatória Simples')
            plt.show()
            ```
            
    - **3.2.4 Exercícios Práticos com Python**
        - **Exercício 1:** Implemente a amostragem por conglomerados para um conjunto de dados de clientes de uma loja, agrupados por região.
        - **Exercício 2:** Calcule o intervalo de confiança de 95% para a média da altura de uma amostra de alunos de uma escola.
        - **Exercício 3:** Crie um gráfico de dispersão para visualizar a relação entre a idade e o salário de uma amostra de funcionários de uma empresa.

<p align="center">
Desenvolvido com :purple_heart:  
</p>

