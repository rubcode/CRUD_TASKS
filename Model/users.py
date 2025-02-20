from .statement import *
import bcrypt



def getUsers():
    query = "SELECT id_user,name, email, status FROM users";
    tasks = selectData(query)
    return tasks

def insertUser(name, email,password,status=1):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    query  = "INSERT INTO users (name, email,password, status) VALUES(%s,%s,%s,%s)"
    values = (name,email,hashed_password,status)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Usuario insertado correctamente"}
    return response

def updateUser(name,ID):
    query  = "UPDATE users SET name = %s WHERE id_user = %s"
    values = (name,ID)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Usuario actualizado correctamente"}
    return response

def deleteUser(ID):
    query  = "DELETE FROM users WHERE id_user= %s"
    values = (ID,)
    response = excuteStatement(query,values)
    if(response['code'] == "000"):
        return {"code": "000","description": "Usuario eliminado correctamente"}
    return response


def verify_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))