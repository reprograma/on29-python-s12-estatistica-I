<h1 align="center">
  <img src="assets/reprograma-fundos-claros.png" alt="logo reprograma" width="500">
</h1>

<h1 align="center">  Estatística com Python: Probabilidade e Amostragem 📊 </h1>
<h3 align="center">  Turma ON29 | Python | Semana 12 | 2024 | Professora Camila Ribeiro  </h3>

<br>

### Instruções

Antes de começar, vamos organizar nosso setup.


    1. Fork esse repositório

    2. Clone o fork na sua máquina (Para isso basta abrir o seu terminal e digitar `git clone url-do-seu-repositorio-forkado`)

    3. Entre na pasta do seu repositório (Para isso basta abrir o seu terminal e digitar `cd nome-do-seu-repositorio-forkado`)


<br>

---

# Índice

- [1. Introdução à Estatística](capitulos/1-introducao-a-estatistica.md)
    - [1.1 Estatística: Definição e Importância](capitulos/1-introducao-a-estatistica.md#11-estatistica-definicao-e-importancia)
        - [1.1.1 Importância de Estudar Estatística](capitulos/1-introducao-a-estatistica.md#111-importancia-de-estudar-estatistica)
        - [1.1.2 Vantagens de Estudar Estatística](capitulos/1-introducao-a-estatistica.md#112-vantagens-de-estudar-estatistica)
        - [1.1.3 Desvantagens de Estudar Estatística](capitulos/1-introducao-a-estatistica.md#113-desvantagens-de-estudar-estatistica)
        - [1.1.4 Preconceitos](capitulos/1-introducao-a-estatistica.md#114-preconceitos)
        - [1.1.5 Estatística em Tecnologia](capitulos/1-introducao-a-estatistica.md#115-estatistica-em-tecnologia)
    - [1.2 Tipos de Dados](capitulos/1-introducao-a-estatistica.md#12-tipos-de-dados)
        - [1.2.1 Dados Qualitativos (Categóricos)](capitulos/1-introducao-a-estatistica.md#121-dados-qualitativos-categoricos)
        - [1.2.2 Dados Quantitativos (Numéricos)](capitulos/1-introducao-a-estatistica.md#122-dados-quantitativos-numericos)
            - [1.2.2.1 Dados Quantitativos Discretos](capitulos/1-introducao-a-estatistica.md#1221-dados-quantitativos-discretos)
            - [1.2.2.2 Dados Quantitativos Contínuos](capitulos/1-introducao-a-estatistica.md#1222-dados-quantitativos-continuos)
    - [1.3 Medidas Descritivas](capitulos/1-introducao-a-estatistica.md#13-medidas-descritivas)
        - [1.3.1 Média](capitulos/1-introducao-a-estatistica.md#131-media)
        - [1.3.2 Mediana](capitulos/1-introducao-a-estatistica.md#132-mediana)
        - [1.3.3 Moda](capitulos/1-introducao-a-estatistica.md#133-moda)
        - [1.3.4 Variância](capitulos/1-introducao-a-estatistica.md#134-variancia)
        - [1.3.5 Desvio Padrão](capitulos/1-introducao-a-estatistica.md#135-desvio-padrao)
    - [1.4 Em Resumo](capitulos/1-introducao-a-estatistica.md#14-em-resumo)
- [2. Python para Estatística](capitulos/2-python-para-estatistica.md)
    - [2.1 Instalação e Configuração do Ambiente Python](capitulos/2-python-para-estatistica.md#21-instalacao-e-configuracao-do-ambiente-python)
    - [2.2 Bibliotecas Essenciais](capitulos/2-python-para-estatistica.md#22-bibliotecas-essenciais)
        - [2.2.1 NumPy](capitulos/2-python-para-estatistica.md#221-numpy)
        - [2.2.2 Pandas](capitulos/2-python-para-estatistica.md#222-pandas)
    - [2.3 Demonstração Prática de Manipulação de Dados com NumPy e Pandas](capitulos/2-python-para-estatistica.md#23-demonstracao-pratica-de-manipulacao-de-dados-com-numpy-e-pandas)
    - [2.4 Em Resumo](capitulos/2-python-para-estatistica.md#24-em-resumo)
- [3. Probabilidade](capitulos/3-probabilidade.md)
    - [3.1 Definição de Probabilidade e Eventos](capitulos/3-probabilidade.md#31-definicao-de-probabilidade-e-eventos)
    - [3.2 Espaço Amostral](capitulos/3-probabilidade.md#32-espaco-amostral)
    - [3.3 Tipos de Probabilidade](capitulos/3-probabilidade.md#33-tipos-de-probabilidade)
        - [3.3.1 Probabilidade Clássica](capitulos/3-probabilidade.md#331-probabilidade-classica)
        - [3.3.2 Probabilidade Frequentista](capitulos/3-probabilidade.md#332-probabilidade-frequentista)
        - [3.3.3 Probabilidade Subjetiva](capitulos/3-probabilidade.md#333-probabilidade-subjetiva)
    - [3.4 Regras de Probabilidade](capitulos/3-probabilidade.md#34-regras-de-probabilidade)
        - [3.4.1 Regra da Soma](capitulos/3-probabilidade.md#341-regra-da-soma)
        - [3.4.2 Regra da Multiplicação](capitulos/3-probabilidade.md#342-regra-da-multiplicacao)
        - [3.4.3 Probabilidade Condicional](capitulos/3-probabilidade.md#343-probabilidade-condicional)
- [4. Probabilidade com Python](capitulos/4-probabilidade-com-python.md)
    - [4.1 Simulação de Eventos Aleatórios com Python](capitulos/4-probabilidade-com-python.md#41-simulacao-de-eventos-aleatorios-com-python)
    - [4.2 Cálculo de Probabilidade com Funções da Biblioteca NumPy](capitulos/4-probabilidade-com-python.md#42-calculo-de-probabilidade-com-funcoes-da-biblioteca-numpy)
    - [4.3 Criação de Gráficos de Probabilidade com Matplotlib](capitulos/4-probabilidade-com-python.md#43-criacao-de-graficos-de-probabilidade-com-matplotlib)
- [5. Amostragem](capitulos/5-amostragem.md)
    - [5.1 Métodos de Amostragem](capitulos/5-amostragem.md#51-metodos-de-amostragem)
        - [5.1.1 Amostragem Aleatória Simples](capitulos/5-amostragem.md#511-amostragem-aleatoria-simples)
        - [5.1.2 Amostragem Estratificada](capitulos/5-amostragem.md#512-amostragem-estratificada)
        - [5.1.3 Amostragem por Conglomerados](capitulos/5-amostragem.md#513-amostragem-por-conglomerados)
        - [5.1.4 Amostragem Sistemática](capitulos/5-amostragem.md#514-amostragem-sistematica)
        - [5.1.5 Erros Amostrais e Intervalos de Confiança](capitulos/5-amostragem.md#515-erros-amostrais-e-intervalos-de-confianca)
- [6. Amostragem com Python](capitulos/6-amostragem-com-python.md)
    - [6.1 Implementação de Métodos de Amostragem com Pandas e NumPy](capitulos/6-amostragem-com-python.md#61-implementacao-de-metodos-de-amostragem-com-pandas-e-numpy)
    - [6.2 Cálculo de Estatísticas Descritivas e Intervalos de Confiança](capitulos/6-amostragem-com-python.md#62-calculo-de-estatisticas-descritivas-e-intervalos-de-confianca)
    - [6.3 Visualização de Dados com Matplotlib](capitulos/6-amostragem-com-python.md#6.3-visualizacao-de-dados-com-matplotlib)

---

### 🔗 Links Úteis

1. **[Doc Numpy](https://numpy-org.translate.goog/devdocs/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc)** :  A base para cálculos numéricos com arrays multidimensionais, fornecendo funções para média, mediana, moda, variância e desvio padrão.
2. **[Doc Pandas](https://pandas-pydata-org.translate.goog/docs/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc)** : Permite manipular e analisar dados estruturados em forma tabular, facilitando cálculos e visualização.
3. **[Doc Matplotlib](https://matplotlib-org.translate.goog/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc)** : A biblioteca principal para criar gráficos, como histogramas.
4. **[Doc Random](https://docs.python.org/pt-br/3/library/random.html)** : Usada para gerar números aleatórios e simular eventos aleatórios, como o lançamento de uma moeda.
5. **[Doc Scipy.stats](https://docs-scipy-org.translate.goog/doc/scipy/reference/stats.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=sc)** : Usada para cálculos estatísticos mais avançados, incluindo a função mode() para encontrar a moda e o cálculo de intervalos de confiança.


<br>


<p align="center">
Desenvolvido com :purple_heart:  
</p>
