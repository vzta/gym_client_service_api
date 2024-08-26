from fastapi import FastAPI, HTTPException, Query, Body
import psycopg2
from pathlib import Path
from typing import Optional, Annotated   
from datetime import date
from pydantic import BaseModel, Field
from connection import connection
import asyncpg
import pandas as pd
import asyncio
import streamlit as st

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

class ClientLift(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    personal_id: int
    bench_lifted: Optional[int]
    squat_lifted: Optional[int]
    deadlift_lifted: Optional[int]
    lift_date: date
    

@app.post("/CREATE_TABLES/")
async def create_table():
    conn = connection()
    cursor = conn.cursor()
    current_path = Path.cwd()
    # Create a new item in the database
    with open(f'{current_path}\SQL_Scripts.sql', 'r') as file:
        sql_commands = file.read()
        print(sql_commands)  # Add this line to confirm the file content

    
    cursor.execute(sql_commands)
    conn.commit()
    cursor.close()
    return {"message": f"Item created successfully"}


@app.get("/clientes/")
async def get_all_clients():
    conn = await connection()
    result = await conn.fetch("""select * from clients""")
    df = pd.DataFrame(result)
    return result
    await conn.close()


@app.post("/Insert_Client/")
async def create_item(Client: ClientRequest):
    # Create a new item in the database
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.clients (name, lastname, personal_id, birthdate) VALUES (%s, %s, %s, %s)",
                   (Client.name, Client.lastname, Client.personal_id, Client.birthdate))
    conn.commit()
    cursor.close()
    return {"message": f"Item created successfully"}


@app.delete("/Delete_Client/{client_id}")
async def delete_item(client_id: int):
    '''
    delete_item Delete clients from DB
    '''
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clients WHERE id = %s', (client_id,))

    conn.commit()
    cursor.close()
    return {"message": "User deleted"}


@app.post("/insert_lift/")
async def add_weight_lifting(Client: ClientLift):
    # Create a new item in the database
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO public.lifting_performance
     (  id,
        personal_id,
        bench_lifted,
        squat_lifted,
        deadlift_lifted,
        lift_date)
     VALUES (%s, %s, %s, %s, %s, %s)""",
                   (Client.id,
                    Client.personal_id,
                    Client.bench_lifted,
                    Client.squat_lifted,
                    Client.deadlift_lifted,
                    Client.lift_date
                    ))
    conn.commit()
    cursor.close()
    return {"message": f"Item Inserted successfully"}


