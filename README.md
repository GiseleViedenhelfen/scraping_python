# scraping_python
Projeto que acessa site feito para fins didáticos de raspagem de dados de url "http://books.toscrape.com/index.html", coleta e cria banco de dados a partir das informações. Utiliza Python e mongoDB.

Para a raspagem de dados utiliza as bibliotecas requests e parsel disponíveis nos links https://pypi.org/project/requests/ e https://pypi.org/project/parsel/, respectivamente.

Para rodar o projeto na máquina é necessário apenas Docker, utilize "docker build -t nomeDaImagem ." no terminal na raiz do projeto e "docker run -it nomeDaImagem" para rodar o projeto.

Caso deseje ver o banco de dados no seu computador será necessário ter o mongo acessível, sendo via docker uma possibilidade. Basta seguir os passos de baixar a imagem do mongo "docker pull mongo:4", depois criar e ativar o container "docker run --name <nome-do-container> -d mongo:4" e, por fim, acessar o shell do mongo com "docker exec -it <nome-do-container-ou-id> mongo".