from flask_openapi3 import OpenAPI, Info, Tag
from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError
from model import Session, Cliente, Agenda, Profissional
from datetime import datetime
from flask_cors import CORS

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


@app.route('/get_agenda', methods=['GET'])
def get_agenda():
    session = Session()
    agenda = session.query(Agenda).order_by(Agenda.data_consulta)
    if not agenda:
        return {"agenda": ""}, 200
    else:
        result = []
        for tarefa in agenda:
            result.append({
                "data_consulta": tarefa.data_consulta.strftime("%d/%m/%Y"),
                "profissionalId": tarefa.profissional,
                "profissional": session.query(Profissional).filter(Profissional.id == tarefa.profissional).first().nome,
                "clienteId": tarefa.cliente,
                "cliente": session.query(Cliente).filter(Cliente.id == tarefa.cliente).first().nome
            })
        return {"agenda": result}, 200
    
@app.route('/add_agenda', methods=['POST'])
def add_agenda():
    session = Session()
    agenda = Agenda(
        cliente=request.form.get("cliente"),
        profissional=request.form.get("profissional"),
        data_consulta=datetime.strptime(request.form.get("data_consulta"), "%d/%m/%Y")
    )
    try:
        session.add(agenda)
        session.commit()

        return {"agenda": "sucesso"}, 200

    except Exception as e:
        error_msg = "Não foi possível salvar nova agenda : " + str(e)
        print(str(e))
        return {"Erro": error_msg}, 400

@app.route('/add_profissional', methods=['POST'])
def add_profissional():
    session = Session()
    profissional = Profissional(
        nome=request.form.get("nome"),
        crm=request.form.get("crm")
    )
    try:
        session.add(profissional)
        session.commit()

        result = []
        result.append({
            "valor": profissional.id,
            "nome": profissional.nome,
            "crm": profissional.crm
        })

        return {"profissional": result}, 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo profissional : " + str(e)
        print(str(e))
        return {"Erro": error_msg + str(e)}, 400
    
@app.route('/del_profissional', methods=['DELETE'])
def del_profissional():
    session = Session()
    profissional = session.query(Profissional).filter(Profissional.id == request.form.get("id")).first()
    try:
        if not profissional:
            error_msg = "Não Existem Profissionais cadastrados"
            return {"Erro": error_msg}, 404
        else:
            session.delete(profissional)
            session.commit()

            return {"profissional": "Profissional Excluído"}, 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo profissional : " + str(e)
        print(str(e))
        return {"Erro": error_msg + str(e)}, 400

@app.route('/get_profissional', methods=['GET'])
def get_profissional():
    session = Session()
    profissionais = session.query(Profissional)
    if not profissionais:
        error_msg = "Não Existem Profissionais cadastrados"
        return {"Erro": error_msg}, 404
    else:
        result = []
        for profissional in profissionais:
            result.append({
                "valor": profissional.id,
                "nome": profissional.nome,
                "crm": profissional.crm
            })

        return {"profissionais": result}
    
@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    session = Session()
    cliente = Cliente(
        nome = request.form.get("nome"),
        cpf = request.form.get("cpf"),
        rg = request.form.get("rg"),
        cep = request.form.get("cep"),
        rua = request.form.get("rua"),
        bairro = request.form.get("bairro"),
        cidade = request.form.get("cidade"),
        estado = request.form.get("estado"),
        numero = request.form.get("numero"),
        complemento = request.form.get("complemento"),
        pais = request.form.get("pais"),
        data_nascimento = datetime.strptime(request.form.get("data_nascimento"), "%d/%m/%Y"),
        sexo = request.form.get("sexo"),
    )

    try:
        session.add(cliente)
        session.commit()

        resultClient = []
        resultClient.append({
            "nome": request.form.get("nome"),
            "cpf": request.form.get("cpf"),
            "rg": request.form.get("rg"),
            "cep": request.form.get("cep"),
            "rua": request.form.get("rua"),
            "bairro": request.form.get("bairro"),
            "cidade": request.form.get("cidade"),
            "estado": request.form.get("estado"),
            "numero": request.form.get("numero"),
            "complemento": request.form.get("complemento"),
            "pais": request.form.get("pais"),
            "data_nascimento": request.form.get("data_nascimento"),
            "sexo": request.form.get("sexo"),
        })

        return {"cliente": resultClient}, 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo cliente : " + str(e)
        print(str(e))
        return {"Erro": error_msg + str(e)}, 400
    

@app.route('/get_cliente', methods=['GET'])
def get_cliente():
    session = Session()
    clientes = session.query(Cliente)
    if not clientes:
        error_msg = "Não Existem Clientes cadastrados"
        return {"Erro": error_msg}, 404
    else:
        resultClient = []
        for cliente in clientes:
            resultClient.append({
                "nome": cliente.nome,
                "cpf": cliente.cpf,
                "rg": cliente.rg,
                "cep": cliente.cep,
                "rua": cliente.rua,
                "bairro": cliente.bairro,
                "cidade": cliente.cidade,
                "estado": cliente.estado,
                "numero": cliente.numero,
                "complemento": cliente.complemento,
                "pais": cliente.pais,
                "data_nascimento": cliente.data_nascimento.strftime("%d/%m/%Y"),
                "sexo": cliente.sexo,
            })

        return {"clientes": resultClient}, 200
    
@app.route('/get_cliente_por_cpf/<cpf>', methods=['GET'])
def get_cliente_por_cpf(cpf):
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.cpf == cpf).first()
    if not cliente:
        error_msg = "Não Existem Clientes cadastrados"
        return {"Erro": error_msg}, 404
    else:
        resultClient = []
        resultClient.append({
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "rg": cliente.rg,
            "cep": cliente.cep,
            "rua": cliente.rua,
            "bairro": cliente.bairro,
            "cidade": cliente.cidade,
            "estado": cliente.estado,
            "numero": cliente.numero,
            "complemento": cliente.complemento,
            "pais": cliente.pais,
            "data_nascimento": cliente.data_nascimento.strftime("%d/%m/%Y"),
            "sexo": cliente.sexo,
        })

        return {"cliente": resultClient}, 200
    
