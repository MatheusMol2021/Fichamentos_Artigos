# Predição de séries temporais da COVID19: uma avaliação de redes neurais com células LSTM


[Download](https://sbic.org.br/wp-content/uploads/2021/09/pdf/CBIC_2021_paper_72.pdf)


## Referência
```bibtex 1
@article{leiteprediccao,
  title={Predi{\c{c}}{\~a}o de s{\'e}ries temporais da COVID19: uma avalia{\c{c}}{\~a}o de redes neurais com c{\'e}lulas LSTM},
  author={Leite, Saulo Joel Oliveira and El{\'e}trica, Engenharia and de Oliveira, Roberto C{\'e}lio Lim{\~a}o and de Campos, L{\'\i}dio Mauro Lima}
}
```


## Comentário
Em resumo, o artigo reasa do uso da rede neural LSTM com a biblioteca KERAS para predição dos casos confirmados e mortes pela covid-19.

1 - Fundamentação teorica
1.1 LSTM: Long-Short-Term Memory, memoria le longo e curto prazo. é treinado usando "Backpropagation Through Time" para melhorar o problema das redes neurais conencionais que não armazenam informações. De modo que é posível criar grandes redes recorrentes que podem ser usadas para resolver problemas difíceis.

De maneira geral o LSTM possui uma sequencia de blocos que são concenctados pos meio de camadas, de modo que cada porta dentro de um bloco usa as unidades de ativação sigmoide para controlar se elas são disparadas ou não, tornando a mudança de estado e adição de informações que fluem através do bloco condicional.

A LSTM tem a capacidade de remover ou adicionar as informações através de sua estrutura de portas, desta forma, quanto mais bloco maior a possibilidade de aprender com o tempo.
Veja a Equação:
ht = phi(bh + xWx + h(t-1)Wh)
   ht = vetor de estado oculto (vetor de saída do LSTM)
   phi = função de ativação
   Bh e Wh = são os pesos das conexões de entrada

De forma simplificada ema LSTM, as redes neurais recorrentes compartilham parâmetros através do tempo, como se fosse um loop do código. Abaixo temos uma representação em 4 períodos.
 H0 = phi(bh + xWx + XWx)
 H1 = phi(bh + xWx + XWx + h0Wh)
 H2 = phi(bh + xWx + XWx + h1Wh)
 H3 = phi(bh + xWx + XWx + h2Wh)

Por fim, vale ressaltar que não é necessario escrever as equações manualmente, já que existem várias frameworks de Deep Learning, como o tensorflow que realizam as funções matemáticas, com base nos dados recebidos. Na pesquisa foram usados os dados com base em séries temporais.


## Pontos fortes
Utilização de LSTM para séries temporais

## Pontos fracos
é voltado para covid-19.