Dashboard em Django

- Pequena aplicação em que há duas telas utilizando o framework Django
- Pagina para inserir dados e outra para fazer a somatoria do valor total, e um grafico de gasto mes a mes.

Pagina Lançar:
    Utilizado HTML e Bootstrap
    Utilizado o framework Django para criar o forms e enviar os dados para o banco de dados
    Utilizamos SQLite para os lançamentos e o ORM do Django para manipular.

Pagina Home:
    Gasto total:
        Criado em HTML, CSS, JS e bootstrap
        Somatoria de valores do banco de dados utilizando uma função em python, e disponibilizando um JSON na url /total_gasto
        Função JS para pegar o valor de total na URL e renderizar na Home
    Gasto Mensal:
        Utilizado HTML, biblioteca Chart.js, JS e o framework Django
        Função em python para pegar o mes atual, e retornar um JSON com os gastos dos ultimos 12 meses
        Retornar o JSON para a url /relatorio_gasto
    Lista de Gastos:
        Utlizando HTML, CSS, Bootstrap e Framework Django

O intuito do projeto é receber informaçoes de gastos, salva-los no banco de dados, e transmitir as informações de gasto total, gasto mensal, e lista de gastos na home.html

O Deploy da aplicação pode ser acessada em https://jpcamatari.tech

