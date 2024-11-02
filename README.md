Nomes: Lucas Mendes Israel, Gustavo Henrique Costa, Gabriel Kasten

OBS: Caso necessário, rodar os comandos 'pip install scikit-fuzzy', 'pip install scipy', 'pip install networkx', 'pip install numpy', 'pip install scikit-learn' e 'pip install matplotlib' para instalar as bibliotecas necessárias para executar o código.

Para executar cada código, basta digitar o comando 'python nomeDoArquivo.py' no terminal do projeto no VsCode, e inserir os dados solicitados/desejados para efetuar a lógica daquele arquivo.

Comparação das soluções:

1.Análise Comparativa

Precisão:

FIS: O Sistema Fuzzy depende de regras estabelecidas manualmente, o que o torna limitado para generalizar além dos casos previamente definidos. Sua precisão é alta em problemas com regras lógicas bem estabelecidas, mas pode ser restrita em cenários mais dinâmicos.

GF: O Sistema Genético-Fuzzy adapta as regras fuzzy com base em um algoritmo genético, permitindo uma melhor generalização e potencialmente aumentando a precisão em dados variados.

NF: O Sistema Neuro-Fuzzy combina o ajuste dinâmico das regras fuzzy com a capacidade de aprendizado da rede neural, oferecendo uma precisão elevada em situações complexas e com variações nos dados.

Adaptabilidade:

FIS: Possui adaptabilidade limitada, pois depende inteiramente das regras fuzzy, sem capacidade de aprendizado ou ajuste baseado em dados.

GF: Oferece uma maior adaptabilidade devido ao uso do algoritmo genético, que pode otimizar e ajustar regras fuzzy para se adaptar a novas condições.

NF: É o mais adaptável dos três sistemas, pois incorpora a habilidade de aprendizado das redes neurais, ajustando as regras fuzzy com base em um conjunto de dados variado.

Eficiência Computacional:

FIS: Requer menos recursos computacionais e tempo de execução, sendo uma solução mais eficiente para problemas bem definidos com baixa variabilidade.

GF: Mais complexo computacionalmente que o FIS devido ao uso de algoritmos genéticos, podendo exigir mais tempo de processamento para convergir.

NF: Demanda um tempo de execução elevado, principalmente durante o treinamento, devido à combinação dos processos de ajuste fuzzy e aprendizado neural.

2.Vantagens e Desvantagens

Sistema Fuzzy (FIS):

Vantagens: Simplicidade de implementação e eficiência computacional para problemas com regras bem definidas.

Desvantagens: Pouca adaptabilidade e dificuldade em generalizar para condições não previstas pelas regras iniciais.

Sistema Genético-Fuzzy (GF):

Vantagens: Permite uma melhor precisão e adaptabilidade ao ajustar regras fuzzy com base em algoritmos genéticos, sem depender unicamente das regras iniciais.

Desvantagens: Complexidade computacional maior e um tempo de processamento potencialmente longo.

Sistema Neuro-Fuzzy (NF):

Vantagens: Melhor desempenho em situações complexas e adaptativas, pois aprende padrões diretamente dos dados, ajustando as regras fuzzy dinamicamente.

Desvantagens: Exige maior tempo para treinamento e consumo computacional, além de precisar de dados significativos para otimizar seu desempenho.

3.Resumo das comparações observadas

O Sistema Fuzzy é indicado para ambientes estáticos com regras claras, o Sistema Genético-Fuzzy para cenários onde ajustes são necessários, e o Sistema Neuro-Fuzzy para problemas dinâmicos com condições variáveis e dados disponíveis para treinamento. A escolha final do modelo deve considerar as necessidades de precisão, adaptabilidade e os recursos disponíveis para treinamento e execução.
