# MIT-BIH Arrhythmia Database

## Physionet (https://physionet.org/content/mitdb/1.0.0/)
um dos primeiros grandes produtos na pesquisa de análise de arritmia e assuntos relacionados foi o MIT-BIH Arrhythmia Database, este foi o primeiro material de teste padrão disponível para avaliação para detectores de arritmia.

'Esta base de dados contem 48 trechos de meia hora de gravações de ECG ambulatorial de dois canais, obtidos de 47 indivíduos estudados pelo "BIH Arrhythmia Laboratory". 23 gravações foram escolhidas aleatoriamente, sendo 60% dos dados coletados de uma população mista de pacientes internados e 40% de pacientes ambulatoriais. as demais 25 gravações foram selecionadas do mesmo conjunto para incluir arritmias menos comuns e significativas clinicamente que não seriam bem representadas em uma pequena amostra aleatoria.

As gravações foram digitalizadas a 360 amostras por segundo com resolução de 11 bits em uma faixa de 10mV. discordâncias foram resolvidas para obter anotações de referencia legível por computadr para cada batida.


## Artigo
[Download](http://ecg.mit.edu/george/publications/mitdb-embs-2001.pdf)
@ARTICLE{932724,
  author={Moody, G.B. and Mark, R.G.},
  journal={IEEE Engineering in Medicine and Biology Magazine}, 
  title={The impact of the MIT-BIH Arrhythmia Database}, 
  year={2001},
  volume={20},
  number={3},
  pages={45-50},
  doi={10.1109/51.932724}}

O banco de dados de aritmia "MIT-BIH", foi o primeiro material padrão para detectores e analisadores de arritmia, e vem sendo usado como pesquisa básica em dinamica cardíaca em mais de 500 sites em todo o mundo, muito utilizada para pesquisa básica como tambem para desenvolvimento e avaliação de dispositivos médicos.


OS ECG são muito utilizados por serem um método não invasivo de avaliar a fisiologia do coração. Desde meados de 1970, estuda-se anormalidades no ritmo cardíaco (arritmias) e tambem métodos automatizados para sua detecção, são feitas pesquisas na academia e na industria com o mesmo interesse.

'Há uma variabilidade muito ampla de ritmos no ECG, tanto entre sujeitos como em indivíduos ao longo do tempo, de modo que uma coleção  representativa útil deve incluir muitas gravações,

Nas décadas de 1960 e 1970, o desenvolvimento de algoritmos automatizados foi dificultados pela falta de dados universalmente acessíveis. Cada grupo utilizava seu próprio conjunto de dados e muitas vezes auto-avaliaram seus algoritmos  usando esse mesmos dados e ficou claro que o desempenho de seus algoritmos era dependente dos dados,

Reconhecendo a necessidade de um conjunto adequado de ECG ao longo para encorajar avaliaç~poes estritamente reprodutíveis, foi esperado uma disponibilidade de uma base de dados comum entre idades de 23 a 89 anos. Na maioria dos registros, um canal é um membro mdificado de chumbo II (MLII), obtido pela colocação de eletrodos no tórax como é feito no registro ambulatorial de ECG, e o outro canal é geralmente V1(às vezes V2, V4 ou V5, dependendo do assunto).

Foram necessários 5 anos para concluir a digitalização, devido aos limites da tecnoogia daquela época


## Limitação técnica

Durante as gravações dos sinais foi verificado artefatos relacionados a componentes mecânicos específicos dos gravadores e da unidade de reprodução e tambem diferenças mínimas entre as orientações de gravação de dois canais de reprodução resultam em uma distorção de sinais de até 40 ms em alguns casos. Além disso, a oscilação vertical da fita na gravação ou reproduçã introduz a uma inclinação variável no tempo, a inclinação deve ser antecipada no projeto pois é uma complicação indesejada para quem pretende usar algoritmos para análise de ECG.

'As gravações digitalizadas n banco de dados reproduz fielmente as gravações analógicas, de modo que o software destinado para analisar fitas analógicas contendo batimentos podem ser avaliados usando essas gravações. Com o apoio de dois cardiologistas que trabalharam de forma independente, foi adicionado rótulos de batimentos adicionais excluindo detecções falsas conforme necessário, e alterando os rótulos para batimentos anormais. Cada um dos dois cardiologistas fez anotações que foram trancritas de forma legível pelos computadores, posteriormete os dois conjuntos foram comparados e apresentados todas as discrepancias destacadas, cada uma foi examinada e resolvido por consenso. Algumas registros  não foram classificados pois os cardiologistas foram incapazes de chegar a um consenso, entretanto estes dados foram mantido pois a presença destes sinais representam desafios mais interessantes para análise automatizada.

'os anotadores forma instruídos a usar todas as evidências disponíveis para identificar cada complexo QRS, a base de daddos contém 7 episodios de perda de sinal ou ruído tão grave que os complexos QRS não podem ser detectados. Em 1983, as posições foram ajustadas com anotações de batida usando software que filtrou digitalmente o sinal primário (geralmente MLII) para enfatizar o QRS, isto permitiu batidas confiaveis para estudos que exigem forma de onda média, bem como para alta precisão medição de intervalos entre batidas em estudos de variabilidade da frequência cardíaca (uma vez que fontes mecânicas de variabilidade da velocidade da fita foram compreendidas).

'. Em 1999, foi disponibilizado metade do banco de dados na PhysioNet, que permite a muitos estudantes uma parte significativa dos dados para estudos exploratórios sem custo. Todas as medições de desempenho são então determinadas por comparações automatizadas entre os arquivos de anotação do algoritmo com a referência a arquivos de anotação usando software de comparação, deste modo, usuários finais de analisadores podem verificar os ressultados, uma vez que rodos os materiais necessário estão disponíveis para qualquer um.

O banco de dados de arritmia do MIT-BIH foi selecionado especificamente porque contém combinações complexas de ritmo, variação morfológica e ruídos que podem trazer vários desafios para analisadores automáticos de arritmia.

Antes dos bancos de dados se tornaram disponíveis, as estatísticas de desempenho foram de pouco ou nenhum valor, pois era amplamente entendido que cada fabricante projetava seus produtos usando seus próprios dados, quando utilizavam outros dados, seus equipamentos não tinham tanto desempenho e aqueles que não estava a altura de seus concorrentes fizeram muitos investimentos em melhoria de desempenho, por isso a falta de dados bem caracterizados dificultou o progresso dos fabricantes. O padrão geral de performance para os detectores de arritmia comerciais melhoraram rapidamente através da disponibilidade dos bancos de dados.







[Download](https://www.ahajournals.org/doi/pdf/10.1161/01.CIR.101.23.e215?download=true)

@article{goldberger2000physiobank,
  title={PhysioBank, PhysioToolkit, and PhysioNet: components of a new research resource for complex physiologic signals},
  author={Goldberger, Ary L and Amaral, Luis AN and Glass, Leon and Hausdorff, Jeffrey M and Ivanov, Plamen Ch and Mark, Roger G and Mietus, Joseph E and Moody, George B and Peng, Chung-Kang and Stanley, H Eugene},
  journal={circulation},
  volume={101},
  number={23},
  pages={e215--e220},
  year={2000},
  publisher={Am Heart Assoc}
}

O auto apresenta o recém inaugurado recurso de pesquisa para sinais fisiológicos complexos, que se destina ao estudo e investigação de sinais biológicos cardiovasculares e outros complexos.

- PhysioBank: é um grande e crescente arquivo de documentos digitais bem caracterizados. gravações de sinais fisiológicos e dados relacionados para uso pela comunidade de pesquisa biomédica.

- PhysioToolkit: é uma biblioteca de código aberto software para processamento e análise de sinais fisiológicos, a exibição interativa e caracterização de sinais, a criação de novas bases de dados, a simulação de sinais fisiológicos e outros, a avaliação quantitativa e comparação de métodos de análise e análise de processos não estacionários.

- Physionet: Ele fornece facilidades para a análise cooperativa de dados e a avaliação de novos algoritmos propostos.Além de fornecer acesso eletrônico gratuito aos dados do PhysioBank e ao software PhysioToolkit através da Web.
