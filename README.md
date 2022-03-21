# Solução do Exercício


## Análise dos dados:

A partir da figura contida em ```figures/dataset.png```

podemos concluir verificando a distribuição nessa amostra que, 
algumas das features possuem  distribuições para cada classe
com diferentes formatos. Por exemplo, na coluna `default_3months`,
o gráfico correspondente à label 0 tem picos afastados do pico principal
do gráfico correspondente à label 1, indicando que dados contidos na região
dos picos provavelmente serão referentes à label 0.

Ao verificar a correlação entre os dados entre a coluna default e as outras colunas
na figura `figures/total_corr.png`, vemos que há uma baixa correlação entre essas colunas
e mesmo fazendo somente para o caso default = 0 `figures/default_0_corr.png`
e para o caso default = 1, `figures/default_1_corr.png` a correlação continua baixa (para
default = 1 os dados são um pouco mais correlacionados, porém ainda é pouco).

Tentei usar essa diferença entre as correlações para filtrar as features do modelo, porém os resultados
não foram satisfatórios. Para os a primeira abordagem, a de olhar a distribuição para as classes o
resultado foi um pouco melhor.

## Modelo:

Para fazer o treino do modelo escolhi as seguintes features "default_3months","dividas_vencidas_qtd", "dividas_vencidas_valor", "acao_judicial_valor","month", que para a amostra obtiveram a distribuição mais diferente.
Também usei para o dataset de treino mais o dataset de teste, a mesma quantidade de elementos com
default = 1 e default = 0
Para evitar com que a diferença entre os valores das variáveis criasse uma tendência no modelo,
optei for fazer um escalonamento nos dados através do StandardScaler. 

Para manter a consistência dos dados
os valores usados foram somente para o dataset de treino. Para os dados da predição e de teste foi usada a
mesma transformação utilizada para o treino.

Para treinar o modelo usei uma regressão logística e obtive as métricas:
`accuracy =  0.6249680225121514`
`precision =  0.7334170854271357`
`recall =  0.6093945720250522`
e a matriz de correlação:
|---------|---------|
|  2906   |  1027   |
|-------------------|
|  1881   |  2004   |
|---------|---------|

O modelo é salvo no arquivo `saved_model/classifier.joblib` e a transformação de
escalonamento é salva no arquivo `saved_model/classifier.joblib`


## Predição

Para realizar a predição o notebook espera um arquivo com uma lista de dicionários.
Ao receber os dicionários os dados são salvos em um dataset pandas, e após
é aplicada a mesma transformação nos dados como no treino e a predição é feita.
Os resultados são salvos em um arquivo a ser definido no notebook


## Makefile

Para instalar os pacotes necessários para a execução dos notebooks podemos rodar o comando
`make install` em um terminal e o comando `make uninstall` para remover os pacotes




## Pontos de Melhorias

Na hora de usar as features, usei as features praticamente como foram passadas
(só foi feito um escalonamento). Explorar um pouco mais as features, poderia
trazer informações novas, que poderiam otimizar o modelo.

Outra melhoria seria fazer o modelo ser escalável para treinar um grande volume
de dados. Por exemplo, ferramentas como tensorflow seria de grande utilidade
que além de facilitar a leitura em batches, ele é capaz de ler os dados do arquivo
enquanto o batch anterior está sendo treinado.

