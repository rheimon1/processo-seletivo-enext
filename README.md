# Requisitos Task1, Task2 e Plus 

É necessário o python 3.6 (ou superior) e o gerenciador de pacotes pip.

Executar os comandos conforme o exemplo abaixo:

- pip3 install virtualenv
- virtualenv venv -p python3
- source venv/bin/activate
- pip install -r requirements.txt

Ao terminar poderá sair do ambiente com o comando deactivate.

# Task 1, Task 2 e Plus

- Os exercícios Task 1, Task 2 e Plus foram resolvidos utilizando a linguagem de programação python e se encontram dentro do arquivo main.py que contém uma classe QuakeLogParser com alguns métodos. Sendo assim, o método parser() se refere ao parser para o log games.log (TASK 1).

- O método print_report_parser(), ao ser invocado, imprime um relatório de cada jogo conforme solicitado e o método general_ranking_kills_player() imprime um ranking geral de kills por jogador(TASK 2).

- O método means_of_death() gera um relatório de mortes agrupadas pelo motivo da morte por partida. E o método print_report_means_of_death() imprime esse relatório(PLUS).

- Por fim, o método create_file_parser_json() gera um arquivo json que permitirá a api consultar o resultado do game por ID(TASK 3). 

- O arquivo test_main.py contém alguns testes unitários feitos. Para executá-los basta informar no terminal o comando pytest

# TASK 3 (API)

- A api foi feita utilizando Node.js e ela contém um endpoint que busca o resultado do game por ID no arquivo parser.json gerado pela Task 1.

- Para executar a API é necessário o Node e o NPM instalados e um software para requisiçoes. A api está escutando na porta 3333.

A seguir os comandos para executar:

- npm install;
- npm run start;

Após os comandos acima, é possível acessar o endpoint conforme abaixo.

- Endpoint para buscar os resultados por id: http://localhost:3333/games/{id}
