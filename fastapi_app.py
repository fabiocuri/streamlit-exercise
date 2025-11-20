from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for demo purposes
items = {}

# Pydantic model for request body validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    quantity: int = 0

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message"""
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/items/")
async def create_item(item: Item):
    """POST endpoint to create a new item"""
    return {"item_id": "hola", "endereco": "caldas", "nome": "oi"}