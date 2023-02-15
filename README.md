# Api desenvolvida com Newsapi e Python.

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/LombaAnderson/pythonapi/blob/main/LICENSE)

# Sobre o projeto

Nesta aplicação, a api da Newsapi foi consumida na linguagem Python e exibida uma lista de notícias recentes do Brasil com informações de seus autores, título e descrição das notícias. Houve preocupação no sentido de esconder a chave de segurança na utilização da biblioteca dotenv do Python

## Print do projeto no Visual Studio Code
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/218907532-825a7304-11fa-4d67-b494-b4b45aaf05f8.png" width="800" />
</div>

## Página do Google Colab
<div align="center">
<img src="https://user-images.githubusercontent.com/60937513/218911048-2cc7afd1-c40a-4fd0-8f7c-e494085116d0.PNG" width="800" />
</div>

# Como executar o projeto no Google Colab e no Visual Studio Code

## Instalando biblioteca newsapi 
pip install newsapi-python

## Importando no Google Colab NewsApiClient

from newsapi import NewsApiClient

## Autenticando a Api

api = NewsApiClient(api_key= 'put your key')

## Buscando notícias recentes em Português

api.get_top_headlines(language='pt')


# Comandos utilizados no Visual Studio Code

## Instalação do newsapi  
pip install newsapi-python

## Instalação da biblioteca responsável por esconder a chave de segurança
pip install python-dotenv


# Clonar repositório
git clone https://github.com/lombaAnderson/pythonapi

```
# Autor

Anderson Lomba de Oliveira

Linkedin

https://www.linkedin.com/in/anderson-lomba-140279142/

Portfólio

https://www.lombanderson.epizy.com

# Agradecimentos

Agradeço a Deus principalmente que faz tudo por mim e a minha esposa que amo de paixão!
