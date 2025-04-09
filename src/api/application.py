from fastapi import FastAPI
from src.api.configuration import configure_db, configure_routes

def create_app():
    app = FastAPI()

    #Incluir rotas
    configure_routes(app)

    #Inicializar db/tortoise
    configure_db(app)
    
    return app

app = create_app()