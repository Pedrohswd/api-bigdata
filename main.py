from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
import os

# Configuração do banco de dados
DATABASE_URL = "postgresql://bigdata_54j0_user:tJHdvyNQk5p4uZZbrn7sB4aR6KjRxqhT@dpg-cvli47ggjchc738i9g10-a.oregon-postgres.render.com:5432/bigdata_54j0"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para buscar dados tratados
@app.get("/dados")
def get_dados(db: Session = Depends(get_db)):
    query = text("SELECT * FROM tomada_inteligente")  # Substitua pelo nome correto da tabela
    result = db.execute(query)
    dados = [dict(row._mapping) for row in result]
    return {"dados": dados}

@app.get("/dados/monitor")
def get_dados(db: Session = Depends(get_db)):
    query = text("SELECT * FROM tomada_inteligente WHERE identificador_tomada = 'MONITOR'")  # Substitua pelo nome correto da tabela
    result = db.execute(query)
    dados = [dict(row._mapping) for row in result]
    return {"dados": dados}

@app.get("/dados/geladeira")
def get_dados(db: Session = Depends(get_db)):
    query = text("SELECT * FROM tomada_inteligente WHERE identificador_tomada = 'GELADEIRA'")  # Substitua pelo nome correto da tabela
    result = db.execute(query)
    dados = [dict(row._mapping) for row in result]
    return {"dados": dados}

# Rota de teste
@app.get("/")
def read_root():
    return {"mensagem": "API de Dashboards funcionando!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    