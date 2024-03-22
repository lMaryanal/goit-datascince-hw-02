import psycopg2
from IPython.display import display
import pandas as pd

status = """CREATE TABLE status(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);"""

users = """CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);"""

tasks = """CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
);"""

with psycopg2.connect(
    database="", user="postgres",
    password="472vx7rty", host="localhost", port=5432 
) as connection:
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS tasks;")
    cursor.execute("DROP TABLE IF EXISTS status;")
    cursor.execute("DROP TABLE IF EXISTS users;")
    cursor.execute(status)
    cursor.execute(users)
    cursor.execute(tasks)
    connection.commit()


# connection.close()
# cursor.close()
