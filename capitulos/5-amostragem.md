## 5. Amostragem

### **Conceitos Fundamentais**

### **35.1 Métodos de Amostragem**

Em muitas situações, é inviável ou caro analisar toda a população de interesse. Por isso, recorremos à amostragem: selecionamos uma parte representativa da população para realizar a análise.

- **5.1.1 Amostragem Aleatória Simples:**

    Cada elemento da população tem a mesma chance de ser selecionado para a amostra. É como sortear um bilhete em uma loteria: todos os bilhetes têm a mesma chance de serem sorteados.

- **Exemplo:** 

    ```python
    Imaginemos uma pesquisa de opinião sobre a preferência por um novo produto. Se a população é de 10.000 pessoas, podemos selecionar uma amostra aleatória simples de 1.000 pessoas, onde cada pessoa tem 1/10 chance de ser escolhida.
    ```

- **Vantagens:** 

```python
    Fácil de implementar, boa representatividade se a população for homogênea.
```
- **Desvantagens:** 

```python
    Pode ser difícil obter uma amostra aleatória verdadeira, especialmente em populações grandes.
```

- **5.1.2 Amostragem Estratificada:**

    A população é dividida em subgrupos (estratos) com características homogêneas, e uma amostra aleatória simples é selecionada dentro de cada estrato.


- **Exemplo:** 

    ```python
    Imagine uma pesquisa sobre o nível de satisfação dos alunos em uma escola. Podemos dividir os alunos em estratos por série (fundamental I, fundamental II, ensino médio), e selecionar uma amostra aleatória simples dentro de cada série.
    ```

- **Vantagens:** 

```python
    Melhor representação de subgrupos da população, garante que cada grupo seja devidamente amostrado.
```
- **Desvantagens:** 

```python
    Exige conhecimento da população e sua divisão em estratos.
```

- **5.1.3 Amostragem por Conglomerados**

    A população é dividida em grupos naturais (conglomerados), e alguns conglomerados são selecionados aleatoriamente. Em seguida, todos os elementos dentro dos conglomerados selecionados são incluídos na amostra.


- **Exemplo:** 

    ```python
    Imagine uma pesquisa sobre as condições de saúde de estudantes universitários. Podemos dividir os estudantes por curso, selecionar alguns cursos aleatoriamente e entrevistar todos os alunos dos cursos escolhidos.
    ```

- **Vantagens:** 

```python
    Útil quando a população está dispersa geograficamente, reduz custos de coleta de dados.
```
- **Desvantagens:** 

```python
    Menos precisa que a amostragem aleatória simples se os conglomerados não forem homogêneos.
```

- **5.1.4 Amostragem Sistemática**

    Selecionamos o primeiro elemento da amostra aleatoriamente e, a partir dele, selecionamos os outros elementos a intervalos regulares.


- **Exemplo:** 

    ```python
    Imagine uma pesquisa sobre a qualidade de um produto em uma linha de produção. Podemos selecionar o primeiro produto aleatoriamente e, a partir dele, selecionar cada décimo produto da linha.
    ```

- **Vantagens:** 

```python
    Fácil de implementar, pode ser mais eficiente que a amostragem aleatória simples em algumas situações.
```
- **Desvantagens:** 

```python
    Pode ser enviesada se houver um padrão cíclico nos dados.
```


- **5.1.5 Erros Amostrais e Intervalos de Confiança**

    A diferença entre a estatística da amostra (média, proporção) e o parâmetro populacional correspondente.

    - **Erro Amostral:** A diferença entre a estatística da amostra (média, proporção) e o parâmetro populacional correspondente.

    - **Intervalo de Confiança:** Um intervalo de valores que provavelmente contém o parâmetro populacional, com um determinado nível de confiança.

        - **Exemplo:** 
        
    ```python
    Imagine uma pesquisa sobre a altura média dos alunos de uma escola. Se a altura média da amostra é 1,65m, o intervalo de confiança de 95% para a altura média da população pode ser de 1,60m a 1,70m. Isso significa que há 95% de chance de a altura média da população estar nesse intervalo.
    ```

>

