from Model.tasks import *

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

class Task(BaseModel):
    task: str
    deadline: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

@app.get("/")
def bienvenida():
    return {"message":"Bienvenido"}

@app.get("/tasks")
def getTasksAPI():
    response = getTaks()
    return response

@app.post("/tasks")
def addTaskApi(task: Task):
    response = insertTask(task.task,task.deadline)
    return response
    

@app.put("/tasks/{task_id}")
def addTaskApi(task: Task,task_id: int):
    response = updateTask(task.task,task.deadline,task_id)
    return response

@app.delete("/tasks/{task_id}")
def addTaskApi(task_id: int):
    response = deleteTask(task_id)
    return response