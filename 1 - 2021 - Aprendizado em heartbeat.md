# Classification of Arrhythmia in Heartbeat Detection Using Deep Learning

[Download](https://downloads.hindawi.com/journals/cin/2021/2195922.pdf)


# Referencias

```

## Pontos fortes
- os fatores saúdaveis levam em consideração o indivíduo adulto e portanto os fatores de diagnóstio se diferem 

- Cada anormalidade da frequencia cardíaca normal, inscluindo disturbios de frequencia cardíaca e regularidade ou condução do impulso elétrico cardíaco, é chamado de arritimias.

- explorou muitos métodos DL, incluindo CNN, DBN, rede neural recorrente, memória de curto prazo (LSTM) e máquina recorrente bloqueada.
ANN,o julgamento final de desempenho do modelo 
CNN é dependente sobre os pesos da estrutura de rede e preferências do camadas anteriores.

- Monitores cardíacos são os instrumentos que permite que a gravação de ECG seja filtrada. + e Filtro passa-baixo (LPF) é aplicado para eliminar a alta frequência indesejada sinal de ruído. Mbachu et al. [14] introduziu LPF, HPF e Arquitetura BSF com a janela Kaiser, onde esses três os filtros são relacionados em série, processando o sinal dentro do faixa de 0 a 100 Hz e atenuando um sinal de 13 dB para cada filtro na ordem de 200 e com sinais de interferência. Dias et al. [12] introduziu um projeto de filtro digital notch usando o Janela de Hamming, com efeito de interferência de 50 Hz,
resultando em atenuação de 13,4 dB.

- Inclui a recente e revolucionária classificação de dados de aprendizado profundo, sistemas de rede neural profunda para monitores de ECG vestíveis,

- Usamos duas funções, ReLU e Swish, na Figura 10. Unidade linear retificada (ReLU) é uma transferência ou ativação função. Ajuda a rede neural a decidir se para produzir sim ou não mapeando a saída para valores como 10 e 0 ou −10,0 e 10,0, dependendo da função do modelo. Swish é uma função suave não monotônica que regularmente iguala ou excede ReLU em redes profundas em vários
áreas complexas, como classificação de imagem e máquina tradução.

- Materiais e Métodos:
- - Dataset: foi utilizado o conjunto de dados amostrados do banco de dados de arritmia MITBIH e no ECG Daignósticos PTB. Ambos os bancos de dados tem quantidade de dados o suficiente para testar um rede neural profunda.

- - Metodologia: foram usados um total de 10 arquivos no formato csv e 3 no formato pth, em u total de 10505 linhas e 188 colunas. de modo que a porcentagem média de dados usados foi de 7,35%, porcentaem de contração de 6,61% e a porcentagem de prematuros atriais é 2,54%.
 Foi usado um treinamento no modelo GAN(Generative Rede Adversária) para separar uma classe ventricular e normal pois a maioria são bastante semelhantes, é isso que o modelo GAN aprendeu a criar.  

- - Modelo Proposto:
(i) obter informações de atenção do codificador,
(ii) calcular os níveis de atenção.
(iii) calcula a relevância de cada estado do decodificador, e retonna a pontuação do valor escalar.
(iv) foi aplicada uma probabilidade softmax para calcular os pesos de atenção
(v) calcule a média ponderada do codificador de atenção como uma saída por meio dos pesos de atenção.
Deste modo, foi usado duas funções ReLU e Swish.


### Resultados
Após o uso do conjunto de dados aprimorado, e 3 conjuntos gerados são um modelo inicial com o conjunto de dados original,  


## Pontos fracos
- A biblioteca do banco de dados de ECG (wfdb) foi usada para o estudo