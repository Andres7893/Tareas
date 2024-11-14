from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def read_root():
    
    respuesta = requests.get('https://game1.tecno1.site')  
    return {"message": "¿Cómo estás?", "respuesta": respuesta.json().get("message", "No se encontró el mensaje")}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)