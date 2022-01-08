from app import app
from flask import render_template



@app.get("/")
@app.get("/index")
def index():
    dados = {"profissao": "Development", "nome": "Gyl Monteiro" }
    return render_template("index.html", dados = dados)

@app.get("/contato")
def contato():
    return render_template("contato.html")