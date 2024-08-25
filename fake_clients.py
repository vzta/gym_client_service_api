from faker import Faker
from connection import connection

fake = Faker()

conn = connection()
with conn.cursor() as cursor:
    # Insert fake subscribers
    for _ in range(10):
        name = fake.name()
        lastname = fake.name()
        dni = fake.random_int(min=4000, max=300000)
        email = fake.email()
        phone_number = fake.phone_number()
        query = cursor.mogrify(
            "INSERT INTO clients (nombre, apellido, dni, email, celular) VALUES (%s, %s, %s, %s, %s)",
            (name, lastname, dni, email, phone_number)
        )
        cursor.execute(query)
        
# Insert fake subscription plans
    for _ in range(5):
        plan_name = fake.word()
        description = fake.text()
        duration = fake.random_int(min=1, max=12)
        price = fake.random_number(digits=3)
        cursor.execute(
            "INSERT INTO gym.subscription_plans (plan_name, description, duration, price) VALUES (%s, %s, %s, %s)",
            (plan_name, description, duration, price)
        )

# Commit the changes
conn.commit()

# Close the connection
conn.close()
