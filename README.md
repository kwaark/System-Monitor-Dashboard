# Monitoramento de Desempenho

## Descrição
Este projeto é um painel de monitoramento do desempenho do sistema. Ele gera gráficos que mostram o uso da memória RAM e do CPU ao longo do tempo, baseado em dados lidos de um arquivo de texto.

## Instruções de uso

## Pré-requisitos
`Python 3.x` 

`Flask` 

`Matplotlib` 


## Configuração do ambiente
Instale o Python 3.x em seu sistema se ainda não o fez. Você pode baixar o Python [aqui](https://www.python.org/downloads/).

Para gerar os gráficos a partir dos dados, execute o script gerar_graficos.py:  
`python3 data-generator.py`  
Este script vai ler os dados do arquivo dados.txt, gerar os gráficos e salvar as imagens no diretório static/graficos.

Execute o aplicativo Flask com o seguinte comando:  
`python app.py`

Abra um navegador e acesse http://localhost:5000. Você verá a página inicial do painel de monitoramento.

Clique nos botões para visualizar os gráficos do uso de memória e de CPU. Há também um botão para atualizar os gráficos.

Quando terminar, você pode parar a execução do aplicativo Flask pressionando Ctrl+C no terminal.

## Personalizando os dados
Para usar seus próprios dados, substitua o conteúdo do arquivo dados.txt com seus dados no formato correto. Cada conjunto de dados deve ter três linhas:

dd-mm-yyyy hh:mm   
MEM. RAM - Total: xxxMB Used: xxxMB   
CPU% - Used: x.xx%  


## GERAR DADOS AUTOMÁTICO (LINUX):
Use o script "get-usages.sh" para pegar o uso da memoria e CPU atuais.

Abra o cron:  
`crontab -e`

Adicione a seguinte linha no cron para rodar seu script a cada 1 minuto e gravar no data.txt:  
`* * * * * bash /caminho/para/seu/script/get-usages.sh >> dados.txt`

# Contribuições
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.

