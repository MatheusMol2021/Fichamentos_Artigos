# Predição de séries temporais da COVID19: uma avaliação de redes neurais com células LSTM


[Download](https://sbic.org.br/wp-content/uploads/2021/09/pdf/CBIC_2021_paper_72.pdf)


## Referência
```bibtex 1
@article{leiteprediccao,
  title={Predi{\c{c}}{\~a}o de s{\'e}ries temporais da COVID19: uma avalia{\c{c}}{\~a}o de redes neurais com c{\'e}lulas LSTM},
  author={Leite, Saulo Joel Oliveira and El{\'e}trica, Engenharia and de Oliveira, Roberto C{\'e}lio Lim{\~a}o and de Campos, L{\'\i}dio Mauro Lima}
}
```
## Trabalhos correlatos

''O autor também utiliza em sua pesquisa as redes neurais do tipo Long Short-term LSTM para predição de séries temporais para doenças como a covid-19, tambem com uma basae de dados de domínio público, foi o escolhido pois a LSTM por conseguir aprender séries temporais que longas sequencias de observações no domínio do tempo

'###Etapa 1 - preparação dos dados.
O primeiro passo de sua metodologia consistia na preparação dos dados, sua base de dados possuia as quantidade diárias de casos confirmados de COVID-19 entre o período de 2020 e 2021. Através de uma função de regressão foi possível converter uma única coluna de dados em duas outras colunas, a primeira coluna contendo a contagem de dias e a segunda contendo a quantidade de dados confirmados

'###Etapa 2 - Desenvolvimento da rede neural Long Short-Term Memory.
Depois de  modelar os dados para avaliação do método utilizado, foi divido os dados em conjuntos de treino e teste, 67% do total de dados adquirido  foi separado para o treinar o modelo e 33% para testes. o modelo descrito foi implementado usando 200 épocas.

'###Etapa 3 - Hiperparametros da rede neural LSTM e método de avaliação de semplenho.
Foi utilizado um otimizadosr "Adam", que se se baseia  em estimativa adaptativa de momentos de primeira e segunda ordem, 
além do otimizador um importante parãmetro foi o "dropout" que consegue reduzir o sobre-ajuste em redes neurais artificias para melhorar a eficiência do sistema.
o método de avaliação de desempenho para o LSTM foi o erro mério quadrático, que tem o objetivo de encontrar a diferenlça média  de um valor e seu parâmetro inicial, seu uso é destinado a compreender um "erro de previsão, quanto menor for erro quadrático melhor será a previsão.

'###Etapa 4 - Grade de busca
Para decidir o melhor resultado obtido pelo modelo, foi feita uma árvore de
O autor testou diferente cobinações em 200 épocas
sua eficiência  foi em cerca de 99% do modelo proposto

'o objetivo do presente trabalho foi apresentar o modelo de redes neurais LSTM, com o  foco na predição de séries temporais em casos confirmados de covid, seu modelo conseguiu atingir o objetivo final em predizer dados da panademia em países como Brasil, Ìndia e China, 


seu modelo obteve bons resultados na área de predição de dados





## Introduão
'No artigo publicado, após a Covid-19 alcançar o posto de uma das maiores pandemias do mundo por levar em conta uma taxa de mortalidade considerável, a tecncologia se tornou um pilar importante no combate ao coronavírus, segundo a IBM  43% dos profissionais de TI que trabalham com Inteligencia Artificial aceleraram a implementação da IA devido ao Covid-19. Desta forma, nota-se que a grande necessidade de pesquinsas na área de predição de dados.

## Comentário
'Em resumo, o artigo reasa do uso da rede neural LSTM com a biblioteca KERAS para predição dos casos confirmados e mortes pela covid-19.'

1 - Fundamentação teorica
'1.1 LSTM: Long-Short-Term Memory, memoria le longo e curto prazo. é treinado usando "Backpropagation Through Time" para melhorar o problema das redes neurais covencionais que não armazenam informações. De modo que é posível criar grandes redes recorrentes que podem ser usadas para resolver problemas difíceis.

'De maneira geral o LSTM possui uma sequencia de blocos que são concenctados pos meio de camadas, de modo que cada porta dentro de um bloco usa as unidades de ativação sigmoide para controlar se elas são disparadas ou não, tornando a mudança de estado e adição de informações que fluem através do bloco condicional.

'A LSTM tem a capacidade de remover ou adicionar as informações através de sua estrutura de portas, desta forma, quanto mais bloco maior a possibilidade de aprender com o tempo.
Veja a Equação:
ht = phi(bh + xWx + h(t-1)Wh)
   ht = vetor de estado oculto (vetor de saída do LSTM)
   phi = função de ativação
   Bh e Wh = são os pesos das conexões de entrada

'De forma simplificada ema LSTM, as redes neurais recorrentes compartilham parâmetros através do tempo, como se fosse um loop do código. Abaixo temos uma representação em 4 períodos.
 H0 = phi(bh + xWx + XWx)
 H1 = phi(bh + xWx + XWx + h0Wh)
 H2 = phi(bh + xWx + XWx + h1Wh)
 H3 = phi(bh + xWx + XWx + h2Wh)

'Por fim, vale ressaltar que não é necessario escrever as equações manualmente, já que existem várias frameworks de Deep Learning, como o tensorflow que realizam as funções matemáticas, com base nos dados recebidos. Na pesquisa foram usados os dados com base em séries temporais.


## Pontos fortes
Utilização de LSTM para séries temporais

## Pontos fracos
é voltado para covid-19.