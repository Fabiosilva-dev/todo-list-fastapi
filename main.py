from fastapi import FastAPI
from routes import router


app = FastAPI(
    title="ToDo List API",
    description="""
    API simples para gerenciamento de tarefas criada com FastAPI.
    
    Funcionalidades: 
    -Criar tarefas
    -Listar tarefas
    -Buscar tarefas por ID
    -Atualizar tarefas 
    -Deletar tarefas
    """,
    version="1.0.0"
)

app.include_router(router)


#python -m pip freeze > requirements.txt
