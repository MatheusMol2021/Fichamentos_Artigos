# Heartbeat_Anomaly_Detection_using_Adversarial_Oversampling

## Detecção de Anomalias de Pulsação usando Amostragem Adversarial

## Abstract

As doenças cardiovasculares são uma das maiorescausas de morte no mundo. 

Prevenção e a detecção precoce é a melhor estratégiapara reduzir este fato. 

Diferentes abordagens de aprendizado de máquina para diagnósticos automáticos estão sendo propostos para esta tarefa.

Como na maioria problemas de saúde, o desequilíbrio entre exemplos e classes é predominante neste problema e afeta o desempenho da solução automatizada.

O artigo trata a classificação de imagens de diferentes doenças cardiovasculares, será proposto uma rede neural convulacional bidimensional para classificalçai,

e depois iremos utilizar a arquitetura infogan para gerar novas imagens sintéticas. O resultado mostra que a sobreamostrgem melhora o desempenho de um classificador.


Cardíaco a arritmia consiste em distúrbios que alteram a frequência cardíaca, constituindo um grave problema de saúde pública

O eletrocardiograma (ECG) é o processo de registro da atividade elétrica do coração ao longo de algum tempo usando eletrodos.
O ECG auxilia no diagnóstico de arritimias cardíacas, pois alem de ser não-invasivo, Epossui altas taxas de erro das abordagens computadorizadas.

Detectar arritmias é uma tarefa difícil devido à variabilidade na onda morfologia entre os pacientes, bem como a presença de ruído.

A maioria das abordagens para classificação de arritmias faz uso a extração de caractéristicas. 
Isso requer conheciento prévio e específico sobre as características que são importantes para representar um determinado batimento cardíaco. Uma estratégia eria tomar batidas anormais em pontos cruciais analisando a recorrencia ao longo do segmento ECG.
As Redes neurais convulacionais (CNN) foram usados para resolver este problema.

O grande problema em uma base de dados envolvendo saúde, seria o alto grau de desequlíbrio, uma vez que muitos sistemas de aprendizagem não são usados para dados desbalanceados, isso ocorre porque as redes neurais geralmente alcançarão maior precisão para as classes majoritárias e uma precisão inceitável para uma classe minortária.
Ocorre porque os pesos serão ajustados para as classes mintoritárias.

Existem algumas técnicas para aumentar a quantidade de minoria de amostras:
- repetir aletoriamente
- selecionar amostras
- gerar amostras extras, incluindo ruídos
- InfoGan

O banco Mit-Bih foi usado com um treinamento CNN

No final da rede, usou uma camada Softmax para fornecer a saída como probabilidades de cada classe de batimentos cardíacos. Usamos o otimizador Adam [17] com o parâmetros padrão e interrompeu o treinamento quando a perda no conjunto de validação parou para diminuir.

O treinamento da CNN consistiu em 20 épocas e uma parada antecipada se a perda no conjunto de validação não diminuiu considerando a época anterior. Os experimentos foram repetidos dez vezes, onde 20% dos dados foram usados como o conjunto de teste, 10% como o
conjunto de validação e 70% para treinamento.

Para classificação bidimensional e por imagem as redes convulocionais funcionam muito bem,