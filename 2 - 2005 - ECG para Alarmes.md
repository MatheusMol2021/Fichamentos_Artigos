# Processamento de sinais de ECG para geração automática de alarmes

[Download](https://www.researchgate.net/profile/Marcelo-Segatto/publication/228876146_Processamento_de_sinais_de_ECG_para_geracao_automatica_de_alarmes/links/0912f510041a3e27a5000000/Processamento-de-sinais-de-ECG-para-geracao-automatica-de-alarmes.pdf)


## Referência
```bibtex
@inproceedings{souza2006processamento,
  title={Processamento de sinais de ECG para gera{\c{c}}{\~a}o autom{\'a}tica de alarmes},
  author={Souza, Camila B and Andre{\~a}o, Rodrigo V and Segatto, Marcelo V},
  booktitle={VI Workshop de Inform{\'a}tica M{\'e}dica-WIM2006},
  year={2006}
}
```

## Resumo
Este artigo apresenta um sistema de análise de eletrocardiograma (ECG) ambulatorial, desenvolvido em Matlab, voltado para o monitoramento da atividade elétrica do coração de pacientes. O aplicativo conta com algoritmos de segmentação e classificação do sinal de ECG, e com uma interface gráfica amigável, que executa e gera a visualização dos resultados
desses algoritmos. Planeja-se a sua utilização em tempo real para geração automática de alarmes e criação de relatório de eventos para auxílio ao diagnóstico médico. 

## Pontos Fortes
- O autor utiliza os dados ECG para o monitoramento dos sinais vitais dos pacietes,

- pacientes com doenças cardíacas crônicas necessitam de um acompanhamento especial, foi então introduzido a telecardiologia com o tele-monitoramento para acompanhar os seus sinais vitais e posteriormente gerar alarmes para que na identificação de alguma anomalia possa ser feito um monitoramento eficaz, minorando as consequencias da doença.

- Diversos sistemas apresentados na literatura realizam o processamento de sinais
de ECG [Shui-cai 2004] [Boquete 2005] [Zhongming 2003] [Hermans 2004] [Dorn
2005].

- o sistema é composto por uma base de dados contendo registros para a simulação de algoritmos e por (interface GUI) para simular algoritmos. O sistema tem uma rede de 3 eletrodos a 250HZ que monitora o coração do paciente,

- O sistema conta com duas bases de registros de ECG ambulatorial para simulação e validação dos algoritmos: QT Database e ST-T Database. A base de dados QT contém 105 registros, com dois canais de 15 minutos de sinal amostrado a uma freqüência de 250 Hz [Laguna 1997]. Todos os registros incluem etiquetas dos picos das formas de ondas (onda P, complexo QRS, ondas T e U) de no máximo 30 batimentos, dando um total de 3623 batimentos [Laguna 1997], e em 78 registros os batimentos foram classificados manualmente por cardiologistas. A base de dados ST-T contém 90 registros com dois canais de 2 horas de sinal amostrado a uma freqüência de 250 Hz [Andreão 2004]. Cada registro possui anotações manuais, feitas por médicos, de episódios de ST-T os quais foram diagnosticados ou supostos episódios de isquemia. 


## Pontos Fracos
Utiliza o Matlab