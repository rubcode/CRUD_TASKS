from Model.tasks import *

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


class Task(BaseModel):
    task: str
    deadline: str

app = FastAPI()

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