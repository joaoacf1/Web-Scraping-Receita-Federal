# Web-Scraping-Receita-Federal
Esse script desenvolvi usando Python, Selenium, Pandas e a API 2Captcha. O objetivo principal é acessar o site da Receita Federal para coletar informações valiosas a partir de um arquivo CSV de CPFs e datas de nascimento.

![Receita Web Scraping](https://github.com/joaoacf1/Web-Scraping-Receita-Federal/assets/72554649/e900abfc-2234-46a9-9789-3dd33bd3ab13)

Fluxo:

- Leitura de Dados: Começa lendo um arquivo CSV com os CPFs e as datas de nascimento que você quer consultar.
- Navegação Automática: Utilizando o Selenium, ele entra no site da Receita Federal e insere os dados de cada CPF em um loop.
- Resolução de Captchas: Resolve o hCaptcha usando a API do 2Captcha, o que significa que você não precisa ficar quebrando a cabeça com os desafios visuais do site.
- Coleta de Informações: Após passar pelo captcha, ele navega até a página de resultados e coleta os dados necessários.
- Geração de Relatório: Todos os dados coletados são organizados em um arquivo Excel usando o Pandas.

Tecnologias usadas:

- Python: A linguagem de programação.
- Selenium: Para automação de navegação web.
- Pandas: Para manipulação de dados e criação do arquivo Excel.
- 2Captcha: Para resolver os hCaptchas automaticamente.


Link do site: https://servicos.receita.fazenda.gov.br/Servicos/CPF/ConsultaSituacao/ConsultaPublica.asp
