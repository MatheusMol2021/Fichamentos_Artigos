
> \documentclass 
>>- Fala a classe do docuemtno se é artigo ou anteprjeto

> \usepackage
>>- Adiciona pacotes de configuração

> \begin{document}
> \end{document}
>>- Inicia e termina o texto

> \maketitle
>>- Onde escreve o título

> \section{Título da seção}
>>- Cria uma Seção no trabalho

> \subsection{sobre vinhos}
>>- Cria uma subcessão no texto

> \begin{center}
> \end{center}
>>- Cria um ambiente separado centralizado

> \begin{flushright}
> \end{flushright}
>>- Alinha o texto a direita

> \begin{flushleft}
> \end{flushleft}
>>- Alinha o texto a esquerda

> \textbf{}
>>- Coloca o texto em negrito

> \textit{}
>>- Coloca o texto em Itálico

> \underline
>>- Sublinha o texto

## Inserir fugura
> \usepackage{graficx}
>>- insere pacotes para inserir figuras

> \begin{figure} 
> \end{figure}
```
\begin{figure}[ht]
    \centering
    \includegraphics[width=5cm]{LA.jpg}
    \caption{logo lati}
    \label{fig:my_label}
\end{figure}
```
>> - insere figuras

> \ref{caption}
>>- Usado para citar a figura