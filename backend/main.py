from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)


@app.get("/")
def read_root():
    return {"test":"test_1"}

@app.get("/api/todo")
async def GetTodo():
    return 1

@app.get("/api/todo{id}")
async def GetTodoId(id):
    return 1

@app.post("/api/todo")
async def PostTodo(todo):
    return 1

@app.put("/api/todo{id}")
async def PutTodo(id, data):
    return 1

@app.delete("/api/todo{id}")
async def DeleteTodoID():
    return 1
