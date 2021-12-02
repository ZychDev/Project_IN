import collections
from typing import Collection
from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb//localhost:27017")
database = client.TodoList
Collection = database.Todo




async def fetchOneTodo(title):
    document = await Collection.find_one({"title":title})
    return document

async def Fetch_Todo():
    todos = []
    cursor - Collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collections.insert_one(document)
    return document

async def update_todo(title, desc):
    await collections.update_one({"title":title}, {"$set":{"description":desc}})
    document = await collections.find_one({"tittle":title})
    return document

async def remove_todo(title):
    await collections.delete_one({"tittle":title})
    return True 