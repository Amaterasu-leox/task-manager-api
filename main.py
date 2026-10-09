from fastapi import FastAPI

app = FastAPI(title="Task Manager API")


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API Task Manager !"}


@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Installer FastAPI", "completed": True},
        {"id": 2, "title": "Créer les routes de l'API", "completed": False},
    ]
