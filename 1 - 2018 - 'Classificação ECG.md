# ECG Heartbeat Classification: A Deep Transferable Representation

[Download](https://sci-hub.se/10.1109/ichi.2018.00092)
[Base de dados](https://www.physionet.org/content/ptbdb/1.0.0/)

# Referencias
```bibtex
@inproceedings{kachuee2018ecg,
  title={Ecg heartbeat classification: A deep transferable representation},
  author={Kachuee, Mohammad and Fazeli, Shayan and Sarrafzadeh, Majid},
  booktitle={2018 IEEE International Conference on Healthcare Informatics (ICHI)},
  pages={443--444},
  year={2018},
  organization={IEEE}
}
```

## Pontos Fortes

'O eletrocardiograma pode ser usado de maneira confiável para monitorar a funcionalidade do sistema cardiovascular,

'No artigo, foi usado o conjunto de dados "MIT-BIH e PTB" Diagnostics da PhysionNet, nele foi aplicado um método baseado em redes neurais profundas, no método utilizado ele é capaz de fazer previsões com acurácias médias de 93,4% a 95,9% para classificação de aritmias.

'No uso de técnicas de aprendizagem de máquina, além de pré processar os sinais, a análise ede processamento de sinais como perceptrons multicamadas, árvores de decisão, etc.

Metodologia:
- Pré-Processsamento:
deve ser cortado as batidas e zerá-las após um determinado comprimento

-Treinamento Classificador de arritmia:
Aqui temos uma rede neural convulacional para classificalção dos batimentos ECG de dados MIT-BIH. Esse método de classificação pode ser usado não somente para para fins de detecção de arritmia mas tambem como um informativo de batidas do coração.

Todas as camadas de convolução estão aplicando convolução com 32 kernels de tamanho 5. A rede de previsão consiste em cinco blocos residuais seguidos por duas camadas totalmente conectadas com 32 neurônos. Cada bloco contém duas camadas ReLU, com uma camada residual.

# Neste artigo tem imgens importantes