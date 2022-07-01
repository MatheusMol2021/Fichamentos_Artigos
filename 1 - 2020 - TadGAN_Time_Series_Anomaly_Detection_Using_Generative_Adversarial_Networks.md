# TadGAN: Time Series Anomaly Detection Using Generative Adversarial Networks


[Download](https://ieeexplore.ieee.org/abstract/document/9378139?casa_token=GkMo8tGXvgAAAAAA:U861qYuZUhXOdEnQLRwXBdbZwEQecXSSB1tJ-wjWvctr9zqYTLwt9Fj8zO8-rVABfIHDJ75ViEM)


## Referência
```bibtex 1
@inproceedings{geiger2020tadgan,
  title={TadGAN: Time series anomaly detection using generative adversarial networks},
  author={Geiger, Alexander and Liu, Dongyu and Alnegheimish, Sarah and Cuesta-Infante, Alfredo and Veeramachaneni, Kalyan},
  booktitle={2020 IEEE International Conference on Big Data (Big Data)},
  pages={33--43},
  year={2020},
  organization={IEEE}
}
```
ok problema

## TadGAN: Detecção de Anomalias em Séries Temporais Usando Redes Adversariais Generativas

## Abstract

Anomalias de séries temporais podem oferecer informações relevantes a situações críticas em vários campos, desde finanças e aeroespacial para os domínios de TI, segurança e medicina.

1.1 Métodos atuais de aprendizado de máquina não supervisionado de última geração para detecção de anomalias sofrem de problemas de escalabilidade e portabilidade  e podem ter altas taxas de falsos positivos.

1.2 Para capturar o correlações temporais de distribuições de séries temporais, usamos LSTM Redes Neurais Recorrentes como Modelos Base para Geradores e Críticos.

nosso método tem a pontuação F1 média mais alta em todos os conjuntos de dados.

## introduction

Uma anomalia de série temporal é definida como s um tempo ponto ou período em que um sistema se comporta de forma incomum [1].

Uma das técnicas de detecção mais simples é o limiar, que detecta pontos de dados que excedem um intervalo normal.

Um dos desafios fundamentais do aprendizado profundo abordagens é que sua notável capacidade de ajustar dados carrega a correm o risco de que eles possam ajustar dados anômalos também.

Além disso, trabalha em este domínio (GAN) frequentemente enfatiza a melhoria do aprendizado profundo modelo em si. No entanto, como mostramos neste artigo, melhorar etapas de pós-processamento podem ajudar significativamente na redução do número de falsos positivos.

No momento da redação deste artigo, o benchmark inclui 9 pipelines de detecção de anomalias, 13 conjuntos de dados e 2 mecanismos de avaliações.

Um ponto de dados é identificado como uma anomalia se a diferença entre sua entrada prevista e o original entrada excede um determinado limite.

Hundman et ai. [6] propor Longo Prazo Redes neurais recorrentes (LSTM RNNs), para prever o futuro passos de tempo e sinalizar grandes desvios das previsões

No entanto, sem a devida regularização, esses métodos baseados em reconstrução podem facilmente se tornar superajustados,
resultando em baixo desempenho. Neste trabalho, propomos o uso de aprendizagem adversarial para permitir séries temporais
reconstrução.

A ideia central por trás dos métodos de detecção de anomalias baseados em reconstrução é aprender um modelo que possa codificar um
ponto de dados (no nosso caso, um segmento de uma série temporal) e em seguida, decodifique o codificado (ou seja, o reconstruído). Um


Arquitetura: Em nossos experimentos, as entradas para TadGAN são sequências de séries temporais de comprimento 100 (domínio X), e o espaço latente (domínio Z) é 20-dimensional. Usamos 1 camada Memória de Longo Prazo Bidirecional (LSTM) com 100 unidades ocultas como o Gerador E e um LSTM bidirecional de 2 camadas com 64 unidades ocultas cada como Gerador G, onde o dropout é aplicado.

Métricas de avaliação: Medimos o desempenho de diferentes métodos usando as métricas comumente usadas Precisão, Recall e F1-Score.


4) Baselines: São métodos baseados em 3 categorias, metodos de predição, reconstrução e ferramentas de comercio online.

ARIMA, HTM, LSTM, AutoEncoder,MAD-GAN, Microsoft Azure Anomaly Detector, Amazon DepAR
