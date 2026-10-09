from fastapi import FastAPI

app = FastAPI()


#- - - - - - - - - - PATH OPERATIONS - - - - - - - -- #


# DUMMEY USER DATA
user_data = [
    {
        "id":1,
        "name":"Santosh",
        "email":"santosh@mail.com"
    },
    {
        "id":2,
        "name":"Anirudh",
        "email":"anirudh@mail.com"
    }
]


# GET
@app.get('/users')
def get_all_users():
    return user_data

# POST
@app.post('/add-user/')
def add_user_data(user:dict):
    user_data.append(user)
    return {"message" : "Added user data to list"}


# PUT
@app.put("/update-user/{id}")
def update_user_data(id:int, user:dict):
    for i in user_data:
        if i["id"] == id:
            i.update(user)
            return {"message": "user update successfully"}
    else:
        return {"message": "user not found"}


# PATCH
@app.patch("/update-email/{id}")
def update_email(id:int, email:str):
    for i in user_data:
        if i["id"] == id:
            i["email"] = email
            return {"message": "email updated"}
    else:
        return {"message": "user not found"}


# DELETE
@app.delete("/delete-user/")
def delete_user_data(id:int):
    for i in user_data:
        if i["id"] == id:
            user_data.remove(i)
            return {"message": "user deleted"}
    else:
            return {"message": "user not found"}