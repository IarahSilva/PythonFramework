from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from passlib.context import CryptContext

app = FastAPI(title="API de autenticação didática")
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
usuarios = {}  # Em memória: os dados somem ao reiniciar.

class Credenciais(BaseModel):
    usuario: str = Field(min_length=3, max_length=40, pattern=r"^[a-zA-Z0-9_.-]+$")
    senha: str = Field(min_length=12, max_length=72)

@app.post("/cadastro", status_code=201)
def cadastro(d: Credenciais):
    if d.usuario in usuarios: raise HTTPException(409, "Usuário já existe.")
    usuarios[d.usuario] = pwd.hash(d.senha)
    return {"mensagem": "Cadastro realizado."}

@app.post("/login")
def login(d: Credenciais):
    hash_salvo = usuarios.get(d.usuario)
    if not hash_salvo or not pwd.verify(d.senha, hash_salvo):
        raise HTTPException(401, "Credenciais inválidas.")
    return {"mensagem": "Login realizado."}

@app.get("/health")
def health(): return {"status": "ok"}
