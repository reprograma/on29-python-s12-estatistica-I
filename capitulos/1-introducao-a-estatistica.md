## 1. Introdução à Estatística

### **Conceitos Básicos:**

### **1.1 Estatística: Definição e Importância**

Estatística é a ciência que recolhe, arruma, estuda, interpreta e mostra dados para chegar a conclusões e fazer decisões bem informadas. Ela nos ajuda a entender padrões, tendências e relações em grupos de dados. Também ajuda a lidar com a incerteza e a variabilidade que existem em coisas reais.
        
#### **1.1.1 Importância de Estudar Estatística:**
        
- Nos ajuda a entender o mundo, tomar decisões embasadas, melhorar a qualidade de produtos/serviços, realizar pesquisas científicas e é valiosa no mercado de trabalho.
        
#### **1.1.2 Vantagens de Estudar Estatística:**
        
- Aprimora o pensamento crítico, auxilia na compreensão da incerteza, favorece decisões racionais e amplia oportunidades profissionais.
        
#### **1.1.3 Desvantagens de Estudar Estatística:**
        
- Complexidade, necessidade de softwares/ferramentas, a importância da interpretação correta e suas limitações.
        
#### **1.1.4 Preconceitos:**
        
- **Interpretação enviesada:** Dados podem ser mal interpretados, gerando conclusões errôneas e preconceitos. O contexto e metodologia devem ser considerados.
- **Generalizações perigosas:** O uso inadequado de estatísticas pode gerar generalizações sobre grupos. Lembrar-se que estatísticas mostram tendências, não realidades individuais.
- **Discriminação algorítmica:** Algoritmos treinados com dados enviesados podem discriminar grupos. Garantir representatividade e justiça nos dados é essencial.
        
#### **1.1.5 Estatística em Tecnologia:**
        
- **Desafios:** Tecnologia enfrenta problemas com preconceitos, especialmente em machine learning e reconhecimento facial.
- **Soluções:** Empresas devem adotar práticas éticas e responsáveis, coletar dados representativos, auditar algoritmos e ser transparentes.
        
### **Conclusão:**
        
**Aprender Estatística requer esforço, mas traz benefícios profissionais e pessoais.** Nos permite lidar com dados de forma crítica e inteligente, tomar decisões efetivas e abre oportunidades. É importante usar a estatística com responsabilidade para promover igualdade e justiça.

<br>

### **1.2 Tipos de Dados**
        
Existem dois tipos principais de dados: **qualitativos** e **quantitativos**.

#### **1.2.1 Dados Qualitativos (Categóricos):**

Representam categorias ou características não numéricas, como cor dos olhos ou tipo de carro. Podem ser **nominais** (sem ordem natural, como cores) ou **ordinais** (com ordem natural, como graus de satisfação).
    
                        
- **Exemplos:**
                        
```python
                - Cor dos olhos: Azul, verde, castanho, preto.
                - Tipo de carro: SUV, Sedan, Hatch, Pick-up.
                - Estado civil: Solteira, casada, divorciada, viúva.
                - Profissão: Médica, professora, advogada, engenheira.
```
                      
#### **1.2.2 Dados Quantitativos (Numéricos):**

Representam quantidades mensuráveis. Podem ser **discretos** (contagens, valores inteiros, como número de filhos) ou **contínuos** (medidas que podem assumir qualquer valor, como altura ou temperatura).

- **1.2.2.1 Dados Quantitativos Discretos:**

    **Definição:** Representam contagens, valores inteiros e não podem ser fracionados.
    - **Exemplos:**

```python
                - Número de filhos:** 0, 1, 2, 3, ...
                - Número de carros em uma garagem:** 0, 1, 2, 3, ...
                - Número de alunos em uma sala de aula:** 20, 25, 30, ...
```

- **1.2.2.2 Dados Quantitativos Contínuos:**

    **Definição:** Representam medidas e podem assumir qualquer valor dentro de um intervalo.
    - **Exemplos:**

```python
                - Altura: 1,70m, 1,85m, 1,60m
                - Salário: R$ 2.500,00, R$ 5.000,00, R$ 10.000,00.
                - Temperatura: 25°C, 30°C, 10°C.
```

<br>

> **💡Entender a diferença entre os tipos de dados é fundamental para a escolha de ferramentas estatísticas adequadas para análise e interpretação.**
 
<br>

>
### **1.3 Medidas Descritivas:**   
        
As medidas descritivas são ferramentas essenciais na Estatística, pois nos permitem resumir e representar características importantes de um conjunto de dados de forma concisa e informativa. Elas nos ajudam a entender a tendência central dos dados (onde a maioria dos valores se concentra) e a dispersão (quão espalhados os dados estão em torno do centro).
        
As principais medidas descritivas são: **média**, **mediana**, **moda**, **variância** e **desvio padrão**.

- **1.3.1 Média:**

    A média é uma medida de tendência central que representa o "valor típico" ou "valor central" dos dados.  É calculada como a soma de todos os valores de um conjunto de dados dividido pelo número de observações.
    - **Exemplos:**

```python
          Se as idades de cinco amigos são 20, 25, 30, 35 e 40, a média das idades é (20 + 25 + 30 + 35 + 40) / 5 = 30 anos.
```


- **Como calcular:** Somamos todos os valores do conjunto de dados e dividimos pelo número total de valores.

    - **Fórmula:** 

                                 Média = Soma dos valores / Número de observações

    - **Interpretação:** A média nos diz que, em média, os amigos têm 30 anos.

<br>

- **1.3.2 Mediana:**

    A mediana é o valor que divide um conjunto de dados ordenado em duas partes iguais. Ou seja, metade dos valores está abaixo da mediana e metade está acima.

    - **Exemplos:**

```python
          Em (20, 25, 30, 35, 40), a mediana é 30, pois é o valor do meio.
```

- **Como calcular:** Ordenamos os dados e encontramos o valor do meio.

    - **Fórmula:** 

            - Para número ímpar de dados, a mediana é o valor que está exatamente no meio do conjunto ordenado.
            - Para número par de dados, a mediana é a média dos dois valores centrais do conjunto ordenado.

    - **Interpretação:** A mediana indica que metade dos valores está abaixo de 30 e metade está acima.

<br>

- **1.3.3 Moda:**

    A moda é o valor que mais aparece em um conjunto de dados. Ela indica o valor mais frequente.

    - **Exemplos:**

```python
          Se as notas de um teste são 7, 8, 8, 9, 9, 9, 10, a moda é 9, pois é a nota que aparece mais vezes.
```
<br>

> **💡Observação: Um conjunto de dados pode ter mais de uma moda (bimodal, trimodal, etc.) ou não ter moda (se todos os valores aparecem uma única vez).**

<br>

- **1.3.4 Variância:**

    A variância mede a dispersão dos dados em relação à média. Ela indica o quão distantes os dados estão da média, ou seja, quão variáveis os dados são.
    - **Exemplos:**

```python
          Se temos um conjunto de dados 20, 25, 30, 35, 40.
          Média (μ): (20 + 25 + 30 + 35 + 40) / 5 = 30
          Diferenças: (20 - 30) = -10, (25 - 30) = -5, (30 - 30) = 0, (35 - 30) = 5, (40 - 30) = 10
          Quadrado das diferenças: (-10)² = 100, (-5)² = 25, 0² = 0, 5² = 25, 10² = 100
          Soma: 100 + 25 + 0 + 25 + 100 = 250
          Variância: 250 / (5 - 1) = 62.5
```

> **💡Observação: Dividimos essa soma pelo número de valores menos 1, quando é variância amostra, quando é populacional, não acrescenta o menos 1**

- **Como calcular:** Calculamos a média dos dados. Em seguida, subtraímos a média de cada valor, elevamos ao quadrado essa diferença e somamos todos os quadrados. Finalmente, dividimos essa soma pelo número de valores menos 1.

    - **Fórmula:** 
        ```python
                    Var(X) = Σ(Xi - μ)² / (n - 1)

                    Var(X): Representa a variância do conjunto de dados.
                    Σ: Símbolo de somatório (soma todas as diferenças ao quadrado).
                    Xi: Cada valor individual do conjunto de dados (20, 25, 30, 35, 40).
                    μ: Média do conjunto de dados (30).
                    n: Número de valores no conjunto de dados (5).
        ```

    - **Interpretação:** Se a variância das idades é alta, as idades são muito diferentes entre si. Alta variância indica que os dados estão mais espalhados ao redor da média.

<br>

- **1.3.5 Desvio Padrão:**

    O desvio padrão é a raiz quadrada da variância. Ele fornece uma medida de dispersão, indicando o quão espalhado os dados estão em torno da média.
    - **Exemplos:**

```python
          Se temos um conjunto de dados 20, 25, 30, 35, 40.
          Desvio Padrão = √62.5 = 7.91 (arredondado para duas casas decimais).
```

- **Como calcular:** Calculamos a raiz quadrada da variância.

    - **Fórmula:** 
        ```python
                    Desvio Padrão = √Variância
        ```

    - **Interpretação:** Um desvio padrão alto indica que os dados estão mais espalhados ao redor da média. Um desvio padrão baixo indica que os dados estão mais concentrados perto da média.

> 💡**Observação:** Não existe um valor absoluto para definir um desvio padrão como "alto" ou "baixo". Depende do contexto e do tipo de dados que você está analisando.

**Aqui estão algumas dicas para determinar se o desvio padrão é alto ou baixo:**

- **Comparar com outros conjuntos de dados:** Se você estiver analisando dados de diferentes grupos ou períodos, compare os desvios padrão. Um desvio padrão significativamente maior que o padrão dos outros conjuntos indica maior dispersão.

- **Comparar com a média:** Calcule a proporção entre o desvio padrão e a média (desvio padrão / média). Uma proporção maior indica maior dispersão em relação à média.

- **Conhecer o tipo de dados:** O desvio padrão "alto" para um tipo de dado pode ser "baixo" para outro. Por exemplo, o desvio padrão de um conjunto de dados de salários de uma empresa pode ser considerado "alto", enquanto o desvio padrão das alturas de uma turma de alunos pode ser considerado "baixo".

- **Analisar o histograma:** Um histograma visualiza a distribuição dos dados. Se o histograma for muito "achatado" (com uma grande dispersão), o desvio padrão provavelmente será alto. Se o histograma for mais "pontudo", o desvio padrão provavelmente será baixo.

- **Usar regras de thumb. Algumas regras de thumb podem ajudar:**

    > - **Desvio padrão > 1.5 * média:** Um desvio padrão que excede 1.5 vezes a média pode ser considerado alto.

    > - **Desvio padrão < 0.5 * média:** Um desvio padrão menor que 0.5 vezes a média pode ser considerado baixo. 

       
### **1.4 Em Resumo:**
                        
    As medidas descritivas fornecem uma visão geral dos dados, revelando sua tendência central e dispersão. A média, mediana e moda indicam o "centro" dos dados, enquanto a variância e o desvio padrão quantificam a dispersão.
                                       
>