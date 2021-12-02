from typing import Collection
from model import Todo
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb//localhost:27017")
database = client.TodoList
Collection = database.Todo




async def fetchOneTodo(title):
    document = await Collection.find_one({"title":title})
    return document