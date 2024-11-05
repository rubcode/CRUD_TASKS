from .statement import *
import json



def getTaks():
    query = "SELECT * FROM tasks";
    tasks = selectData(query)
    return tasks

def insertTask(task, deadline):
    query  = "INSERT INTO tasks (task, deadline) VALUES(%s,%s)"
    values = (task,deadline)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Tarea insertada correctamente"}
    return response

def updateTask(task,deadline,ID):
    query  = "UPDATE tasks SET task = %s, deadline= %s WHERE id = %s"
    values = (task,deadline,ID)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Tarea actualizada correctamente"}
    return response

def deleteTask(ID):
    query  = "DELETE FROM tasks WHERE id= %s"
    values = (ID,)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Tarea eliminada correctamente"}
    return response
