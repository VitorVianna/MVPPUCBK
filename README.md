# API de Agendamento de Consultas para o hospital HELLPASS

Este pequeno projeto foi desenvolvido como MVP para a Disciplina **Desenvolvimento Full Stack Básico** & **Arquitetura de Software**.

O objetivo foi desenvolver esta API em Python para gerenciar as consultas no hospital.
Com as rotas criadas, é possível:
1 - Listar Todos, Adicionar e Excluir Médicos.
2 - Listar Todos, Listar por CPF e Adicionar novos Clientes.
3 - Listar Todas e Criar novas Consultas. 
4 - Foi implementado também o arquivo Dockerfile, com o objetivo de poder executar todo o sistema utilizando conteinerização. 

Nesta documentação, abaixo existirão 2 links para vídeos, o primeiro foi desenvolvido para explicar os conceitos básicos, para a disciplina **Desenvolvimento Full Stack Básico**. O segundo, mais abaixo, foi desenvolvido para explicar os conceitos da utilização do Docker, bem como a utilização das APIs externas extras, para a disciplina **Arquitetura de Software**.

As APIs externas são (utilizadas apenas no FrontEnd):
- **Via CEP** (esta já havia sido implementada) - Com o objetivo de listar o endereço do cliente a partir do CEP.
- **Economia** - Para trazer informações atualizadas de câmbio.
- **IBGE.GOV** - Para trazer notícias atualizadas.
- **HG Brasil** - Para trazer informações de Previsão do Tempo atualizada.
  - Para utilizar este último, é necessário inserir a Key na variável keyPrevisao, do arquivo /js/news.js, localizada na linha **3**.
---

## Melhorias que podem ser implementadas:
- Edição de Profissionais
- Edição de Clientes
- Marcação de Consulta com hora específica, atualmente apenas o dia está sendo enviado para a API.

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

> python -m venv env
> env/Scripts/Activate.ps1  

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

## Demonstração (MVP - FullStack Básico)
Vídeo de demonstração: https://photos.app.goo.gl/y2tJBVRcA6PXHf6p9

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.



### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).

## Demonstração (MVP - Arquitetura de Software)
Vídeo de demonstração: ([link](https://photos.app.goo.gl/U25cpr6sins3gVzTA))

## Fluxograma do sistema:
![Fluxograma do sistema](/image/fluxogramaHellpass.drawio.png)