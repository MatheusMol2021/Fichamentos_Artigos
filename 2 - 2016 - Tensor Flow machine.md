# TensorFlow: A System for Large-Scale Machine Learning

[Download](https://www.usenix.org/system/files/conference/osdi16/osdi16-abadi.pdf)

## Referência
```bibtex 1
@inproceedings {199317,
author = {Mart{\'\i}n Abadi and Paul Barham and Jianmin Chen and Zhifeng Chen and Andy Davis and Jeffrey Dean and Matthieu Devin and Sanjay Ghemawat and Geoffrey Irving and Michael Isard and Manjunath Kudlur and Josh Levenberg and Rajat Monga and Sherry Moore and Derek G. Murray and Benoit Steiner and Paul Tucker and Vijay Vasudevan and Pete Warden and Martin Wicke and Yuan Yu and Xiaoqiang Zheng},
title = {{TensorFlow}: A System for {Large-Scale} Machine Learning},
booktitle = {12th USENIX Symposium on Operating Systems Design and Implementation (OSDI 16)},
year = {2016},
isbn = {978-1-931971-33-1},
address = {Savannah, GA},
pages = {265--283},
url = {https://www.usenix.org/conference/osdi16/technical-sessions/presentation/abadi},
publisher = {USENIX Association},
month = nov,
}
```


## Comentário

## Pontos fortes
- TensorFlow:
o TensorFlow permite que os desenvolvedores experimentem novas otimizações e algoritmos de treinamento. O TensorFlow oferece suporte a uma variedade de aplicativos, com foco em treinamento e inferência em redes neurais profundas. Vários serviços do Google usam o TensorFlow em produção, nós o lançamos como um projeto de código aberto e tornou-se amplamente utilizado para pesquisa de aprendizado de máquina.

TensorFlow
suporta treinamento e inferência em grande escala: ele usa com eficiência centenas de servidores poderosos (habilitados para GPU) para treinamento rápido e executa modelos treinados para inferência em produção em várias plataformas, desde grandes clusters distribuídos em um datacenter, até execução local em dispositivos móveis.

O TensorFlow fornece uma abstração de programação simples baseada em fluxo de dados que permite aos usuários implantar aplicativos em clusters distribuídos, estações de trabalho locais, dispositivos móveis e aceleradores personalizados

O TensorFlow oferece vários algoritmos de aprendizado de máquina com fluxo de controle condicional e iterativo. Como um exemplo, temos a rede neural recorrente (RNN) como um LSTM pode gerar previsões de dados.O núcleo de um RNN é uma relação de recorrência, onde o fluxo de controle dinâmico permite a interação sobre sequencias de controles variáveis

Foi lucrativo,  implementar manualmente kernels fundidos para algum desempenho operações críticas, como as funções de ativação ReLU e Sigmoid e seus gradientes correspondentes.

6

## Pontos fracos