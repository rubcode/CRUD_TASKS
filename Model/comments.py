from .statement import *

def getComments():
    query = "SELECT * FROM comments";
    tasks = selectData(query)
    return tasks

def insertComment(comment,idTask,status=1):
    query  = "INSERT INTO comments (comment, id_task,status) VALUES(%s,%s,%s)"
    values = (comment,idTask,status)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Comentario insertado correctamente"}
    return response

def updateComment(comment,ID):
    query  = "UPDATE comments SET comment = %s WHERE id = %s"
    values = (comment,ID)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Comentario actualizada correctamente"}
    return response

def deleteComment(ID):
    query  = "DELETE FROM comments WHERE id= %s"
    values = (ID,)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Comentario eliminada correctamente"}
    return response
