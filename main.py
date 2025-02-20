from Model.tasks import *
from Model.comments import *
from Model.users import *

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

class Task(BaseModel):
    task: str
    deadline: str
    status: str

class Comment(BaseModel):
    comment: str
    idTask: int
    status: int

class User(BaseModel):
    name: str
    email: str 
    password: str
    status: int


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
    response = insertTask(task.task,task.deadline,task.status)
    return response
    

@app.put("/tasks/{task_id}")
def addTaskApi(task: Task,task_id: int):
    response = updateTask(task.task,task.deadline,task.status,task_id)
    return response

@app.delete("/tasks/{task_id}")
def addTaskApi(task_id: int):
    response = deleteTask(task_id)
    return response

@app.get("/comments")
def getCommentsAPI():
    response = getComments()
    return response

@app.post("/comments")
def addCommentApi(comment: Comment):
    response = insertComment(comment.comment,comment.idTask)
    return response

@app.put("/comments/{comment_id}")
def updateCommentApi(comment: Comment,comment_id: int):
    response = updateComment(comment.comment,comment_id)
    return response

@app.delete("/comments/{comment_id}")
def deleteCommentApi(comment_id: int):
    response = deleteComment(comment_id)
    return response
    

@app.get("/users")
def getCommentsAPI():
    response = getUsers()
    return response

@app.post("/users")
def addCommentApi(user: User):
    response = insertUser(user.name,user.email,user.password,user.status)
    return response


@app.put("/users/{user_id}")
def updateUserApi(user: User,user_id: int):
    response = updateUser(user.name,user_id)
    return response

@app.delete("/users/{user_id}")
def deleteUserApi(user_id: int):
    response = deleteUser(user_id)
    return response