# Gerador de LOG.

Script criado para facilitar a criação de LOGs usando python.

## Como usar   
Cópie o arquivo [gera_log.py](https://github.com/danielns-op/GeraLog/blob/main/gera_log.py) para dentro do diretório do seu programa, 
dentro do seu programa você irá importar a classe **GeraLog**
```python
from gera_log import GeraLog
```

Após importar a classe, basta apenas seguir os passos abaixo:
```python
# atribuir a classe a uma variável e definir o nome do arquio de log.
meu_log = GeraLog("nome_arquivo.log")

# executa um função da classe para gravar o log dependendo de sua necessidade.
meu_log.grava_info("Aqui temos apenas um log informativo")
```

Saida gravada no log:
`INFO 2022-09-01 14:00:50,376 - Aqui temos apenas um log informativo`   

| Funções disponíveis | Descrição |
| --- | --- |
| grava_info | Utilizado para gravar informações referente a execução. |
| grava_warning | Uma indicação de que algo inesperado aconteceu, ou indicativo de algum problema. |
| grava_error | Um erro grave, indicando que o próprio programa pode não conseguir continuar em execução. |
| grava_critical | Devido a um problema mais sério, o software não conseguiu executar algumas funções. |
| grava_debug | Informações detalhadas, normalmente de interesse apenas ao diagnosticar problemas. |
