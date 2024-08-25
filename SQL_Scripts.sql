CREATE TABLE IF NOT EXISTS public.clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    personal_id INT UNIQUE NOT NULL,
    birthdate DATE NOT NULL,
    age INT,
    cellphone VARCHAR(20),
    email VARCHAR(255) UNIQUE
);


CREATE TABLE IF NOT EXISTS public.status (
    id SERIAL PRIMARY KEY,
    personal_id INT UNIQUE NOT NULL,
    diseases TEXT,
    weight FLOAT,
    height FLOAT,
    sex VARCHAR(10)
);