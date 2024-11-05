from fastapi import FastAPI
from api.otimazacao import  criar_modelo_inteiro 
import json
from api.ano import pesos
app = FastAPI()



@app.get('/quadro/')
def retorno(tempos_materia: str, ano):
    peso_ano = pesos(ano)
    if peso_ano =="Ano Inválido":
        return f"{ano} não é um ano válido"
    # Converte a string JSON para um dicionário
    try:
        tempos_materia = json.loads(tempos_materia)
    except json.JSONDecodeError:
        return {"error": "Formato JSON inválido"}
    
    materias = list(tempos_materia.keys())

    quadro = criar_modelo_inteiro(materias, tempos_materia, peso_ano)

    return quadro


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)


