from fastapi import FastAPI

app = FastAPI()

llista_users=["valeria","paco","martina"]

# response_model=dict
# response_model=str
# @app.get(path:/hola", response_model=dict


@app.get("/users")
def read_root():
    return {"result": llista_users}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"message": user_id}

@app.post("/users")
def add_user():
    return {"message": "Aix es un post"}

@app.delete("/users/del")
def del_user():
    return {"message": "Aix es un post"}

