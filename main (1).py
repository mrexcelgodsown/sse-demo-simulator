from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import redis
import jwt
import uuid
from datetime import datetime, timedelta
import re  # For mock DLP scanning

app = FastAPI()
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

class Task(BaseModel):
    task: str

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
async def login(user: User):
    if user.username == "admin" and user.password = "password":
        token = jwt.encode({
            "sub": user.username,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/tasks")
async def enqueue_task(task: Task, user: str = Depends(get_current_user)):
    task_id = str(uuid.uuid4())
    redis_client.hset(f"task:{task_id}", mapping={
        "task": task.task,
        "status": "queued",
        "result": ""
    })
    redis_client.lpush("task_queue", task_id)
    return {"task_id": task_id, "status": "queued"}

@app.get("/tasks")
async def get_tasks(user: str = Depends(get_current_user)):
    tasks = []
    for key in redis_client.keys("task:*"):
        task = redis_client.hgetall(key)
        tasks.append(task)
    queue_length = redis_client.llen("task_queue")
    return {"tasks": tasks, "queue_length": queue_length}