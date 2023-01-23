#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn 3_crud:app --reload-
#{"id"="3","Name":"Alfredo", "LastName":"Garcia", "Age":"30"}
#Definimos nuestra entidad: user

class User(BaseModel):
    PassangerId:int
    Survived:int
    Pclass:int
    Name:str
    Sex:str
    Age:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(PassangerId=1,Survived=0,Pclass=3,Name="Braund, Mr. Owen Harris", Sex="male", Age=22),
            User(PassangerId=2,Survived=1,Pclass=1,Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Sex="female", Age=38),
            User(PassangerId=3,Survived=1,Pclass=3,Name="Heikkinen, Miss. Laina", Sex="female", Age=26),
            User(PassangerId=4,Survived=1,Pclass=1,Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", Sex="female", Age=35),
            User(PassangerId=5,Survived=0,Pclass=3,Name="Allen, Mr. William Henry", Sex="male", Age=35),
            User(PassangerId=6,Survived=0,Pclass=3,Name="Moran, Mr. James", Sex="male", Age=24),
            User(PassangerId=7,Survived=0,Pclass=1,Name="McCarthy, Mr. Timothy J", Sex="male", Age=54),
            User(PassangerId=8,Survived=0,Pclass=3,Name="Palsson, Master. Gosta Leonard", Sex="male", Age=2),
            User(PassangerId=9,Survived=1,Pclass=3,Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)", Sex="female", Age=27),
            User(PassangerId=10,Survived=1,Pclass=2,Name="Nasser, Mrs. Nicholas (Adele Achem)", Sex="female", Age=14),
            User(PassangerId=11,Survived=1,Pclass=3,Name="Sandstrom, Miss. Marguerite Rut", Sex="female", Age=4),
            User(PassangerId=12,Survived=1,Pclass=1,Name="Bonnell, Miss. Elizabeth", Sex="female", Age=58),
            User(PassangerId=13,Survived=0,Pclass=3,Name="Saundercock, Mr. William Henry", Sex="male", Age=20),
            User(PassangerId=14,Survived=0,Pclass=3,Name="Andersson, Mr. Anders Johan", Sex="male", Age=39),
            User(PassangerId=15,Survived=0,Pclass=3,Name="Vestrom, Miss. Hulda Amanda Adolfina", Sex="female", Age=14),
            User(PassangerId=16,Survived=1,Pclass=2,Name="Hewlett, Mrs. (Mary D Kingcome) ", Sex="female", Age=55),
            User(PassangerId=17,Survived=0,Pclass=3,Name="Rice, Master. Eugene", Sex="male", Age=2),
            User(PassangerId=18,Survived=1,Pclass=2,Name="Williams, Mr. Charles Eugene", Sex="male", Age=5),
            User(PassangerId=19,Survived=0,Pclass=3,Name="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)", Sex="female", Age=31),
            User(PassangerId=20,Survived=1,Pclass=3,Name="Masselmani, Mrs. Fatima", Sex="female", Age=5),
            User(PassangerId=21,Survived=0,Pclass=2,Name="Fynney, Mr. Joseph J", Sex="male", Age=35),
            User(PassangerId=22,Survived=1,Pclass=2,Name="Beesley, Mr. Lawrence", Sex="male", Age=34),
            User(PassangerId=23,Survived=1,Pclass=3,Name="McGowan, Miss. Anna (Annie)", Sex="female", Age=15),
            User(PassangerId=24,Survived=1,Pclass=1,Name="Sloper, Mr. William Thompson", Sex="male", Age=28),
            User(PassangerId=25,Survived=0,Pclass=3,Name="Palsson, Miss. Torborg Danira", Sex="female", Age=8), 
             ]


#***Get
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#***Get con Filtro Path
@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


#***Get con Filtro Query
@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#***Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
    for index, saved_user in enumerate(users_list):
        if saved_user.PassangerId == user.PassangerId:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   
   
    #***Put
#@app.put("/usersclass/")
#async def usersclass(user:User):
    
#    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
#    for index, saved_user in enumerate(users_list):
#        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
#           users_list[index] = user  #accedemos al indice de la lista que hemos encontrado y actualizamos con el nuevo usuario
#           found=True
           
#    if not found:
#        return {"error":"No se ha actualizado el usuario"}
#    else:
#        return user
    
    #http://127.0.0.1:8000/usersclass/
    
    
        #***Delete
#@app.delete("/usersclass/{id}")
#async def usersclass(id:int):
    
 #   found=False     #Usamos bandera found para verificar si hemos encontrado el usuario 
    
 #   for index, saved_user in enumerate(users_list):
#      if saved_user.id ==id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
#           del users_list[index]  #Eliminamos al indice de la lista que hemos encontrado 
#           found=True
#           return "El registro se ha eliminado"
       
#    if not found:
#        return {"error":"No se ha eliminado el usuario"}
    
    #http://127.0.0.1:8000/usersclass/1