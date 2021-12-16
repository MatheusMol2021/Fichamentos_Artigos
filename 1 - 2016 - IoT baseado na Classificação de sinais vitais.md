
# IoT Based Classification of Vital Signs Data for Chronic Disease Monitoring

[Download](https://sci-hub.se/https://doi.org/10.1109/ISCO.2016.7727048)


## Referência
''' bibtex
@inproceedings{raji2016iot,
  title={IoT based classification of vital signs data for chronic disease monitoring},
  author={Raji, A and Jeyasheeli, P Golda and Jenitha, T},
  booktitle={2016 10th International Conference on Intelligent Systems and Control (ISCO)},
  pages={1--5},
  year={2016},
  organization={IEEE}
}
'''

## Resumo



## Comentários

- Na ìndia a pricipal causa de morte são as doenças crônicas(diabetes, derrame, doenças cardiovasculares, doenças de saúde mental, cãncer e doenças pulmonares) para estes pacientes é fundamental que tenham um monitoramento contínuo dos sinais, uma vez que o número de enfermeira é relativamente baixo. o sistema recebe na forma de documento de texto seus parâmetros que informam sua saúde e deste modo os pacientes conseguem ser diagnosticados em tempo hábil e melhoram sua qualidade de vida

- Na tentativa de melhorar o sistema de saúde passou a ser monitorado os principais sinais vitais, eles incluem: Medição de temperatura, frequência respiratória, pulso, pressão sanguínea e saturação de oxigênio no sangue. Deste modo, pode-se identificar qualquer problema médico, doença ou estresse fisiológico.

- Cada doença apresenta uma ténica de mineração de dados diferente como Naïve Bayes e Support Vector Machine, para doenças renais foi utilizado o algoritmo SVM.

- No artigo foram aplicadas técnicas de Bigdata, como Hadoop, HDFS, Storm e Oozie e sua análise de dados é feita por mineração de dados. Uma outra abordagem considerou 9 condições clínicas para diagnosticar insuficiência respiratória, considerando apenas 3 medições fisiológicas (frequência cardíaca, pressão arterial e taxa de respiração.

![Figura 1 - Aquisição de dados](C:\Users\Usuário\Documents\Figuras\Figura1.png)

- Processamento de dados: Os sinais vitais variam de acordo com o dia e a hora e além disso os sensores podem ser afetados por diferentes fatores ambientais.

 1. Algoritmo Naive: Os objetos são classificados com base no modelo probabilístico, nesse algoritmo o maior valor de hipótese para classificar os objetos.

 2. Algoritmo J48: Gera uma árvore de decisão para cada conjunto de dados, a participação que tem maior ganho de informação é selecionada como mehor atributo que classifique os dados.


## Pontos fracos:

- o uso de mineração de dados exclui a necess7idade de aprendizagem de máquina para receber os dados de cada paciente.