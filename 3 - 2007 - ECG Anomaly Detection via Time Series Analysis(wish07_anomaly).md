# ECG Anomaly Detection via Time Series Analysis(wish07_anomaly)

[Download](https://link.springer.com/chapter/10.1007/978-3-540-74767-3_14)


## Referência
```bibtex 1
@inproceedings{chuah2007ecg,
  title={ECG anomaly detection via time series analysis},
  author={Chuah, Mooi Choo and Fu, Fen},
  booktitle={International Symposium on Parallel and Distributed Processing and Applications},
  pages={123--135},
  year={2007},
  organization={Springer}
}
```
ok


# Detecção de anomalias de ECG por meio de análise de séries temporais

Três importantes sinais vitais que geralmente são coletados em tal monitoramento de sensor médico sistema são batimentos cardíacos, taxas de pulso e saturação de oxigênio. 

Eles propõem o uso de redes de sensores sem fio que podem fornecer recursos que são valioso para monitoramento remoto e contínuo. Em tais redes de sensores, dispositivos sem fio são integrados a uma ampla variedade de sensores ambientais e médicos. Os dados dos sinais vitais podem ser coletados automaticamente, permitindo o monitoramento médico remoto e diagnóstico. Prevê-se que tal sistema precisa ser projetado de forma eficiente, uma vez que alguns desses dispositivos de monitoramento funcionam com bateria e, portanto, têm restrições de energia limitadas. Normalmente, os dados do sensor são coletados por alguns nós de armazenamento intermediários que possuem maior largura de banda sem fio. 

1.1 Para melhor eficiência energética, os nós intermediários de armazenamento podem processar esses fluxos em tempo real para identificar qualquer anormalidade. Uma vez identificado, apenas o dados anormais precisam ser enviados ao médico para diagnóstico adicional, enquanto o resto do os dados normais podem ser arquivados nos nós de armazenamento local. Os nós de armazenamento local podem ainda transferir esses dados normais para unidades de armazenamento de longo prazo em uma escala de tempo mais lenta (por exemplo, diariamente).

1.2 Conforme descrito anteriormente, é mais  energia eficiente para transmitir apenas dados anormais por meio de links sem fio. Para decidir se um tempo real fluxo de dados do sensor contém dados anormais, é preciso usar um esquema de detecção de anomalias.


Nosso esquema é um aprimoramento do esquema Brute Force Discord Discovery (BFDD) proposto em.Usando os registros de batimentos  ardíacos do banco de dados de arritmia do MIT-BIH [3], demonstramos que nosso esquema AWDD fornece maior precisão na distinção entre batimentos cardíacos normais/anormais dentro de 40 segundos trechos de leituras de batimentos cardíacos quando comparado ao BFDD.


Os autores em [4] propõem dois algoritmos de descoberta de discórdia, a saber a descoberta de discórdia de força bruta (BFDD) e a descoberta de discórdia heurística (HDD).

Dataset: usamos os dados de ECG do MIT BIH Arrhythmia Database.