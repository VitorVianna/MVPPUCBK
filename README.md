# API de Agendamento de Consultas para o hospital HELLPASS

Este pequeno projeto foi desenvolvido como MVP para a Disciplina **Desenvolvimento Full Stack Básico** 

O objetivo foi desenvolver esta API em Python para gerenciar as consultas no hospital.
Com as rotas criadas, é possível:
1 - Listar Todos, Adicionar e Excluir Médicos.
2 - Listar Todos, Listar por CPF e Adicionar novos Clientes.
3 - Listar Todas e Criar novas Consultas. 

---
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
