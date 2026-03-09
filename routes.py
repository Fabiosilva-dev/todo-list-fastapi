from fastapi import APIRouter
from models import Tarefas

router = APIRouter(tags=["Gerenciamento de Tarefas"])



lista_tarefas = []

contador_id = 1


#CREATE
@router.post("/tarefas")
def adicionar_tarefa(tarefa:Tarefas):

    global contador_id

    novo = {
        "id":contador_id,
        "titulo":tarefa.titulo
    }
    lista_tarefas.append(novo)
    contador_id += 1 
    return novo


#READ
@router.get("/tarefas")
def listar_tarefas():
    return lista_tarefas


#READ - buscar por id
@router.get("/tarefas/{id}")
def mostrar_tarefa(id:int):
    for tarefa in lista_tarefas:
        if tarefa["id"] == id :
            return tarefa
        

#UPDATE
@router.put("/tarefas/{id}")
def atualizar_tarefa(id:int,tarefa_atualizada:Tarefas):
    
    for tarefa in lista_tarefas:
        if tarefa["id"] == id :
            tarefa["titulo"] = tarefa_atualizada.titulo
            return tarefa
    return {"Mensagem":"tarefa não encontrada"}


#DELETE
@router.delete("/tarefas/{id}")
def deletar_tarefa(id:int):
    for tarefa in lista_tarefas:
        if tarefa["id"] == id :
            lista_tarefas.remove(tarefa)
            return {"mensagem":"Tarefa deletada"}
    return {"mensagem":"Tarefa não encontrada"}