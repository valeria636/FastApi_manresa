from fastapi import FastAPI

app = FastAPI()
users = ["valeria"]

@app.post("/api/users/{id}", response_model=dict)
def add_user(id: str):
    users.append(id)
    diccionari = dict(zip(users, range(len(users))))
    return diccionari

@app.get("/api/users/{id}", response_model=dict)
def get_user(id: int):
    if 0 <= id < len(users):
        return {"user": users[id]}
    else:
        return {"error": "User not found"}

@app.put("/api/users/{id}", response_model=dict)
def update_user(id: int, updated_user: str):
    if 0 <= id < len(users):
        users[id] = updated_user
        return {"updated": updated_user}
    else:
        return {"error": "User not found"}

@app.delete("/api/usuaris/{id}", response_model=dict)
def delete_user(id: int):
    if 0 <= id < len(users):
        deleted = users.pop(id)
        diccionari = dict(zip(users, range(len(users))))
        return {"deleted": deleted, "users": diccionari}
    else:
        return {"error": "User not found"}
