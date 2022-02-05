# Classification of Arrhythmia in Heartbeat Detection Using Deep Learning

[Download](https://downloads.hindawi.com/journals/cin/2021/2195922.pdf)


# Referencias
```
@article{ullah2021classification,
  title={Classification of arrhythmia in heartbeat detection using deep learning},
  author={Ullah, Wusat and Siddique, Imran and Zulqarnain, Rana Muhammad and Alam, Mohammad Mahtab and Ahmad, Irfan and Raza, Usman Ahmad},
  journal={Computational Intelligence and Neuroscience},
  volume={2021},
  year={2021},
  publisher={Hindawi}
}
```

## Trabalhos correlatos.

O autor utiliza técnicas de aprendizado profundo em conjunto de dados disponíveis publicamente para classificar arritmia. Foi usado dois tipos de conjuntos de dados em seu trabalho de pesquisa. um conjunto de dados é o banco de dados MIT-BIH, com freqências de amostragem de 125Hz com 109446 batimentos de ECG, o segundo foi o banco de ECG Diagnostico PTB, nesses conjuntos de dados os sinais correpondem ao ECG de batimentos cardíacos. A técnicas utilizadas foram CNN, CNN+LSTM e CNN + LSTM + modelo de atenção. 80% dos dados foram separados para treino e os 20% restantes foram utilizados para teste, os resultados obtids com as técnicas foram precisão de 99,12% para o modelo CNN, 99,3% para o CNN e 99,29% para o LSTM+CNN + moldeo de atenção.

Em sua metodologia, antes do uso das técnicas de deep learning, foi separado  um total de 10 arquivos .csv e 3 .pth, o total de dados continha 10505 linhas e 188 colunas, posterioemte foi aplicado GAN  (Generative Adversarial Network) ou rede adversária negativa para gerar sinais dominantes e criar novos dados artificiais para classes com poucos dados e nivelar todas as bases de dados. Após a aplicação dos métodos CNN+LSTM+Modelo de atenção foi obtido grande nível de acurácia na classificação dos sinais. Diante dos genades resultados encontrados, o autor espera que no futuro sua pequisa seja usada em domínios vinvulativos como nuvem, dispositivos móveis e também com tecnologias vestíveis integradas.




#outros tituloos
F. Murat, O. Yildirim, M. Talo, U. B. Baloglu, Y. Demir, and
U. R. Acharya, “Application of deep learning techniques for
heartbeats detection using ECG signals-analysis and review,”
Computers in Biology and Medicine, vol. 120, p. 103726, 2020

## Introdução

'O maior problema de saúde pública são as doenças cardiovasculares. Ataques cardíacos e derrames são responsáveis por quatro em cada cinco mortes por doenças cardiovasculares, as principais são Doença cardíaca coronária, doença cerebrovascular e doença cardíaca reumática. O ECG é um exame não invasivo que registra o estado fisioógico do coração ao longo do tempo, com este método contrações prematuras dos átrios (PAC) ou ventrículos (PVC), fibrilação atrial (FA), infarto do miocárdio (IM) e insuficiência cardíaca congestiva, podem ser diagnóticadas. Por fim, com o advento de novos vestíveis como o Apple Watch, os dados ECG podem ser analisados automaticamente e corretamente.

## Pontos fortes
- 'os fatores saúdaveis levam em consideração o indivíduo adulto e portanto os fatores de diagnóstio se diferem 

- 'Cada anormalidade da frequencia cardíaca normal, inscluindo disturbios de frequencia cardíaca e regularidade ou condução do impulso elétrico cardíaco, é chamado de arritimias.

- 'explorou muitos métodos DL, incluindo CNN, DBN, rede neural recorrente, memória de curto prazo (LSTM) e máquina recorrente bloqueada.
ANN,o julgamento final de desempenho do modelo 
CNN é dependente sobre os pesos da estrutura de rede e preferências do camadas anteriores.

- Monitores cardíacos são os instrumentos que permite que a gravação de ECG seja filtrada. + e Filtro passa-baixo (LPF) é aplicado para eliminar a alta frequência indesejada sinal de ruído. Mbachu et al. [14] introduziu LPF, HPF e Arquitetura BSF com a janela Kaiser, onde esses três os filtros são relacionados em série, processando o sinal dentro do faixa de 0 a 100 Hz e atenuando um sinal de 13 dB para cada filtro na ordem de 200 e com sinais de interferência. Dias et al. [12] introduziu um projeto de filtro digital notch usando o Janela de Hamming, com efeito de interferência de 50 Hz,
resultando em atenuação de 13,4 dB.

- Inclui a recente e revolucionária classificação de dados de aprendizado profundo, sistemas de rede neural profunda para monitores de ECG vestíveis,

- Usamos duas funções, ReLU e Swish, na Figura 10. Unidade linear retificada (ReLU) é uma transferência ou ativação função. Ajuda a rede neural a decidir se para produzir sim ou não mapeando a saída para valores como 10 e 0 ou −10,0 e 10,0, dependendo da função do modelo. Swish é uma função suave não monotônica que regularmente iguala ou excede ReLU em redes profundas em vários
áreas complexas, como classificação de imagem e máquina tradução.

- Materiais e Métodos:
'- - Dataset: foi utilizado o conjunto de dados amostrados do banco de dados de arritmia MITBIH e no ECG Daignósticos PTB. Ambos os bancos de dados tem quantidade de dados o suficiente para testar um rede neural profunda.

'- - Metodologia: foram usados um total de 10 arquivos no formato csv e 3 no formato pth, em u total de 10505 linhas e 188 colunas. de modo que a porcentagem média de dados usados foi de 7,35%, porcentaem de contração de 6,61% e a porcentagem de prematuros atriais é 2,54%.
 Foi usado um treinamento no modelo GAN(Generative Rede Adversária) para separar uma classe ventricular e normal pois a maioria são bastante semelhantes, é isso que o modelo GAN aprendeu a criar.  

'- - Modelo Proposto:
(i) obter informações de atenção do codificador,
(ii) calcular os níveis de atenção.
(iii) calcula a relevância de cada estado do decodificador, e retonna a pontuação do valor escalar.
(iv) foi aplicada uma probabilidade softmax para calcular os pesos de atenção
(v) calcule a média ponderada do codificador de atenção como uma saída por meio dos pesos de atenção.
Deste modo, foi usado duas funções ReLU e Swish.


### Resultados
Atravé de um conjunto de dados aprimorado, foi gerado 3 conjuntos de dados

A precisão do LSTM foi de 99,12%, 
o CNN + LSTM teve precisão média de 99,3%.
o CNN + LSTM + Modelo de atenção teve precisão de 99,29%


###
No futuro espera-se que este estudo esteja voltado para domínios vinculativos como e nuvem e dispositivos móveis. E tambem com tecnologias vestíveis e de baixo consumo de energia.

## Pontos fracos
- A biblioteca do banco de dados de ECG (wfdb) foi usada para o estudo