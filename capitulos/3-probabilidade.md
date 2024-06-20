## 3. Probabilidade

### **Conceitos Fundamentais**

### **3.1 Definição de Probabilidade e Eventos**

- **Probabilidade:** A probabilidade é a medida da chance de um evento ocorrer. É um número entre 0 e 1, onde 0 representa a impossibilidade do evento e 1 representa a certeza do evento.

- **Evento:** Um evento é um resultado específico ou um conjunto de resultados possíveis em um experimento aleatório.

    - **Exemplos:**


        - **Experimento:** Lançar um dado de seis faces.
        - **Evento:** Obter um número par.

    - **Justificativa:**
        > Vamos usar o exemplo do dado. Se você jogar um dado de seis faces, existem seis possíveis resultados: 1, 2, 3, 4, 5 ou 6. Cada um desses é um evento. Agora, se quisermos falar sobre o evento “obter um número par”, estamos falando sobre três possíveis resultados: 2, 4 ou 6. A probabilidade desse evento é o número de resultados que satisfazem o evento (neste caso, 3: 2, 4 e 6) dividido pelo número total de resultados (neste caso, 6). Então, a probabilidade de obter um número par é 3/6 ou 0,5 (ou 50%).
    <br>

  ### **3.2 Espaço Amostral**

  O espaço amostral é o conjunto de todos os resultados possíveis de um experimento aleatório.
  
    - **Exemplos:**


        - **Experimento:** Lançar uma moeda.
        - **Espaço Amostral:** {Cara, Coroa}.

    - **Justificativa:**
        > Vamos usar o exemplo de lançar uma moeda. Quando você lança uma moeda, existem dois possíveis resultados: a moeda pode cair com a cara para cima ou com a coroa para cima. Então, o espaço amostral para este experimento é {Cara, Coroa}. Não importa quantas vezes você jogue a moeda, esses são os únicos resultados possíveis.
    <br>

 ### **3.3 Tipos de Probabilidade**

- **3.3.1 Probabilidade Clássica:**
A probabilidade clássica é calculada como a razão entre o número de resultados favoráveis a um evento e o número total de resultados possíveis, assumindo que todos os resultados são igualmente prováveis.

    - **Exemplos:**

```python
    A probabilidade de obter cara ao lançar uma moeda é 1/2, pois há um resultado favorável (cara) e dois resultados possíveis (cara ou coroa).
```

- **3.3.2 Probabilidade Frequentista:**
 
    A probabilidade frequentista é estimada observando a frequência relativa de um evento em um grande número de repetições do experimento.

    - **Exemplos:**


```python
    Se lançarmos uma moeda 100 vezes e obtermos cara 52 vezes, a probabilidade frequentista de obter cara é 52/100 = 0,52 ou 52%.
```

- **3.3.3 Probabilidade Subjetiva:**
A probabilidade subjetiva é baseada na opinião, crença ou experiência pessoal de um indivíduo.

    - **Exemplos:**

```python
    A probabilidade de um time de futebol vencer um jogo, baseada na análise de um torcedor.
```

### **3.4 Regras de Probabilidade**

- **3.4.1 Regra da Soma:**
    A probabilidade da união de dois eventos mutuamente exclusivos (que não podem ocorrer ao mesmo tempo) é a soma das probabilidades dos eventos individuais.

    - **Exemplo:** 

```python        
    A probabilidade de obter cara ou coroa ao lançar uma moeda é 1/2 + 1/2 = 1.
```

- **3.4.2 Regra da Multiplicação:**

    A probabilidade da interseção de dois eventos independentes (a ocorrência de um evento não afeta a ocorrência do outro) é o produto das probabilidades dos eventos individuais.
    
    - **Exemplos:**

```python
    A probabilidade de obter cara em dois lançamentos consecutivos de uma moeda é 1/2 * 1/2 = 1/4.
```

- **3.4.3 Probabilidade Condicional:**

    A probabilidade condicional é a probabilidade de um evento ocorrer dado que outro evento já ocorreu.


    - **Fórmula:**

```python
    P(A|B) = P(A e B) / P(B), onde P(A|B) é a probabilidade de A ocorrer dado que B já ocorreu.
```

- **Exemplos:**

```python
    Se temos um baralho de 52 cartas, a probabilidade de tirar um ás dado que a carta retirada é de copas é 1/13, pois há um ás de copas e 13 cartas de copas no baralho.
```

>
