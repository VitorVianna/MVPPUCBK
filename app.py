from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError
from model import Session, Cliente, Agenda, Profissional

app = Flask(__name__)


@app.route('/')
def home():
    session = Session()
    agenda = session.query(Agenda)
    return agenda
