# A 12-lead electrocardiogram database for arrhythmia research covering more than 10,000 patients (s41597-020-0386-x)


[Download](https://www.nature.com/articles/s41597-020-0386-x)


## Referência
```bibtex 1
@article{zheng202012,
  title={A 12-lead electrocardiogram database for arrhythmia research covering more than 10,000 patients},
  author={Zheng, Jianwei and Zhang, Jianming and Danioko, Sidy and Yao, Hai and Guo, Hangyuan and Rakovski, Cyril},
  journal={Scientific data},
  volume={7},
  number={1},
  pages={1--8},
  year={2020},
  publisher={Nature Publishing Group}
}
```
ok

## Eletrocardiograma de 12 derivações banco de dados para pesquisa de arritmia abrangendo mais de 10.000 pacientes

Avanço da máquina moderna ferramentas estatísticas e de aprendizado podem ser treinadas em dados grandes e de alta qualidade para alcançar níveis excepcionais de precisão diagnóstica automatizada.

Como um teste não invasivo, o monitoramento de ECG de longo prazo é uma ferramenta de diagnóstico importante e vital para detectar essas condições. Essa prática, no entanto, gera grandes quantidades de dados, a análise dos quais requer tempo e esforço  consideráveis ​​por especialistas humanos.

4Assim, coletamos e divulgamos este novo banco de dados que contém ECGs de 12 derivações de 10.646 pacientes com taxa de amostragem de 500Hz que apresenta 11 ritmos comuns e 67 condições cardiovasculares adicionais, todas rotuladas por especialistas profissionais. O conjunto de dados consiste em ECGs de 10 segundos e 12 dimensões e rótulos para ritmos e outras condições para cada sujeito. o conjunto de dados pode ser usado para projetar, comparar e ajustar estatísticas e máquinas novas e clássicas técnicas de aprendizagem em estudos focados em arritmias e outras condições cardiovasculares.

O gráfico de ECG de uma batida normal consiste em uma sequência de ondas. As arritmias representam uma família de condições cardíacas caracterizadas por irregularidades na frequência ou ritmo dos batimentos cardíacos.

consiste em uma sequência de ondas, uma onda P apresentando o processo de despolarização atrial, um complexo QRS denotando o processo de despolarização ventricular e uma onda T representando a repolarização ventricular. Outras porções do sinal incluem os intervalos PR, ST e QT.

Existem várias dezenas dessas classes com vários manifestações como batimentos cardíacos excessivamente lentos ou rápidos (bradicardia sinusal (SB) e taquicardia atrial (AT)) e ritmo irregular com segmentos e intervalos de onda ausentes ou distorcidos (contração ventricular prematura (PVC)). O tipo de arritmia mais comum e perniciosa é a fibrilação atrial (AFIB)

De acordo com as práticas atuais de triagem e diagnóstico, cardiologistas ou médicos revisam os dados de ECG, estabelecer o diagnóstico correto e começar a implementar planos de tratamento subsequentes, como regime de medicação e ablação por cateter de radiofrequência. 
No entanto, a demanda por diagnósticos automáticos de doenças cardíacas de alta precisão recentemente aumentou acentuadamente em paralelo com a política de saúde pública de implementação de exames mais amplos


4Esse banco de dados contém o maior número de assuntos, a maior taxa de amostragem e o maior número de ligações. Além disso, também inclui 11 ritmos cardíacos e 56 tipos de condições cardiovasculares rotulados por médicos profissionais. Além disso, o banco de dados inclui medições básicas de ECG, como QRS contagens, frequência de batimentos atriais, frequência de batimentos ventriculares, deslocamento Q e deslocamento T.


4 Nossos dados consistem em 10.646 ECGs de pacientes, incluindo 5.956 homens e 4.690 mulheres. Entre esses pacientes, 17% apresentavam ritmo sinusal normal e 83% apresentavam pelo menos uma anormalidade. As faixas etárias com maior prevalência foram 51–60, 61–70 e 71–80 anos representando 19,82%, 24,38% e 16,9%, respectivamente. 

Uma descrição detalhada das características basais dos participantes inscritos ea distribuição de frequência de ritmo é apresentada na Tabela 2. O número de volts por bit A/D é 4,88 e o conversor A/D tinha resolução de 32 bits. A unidade de amplitude foi microvolt. O limite superior foi 32.767, e o limite inferior foi
−32.768. 

4 O conselho de revisão institucional do Shaoxing People's Hospital aprovou este estudo, concedeu a isenção
para obter consentimento informado e permitiu que os dados fossem compartilhados publicamente após a desidentificação.


Os dados foram adquiridos em quatro etapas. Primeiro, cada sujeito foi submetido a um ECG de repouso de 12 derivações teste que foi feito durante um período de 10 segundos. Os dados foram armazenados no sistema GE MUSE ECG. Segundo, um médico licenciado rotulou o ritmo e outras condições cardíacas. Outro médico licenciado realizou segunda validação, se houversse desacordoum m~edico s~enior tomava a decisão fiunal

Como se sabe, a presença de ruído pode ser um obstáculo notável para qualquer análise estatística.
Uma vez que a frequência intervalo de ECG normal é de 0,5Hz a 50Hz, o filtro passa-baixa Butterworth foi usado para remover o sinal com um frequência acima de 50Hz.
A técnica Non Local Means (NLM) foi usada para lidar com o ruído restante.

Esses arquivos estão disponíveis online em fgshare13.
cada arquivo CSV mencionado acima contém 5.000 linhas e 12 colunas com nomes de cabeçalho apresentando a derivação de ECG.
O arquivo de diagnósticos contém todas as informações de diagnóstico para cada sujeito, incluindo nome do arquivo, ritmo,
outras condições, idade do paciente, sexo e outros atributos de resumo de ECG (adquiridos no sistema GE MUSE).


a irregularidade sinusal pode ser facilmente separada do ritmo sinusal posteriormente por um único critério, variação do intervalo RR. 

Os recursos extraídos da derivação II incluem frequência ventricular em batimentos por minuto (BPM), frequência atrial em BPM, duração do QRS em milissegundos, intervalo QT em milissegundos, eixo R,  Eixo T, contagem QRS, início Q, deslocamento Q, média do intervalo RR, variação do intervalo RR, contagem do intervalo RR. Características

A pontuação F1 de 0,97 é a pontuação média da validação cruzada de 10 vezes (10-fold cros-validation) com dados de teste de 20%. Por
cada grupo, os tamanhos de amostra dos conjuntos de dados de treinamento e teste são apresentados na Tabela 5

Incentivamos a implementação e comparação de vários esquemas de classificação concorrentes que incluem ajuste de superparâmetros. Os resultados da classificação precisam relatar a precisão do desempenho médio usando 10-validação de dobra. (10 fold-validation).

F1-score, Overall Accuracy, Confusion Matrix, Precision (Positive Predictivity), and Recall (Sensitivity) are 
recommended to report classifcation performance.


4 Na etapa de extração de recursos, BioSPPy é recomendado para extrair recursos gerais de resumo de ECG, como contagem de QRS, R
localização da onda etc. Quanto aos pacotes de aprendizado de máquina, sugerimos scikit-learn e TensorFlow para construção de modelo de aprendizado.

