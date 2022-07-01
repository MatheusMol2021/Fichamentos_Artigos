# A Survey of Heart Anomaly Detection Using Ambulatory Electrocardiogram (ECG)(sensors-20-01461-v2)


[Download](https://www.mdpi.com/1424-8220/20/5/1461)


## Referência
```bibtex 1
@article{li2020survey,
  title={A survey of heart anomaly detection using ambulatory Electrocardiogram (ECG)},
  author={Li, Hongzu and Boulanger, Pierre},
  journal={Sensors},
  volume={20},
  number={5},
  pages={1461},
  year={2020},
  publisher={MDPI}
}
```
ok

# Uma Pesquisa de Detecção de Anomalias Cardíacas Usando Eletrocardiograma Ambulatorial (ECG)

## Abstract
1As doenças cardiovasculares (DCV) são a principal causa de morte no mundo. Um estimado 17,9 milhões de pessoas morrem de DCV a cada ano, representando 31% de todas as mortes globais.

A maioria desses dispositivos podem registrar os dados biométricos de um paciente sinais tanto em repouso como em situações de exercício.
No entanto, lendo a enorme quantidade de matérias-primas sinais de eletrocardiograma (ECG) dos sensores é muito demorado.


1Segundo a Organização Mundial da Saúde (OMS), as doenças cardiovasculares (DCV) são as a primeira causa de morte no mundo. Estima-se que 17,9 milhões de pessoas morram de DCV, representando 31% de todas as mortes globais
1Quatro em cada cinco mortes por DCV são devidas a ataques cardíacos e derrames, e um terço das essas mortes ocorrem prematuramente em pessoas com menos de 70 anos de idade [1].

1Muitos trabalhos de pesquisa, [31,89-93], provaram que usando um modelo específico do paciente, os algoritmos de detecção têm uma precisão maior do que os sistemas tradicionais em casos práticos.

DATASET
Um ECG de doze derivações é a ferramenta padrão de hoje e é usado por cardiologistas para detectar várias anormalidades cardiovasculares.

Um de 12 derivações O ECG tem seis derivações dos membros (I, II, III, aVF, aVL e aVR) e seis derivações torácicas (V1-V6). O padrão
O ECG de 12 derivações é usado como uma ferramenta clínica padrão de análise de arritmia para dor ou desconforto no peito, lesões elétricas, desequilíbrios eletrolíticos, overdose de medicamentos, insuficiência ventricular, acidente vascular cerebral, síncope, e pacientes instáveis. É amplamente utilizado em clínicas e hospitais para diagnóstico de doenças cardíacas [8].

1com o desenvolvimento de novas tecnologias de detecção. ECG portátil dispositivos de gravação como o Apple Watch [3], AliveCor [4], Omron HeartScan [5], QardioMD [6] e, mais recentemente, as Smart Shirt Astroskin [7] estão revolucionando o diagnóstico cardíaco ao medir um atividades cardíacas do paciente 24 horas por dia, 7 dias por semana e transmitindo essas informações para um serviço em nuvem para serem armazenadas e processado remotamente

SINAIS NORMAIS:
Para detectar anomalias nos sinais de ECG, é preciso primeiro saber como é um batimento cardíaco normal. Em [8], um ritmo normal (ver Figura 1) é definido como o resultado de um impulso elétrico que inicia do nó sinoatrial (SA), propaga-se pelos músculos cardíacos e depois para o tórax do paciente. Um ritmo normal é composto pelos seguintes segmentos em sequência: uma onda P gerada pelo despolarização, o complexo QRS gerado pela despolarização ventricular e uma onda T e U onda gerada pela repolarização ventricular. Em sinais normais de ECG, a onda P, complexo QRS, e a onda T deve ser semelhante ao longo do tempo em uma frequência que varia de 60 a 100 bpm

a variação entre o PP mais curto intervalo/intervalo RR e o intervalo PP/intervalo RR mais longo deve ser inferior a 0,04 s (consulte a Figura 2)

SINAIS ANORMAIS:
As anomalias nos sinais de ECG podem ser categorizadas em três subconjuntos: frequência cardíaca irregular, ritmo e ritmo ectópico. A frequência cardíaca pode ser contada medindo-se os intervalos PP/RR no ECG. Se o intervalo PP/RR for longo, isso indica uma frequência cardíaca baixa, caso contrário, indica uma frequência cardíaca alta avaliar. Se as pulsações começam no nó SA, mas os intervalos PP/RR são maiores que 1 s, isso pode indicar bradicardia sinusal (Figura 3a), que indica que o coração está bombeando muito devagar. Quando o PP/RR intervalos menores que 0,6 s, pode ser sinal de Taquicardia Sinusal (Figura 3b). Além disso, se o variações entre os intervalos PP/RR são muito grandes, isso pode indicar Arritmia Sinusal, Bloqueio Sinusal,

Detecção de anomalias
O objetivo de detectar anomalias nos sinais de ECG consiste em encontrar as frequências cardíacas irregulares,
batimentos cardíacos e ritmos.

Além disso, o sistema examina toda a gravação para detectar quaisquer segmentos de ritmo irregulares, como um R-R inconsistente
intervalo e ritmos ectópicos. Portanto, um sistema de detecção de anomalias é composto por cinco subsistemas: remoção de ruído (Seção 3.2), detecção de batimentos cardíacos (Seção 3.3), segmentação de batimentos cardíacos (Seção 3.3), classificação de batimentos cardíacos (Seção 3.4) e classificação de ritmo (Seção 3.5).

A detecção de batimentos cardíacos visa encontrar a localização dos batimentos cardíacos para calcular a frequencia cardíaca.

Todas as pesquisas selecionadas nesta revisão utilizaram a base de dados do MIT-BIH, que permite testar e comparar
o desempenho dos algoritmos.

REMOÇÃO DE RUÍDO
Portanto, a remoção de ruído é um passo necessário para detecção de anomalias em ECGs ambulatoriais. Existem dois grupos principais de artefatos: artefatos não fisiológicos e fisiológicos. O primeiro é causado por problemas de equipamento, como interferência na linha de energia, e o outro é causado por músculo atividades, interferência da pele ou movimento do corpo,


DETECÇÃO E SEGMENTAÇÃO DE BATIMENTOS CARDÍACOS
A detecção de batimentos cardíacos geralmente está relacionada à detecção de uma frequência cardíaca irregular e
RR-intervalos, que são explicados na Seção 2. A detecção de batimentos cardíacos também é o passo chave para extrair o batimentos cardíacos do sinal de ECG a ser usado para classificação.

ponto inicial (no local) da onda P ao seu ponto final (fora do local) da onda T.
No entanto, a onda P e a onda T podem não ser detectáveis em certos tipos de batimentos cardíacos anormais,
e o complexo QRS é a forma de onda mais óbvia. Assim, a localização do complexo QRS é frequentemente
usado para localizar a origem do batimento cardíaco;

Para detectar o complexo QRS, foi definido um limiar para selecionar os picos que possuem grande amplitude. No pré-processamento
estágio de seu algoritmo, um filtro passa-banda é aplicado ao sinal bruto de ECG para remover a linha de base vaguear e ruído de alta frequência. Depois disso, um diferenciador e normalizador é aplicado à limpeza sinal para destacar os componentes do complexo QRS.

usa-se a transformada wavelet e limiar adaptativo para detectar a localização do complexo QRS e dar uma
estimativa das localizações das ondas P e T [69].

MODELO DE TREINAMENTO
Existem vários métodos que provaram ser válidos paraidentificando os tipos de batimentos cardíacos. Eles são clustering, machine learning tradicional e deep classificação de aprendizagem.

muitos modelos foram implementados para classificação como K-mean clustering,
Outro método importante são os algoritmos tradicionais de classificação de aprendizado de máquina: Kth vizinho mais próximo (KNN), Análise Discriminante Linear (LDA), Funções Discriminantes Quadráticas (QDF), Suporte Vector Machine (SVM) e rede neural perceptron multicamada (MLPNN).

A maioria dos pesquisadores tem usado métodos tradicionais para resolver o problema. Máquina tradicional métodos de classificação de aprendizado não requerem uma quantidade considerável de dados de treinamento,

3.1 um modelo de aprendizado profundo precisa de muitos dados rotulados para treinamento. Felizmente, conjuntos de dados públicos podem ser facilmente encontrados na Internet. Portanto, muitos estudos usando vários arquitetura de aprendizado profundo publicaram novos algoritmos para classificar batimentos cardíacos


Chauhan e Vig desenvolveram um algoritmo preditivo que pode detectar normal, PVC, PAC,
batimentos cardíacos compassados ​​por meio de uma rede neural profunda LSTM (memória de longo prazo) (Figura 16). Em seu
algoritmo, a etapa de extração/seleção de recursos é negligenciada, dados brutos de ECG e rótulos correspondentes
são usados ​​como entradas para a rede neural LSTM empilhada (duas camadas).

No experimento, eles dividiram o banco de dados MIT-BIH em quatro conjuntos: um conjunto de treinamento não anômalo (SN), validação não anômala set (VN), mistura de conjuntos de validação normal e anormal (SN+A) e os conjuntos de teste (tN+A). A rede LSTM foi treinada em SN e usou VN para parada antecipada. A rede LSTM treinada foi então aplicado a SN+A para encontrar o limiar para detectar batimentos cardíacos anormais. Por fim, o escolhido O limiar foi usado em tN+A para discriminar batimentos cardíacos regulares e anômalos durante a previsão [79]. O modelo apresentado foi capaz de atingir uma precisão de 97,5% com um recall de 46,47% no conjunto de teste (tN+A).

Os segmentos de batimentos cardíacos brutos foram submetidos a uma rede neural convolucional adaptativa 1-D (CNN) para reconhecimento de padrões. A rede neural convolucional 1-D atuou como uma ferramenta de extração de recursos, bem como uma ferramenta de classificação.

A próxima geração de algoritmos de detecção de anomalias cardíacas deve ser capaz de lidar com medições de saúde aproveitando várias medições sincronizadas de: acelerômetro, pressão arterial em tempo real (com base no tempo de trânsito do pulso), temperatura da pele e tórax superior e inferior sensores respiratórios.

Isso pode ser feito usando LSTM avançado e redes neurais recorrentes (RNN).
As medições de sinal (PPG) e acelerômetro foram combinadas usando um LSTM e RNN para calcular em movimento em tempo real da pressão arterial compensada.