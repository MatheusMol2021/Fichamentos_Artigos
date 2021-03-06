# Online anomaly detection for long-term ECG monitoring using wearable devices (1-s2.0-S0031320318304102-main)


[Download](https://www.sciencedirect.com/science/article/abs/pii/S0031320318304102)


## Referência
```bibtex 1
@article{carrera2019online,
  title={Online anomaly detection for long-term ECG monitoring using wearable devices},
  author={Carrera, Diego and Rossi, Beatrice and Fragneto, Pasqualina and Boracchi, Giacomo},
  journal={Pattern Recognition},
  volume={88},
  pages={482--492},
  year={2019},
  publisher={Elsevier}
}
```
1.2

### Abstract
Ainda existem alguns desafios para embregar estes algoritmos em sistemas vestíveis, para permitir assim o monitoramento.

A morfologia dos batimentos cardíacos mudam conforme a frequencia cardíaca, por isso os modelos aprendidos devem ser ajustados para analisar o sinais ECG tambem para atividades cotidianas

Foi porposto então utilizar o ECG para modelar os batimentos cardíacos, onde qualquer não conformidade é definido como anômalos.

Foi utilizado variações de frequencia cardíaca através de transformações lineares por meio de sinais de ECG, 

### Introdução
O monitoramento da saúde e do ECG atraíram a atenção no literatura de reconhecimento de padrões e aprendizado de  máquina e algoritmos para apoiar a anotação manual de sinais  e ECG foram amplamente pesquisado para aliviar esta operação cara e demorada.

Muitos algoritmos de classificação de batimentos cardíacos foram propostos. e alguns produtos comerciais já estão disponíveis.

Muitas vezes os médicos empregam estas técnicas para destacar segmentos relevantes na  análise de longos sinais ECG

A proxima etapa é usar estas tecnologias em dispositivos de sensoriamento, e os vestíveis tem enorme potencial neste cenário.

No entanto seu uso na vida real não é simples, pois temos alguns desafios a ser implementaods.

A maioria dos algoritmos são aprendidos com base em cada usuário específico, uma vez que cada ususário apresenta uma morofologia muito específico.

Portanto a análise de classificação deve ser considerado através de um aprendizado não supervisionado, sem requerir do médico batimentos anôma-los.

1.2 A morfologia  dos batimentos cardíacos muda quando a frequencia cardíaca aumenta, 

portanto quando o usuário está em repouso não podemos descrever adequadamente os batimentos cardíacos. Portanto aprender um modelo para cada frequencia não é viável. Para evitar a drgradação do desempenho, os modelos específicos devem ser adaptados para a variação da frequencia cardíaca.

Poucos minutos de ECG são são suficientes para aprender um dicionário específico do usuário.
Para reportar qualquer batimento cardíaco anôma-lo foi porposto um algoritmo para calcular a distancia do batimento cardíaco e a união de espaços, as anomalias são detectadas por limiares dessa distancia reportanto quanquer batimento cardíaco que não está conforme as condições de descanso do usuário.

Foi utilizado o aprendizado de tranferência transdutiva, onde após a variação da frequencia cardíaca

### Trabalhos correlatos
A tecnologia de detecção de anomalias não estão embutidos nos equipamentos vestíveis,

que exploram características morfológicas artesanais que imitam os critérios usados pelos médicos para analisar sinais de ECG. 

1.1Exemplos típicos de características são o intervalo RR, ou seja, a distância entre dois picos R consecutivos, a amplitude e a largura do complexo QRS, bem como descritores de forma para as formas de onda locais como P-wave, T-wave e ST-segment (ver Fig. 1).  Outras características podem ser extraídas do vetor cardiograma [25], computado através de uma transformação linear dos 12 leads ECG, ou no domínio wavelet [1] ou através da transformação hermita [12].

* A rede neural convulacional CNN atinfe precisão de 98,6% em 24 gravações do MIT-BIH. A LSTM consegue detectar anomalias onde o sistema é desconhecido. 

* Como falado anteriormente para analisar o monitoramento de ECG a longo prazo, é necessario a criação de um modelo a partir de dados rotulados com variaçõesde frequencia cardíaca, ou seja o modelo aprendido no domínio de origem é transformado para operar com outras variáveis.
O objetivo é aprender atravé de dados rotulados no dominio de origem um classificador para um domíni alvo posivelmente não supervisionado.
É mais recomendável  consultar métodos de adaptação no dmínio de tranferencia indutiva.

* Ver figura 1

* poucosinutos são necesários para aprender um dicionário de batimentos cardíacos.

* A figura 2 apresenta um modo de alteração de limiar para cada usuário.

No trabalho foram considerados 5 datasets, (LTSTDB, LTAFDB, LTDB,EB, MIT-BIH) da Physionet,
todos os conjuntos foram anotados manualmente por uma ferramenta corrigida por cardiologistas,
O Conjunto MIT-BIJ contem apenas sinais ECG que não apresentam variabilidade de frequencia cardíaca, o que o torna mais apropriado para detecção de anomalias.

O conjunto de dados BioBit Move(B2B), contem 15 linhsa de senais ECG sendo 12 de usuáriossaudaveis e 3 por usuários acomentidos por aluma doença cardovaascular, onde cada dado tem um intervalo de pelo menos 1h e é adquirido para atividades da vida normal por exemplo, descansar, deitar, caminhar. Assim a frequencia cardíaca varia significativamente.
Restringimos esntão nossa análise a btimentos mais frequentes, ou seja, (70,80,90,100).

O conjunto dedados são muito diferentes dos conjuntos de dados da Physionet, batimentos cardíacos de baixa qualidade foram descartados por um sistema automático e a supervisão de um cardiologista.

para avaliar os dicionarios adaptados de modelagem foi utilizado a taxa de verdadeiro positivo(TPR) e frequencia de falso positivo(FPR)

