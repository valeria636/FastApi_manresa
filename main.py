#
from fastapi import FastAPI
from typing import List

app = FastAPI()

# Llista inicial d'usuaris amb un nom i ID
users = [{"id": 1, "name": "valeria"}]

# Model per a rebre un usuari nou
# Obtenir tots els usuaris
@app.get("/users")
def read_users():
    return {"result": users}

# Afegir un nou usuari
@app.post("/api/users")
def add_user(user: users):  # Rebem un objecte 'user' del model 'User'
    new_id = len(users) + 1
    new_user = {"id": new_id, "name": user.name}
    users.append(new_user)
    return {"users": users}

# Obtenir un usuari pel seu ID
@app.get("/api/users/{id}")
def get_user(id: int):
    for user in users:
        if user["id"] == id:
            return {"result": user}
    return {"error": "User not found"}
