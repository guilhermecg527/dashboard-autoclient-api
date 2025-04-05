# main.py
from fastapi import FastAPI
from models import Abordagem

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API do Dashboard AutoClient está funcionando!"}

@app.post("/abordagem")
def receber_abordagem(dados: Abordagem):
    # Aqui você poderia salvar no banco, enviar para uma fila, etc.
    return {
        "mensagem": "Abordagem recebida com sucesso.",
        "lead": dados.nome_lead,
        "telefone": dados.telefone,
        "cliente_id": dados.cliente_id
    }
