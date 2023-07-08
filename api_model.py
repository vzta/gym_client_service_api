from fastapi import FastAPI
import psycopg2
from typing import Optional
from datetime import date
from pydantic import BaseModel, Field

app = FastAPI()

class Cliente:
    id: int
    name: str
    lastname: str
    personal_id: int
    birthdate: date
    age: int
    disseases: str
    weight: float
    height: float
    sex: str
    cellphone: str
    email: str


    def __init__(self, id, name, lastname, personal_id, birthdate, age, disseases, weight, height, sex, cellphone, email ):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.personal_id = personal_id
        self.birthdate = birthdate
        self.age = age
        self.disseases = disseases
        self.weight = weight
        self.height = height
        self.sex = sex
        self.cellphone = cellphone
        self.email = email
        
class ClientRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    name: str
    lastname: str
    personal_id: int
    birthdate: Optional[date]
    age: Optional[int]
    disseases: Optional[str]
    weight: Optional[float]
    height: Optional[float]
    sex: Optional[str]
    cellphone: Optional[str]
    email: Optional[str]


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="asarasa12"
)

@app.get("/clientes/")
async def get_all_clients():
    cursor = conn.cursor()
    cursor.execute("select * from gym.clientes")
    result = cursor.fetchall()
    cursor.close()

    return result

@app.post("/Insert_Client/")
async def create_item(Client: ClientRequest):
    # Create a new item in the database
    cursor = conn.cursor()
    cursor.execute("INSERT INTO gym.clientes (nombre, apellido, dni) VALUES (%s, %s, %s)",
                   (Client.name, Client.lastname, Client.personal_id))
    conn.commit()
    cursor.close()
    return {"message": "Item created successfully"}
