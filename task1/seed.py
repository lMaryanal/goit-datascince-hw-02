import faker
from random import randint, choice
import psycopg2
import pandas as pd

NUMBER_USERS = 20
STATUS_NAME = [('new',), ('in progress',), ('completed',)]
NUMBER_OF_TASKS = 50
def generate_fake_data(number_users, number_tasks, status_name) -> tuple():
    fake_users = []
    fake_titles = []
    fake_descriptions = []
    fake_emails = []
    fake_data = faker.Faker()


    for _ in range(number_users):
        fake_users.append(fake_data.name())
        fake_emails.append(fake_data.email())

    for _ in range(number_tasks):
        fake_titles.append(fake_data.sentence(nb_words=5))
        if randint(0, 4):
            fake_descriptions.append(fake_data.paragraph(nb_sentences=3))
        else:
            fake_descriptions.append(None)

    return fake_users, fake_titles, fake_descriptions, status_name, fake_emails

def prepare_data(users, titles, descriptions, status_name, emails) -> tuple():
    for_status = []

    for status in status_name:
        for_status.append((status))

    for_users = []

    for user, email in zip(users, emails):
        for_users.append((user, email))

    for_tasks = []

    for title, description in zip(titles, descriptions):
        for_tasks.append((title, description, randint(1, len(STATUS_NAME)), randint(1, NUMBER_USERS)))

    return for_users, for_tasks, for_status


def insert_data_to_db(users, tasks, status) -> None:

    with psycopg2.connect(
    database="", user="postgres",
    password="472vx7rty", host="localhost", port=5432 
) as con:

        cur = con.cursor()

        sql_to_status = """INSERT INTO status(name)
                               VALUES (%s)"""

        cur.executemany(sql_to_status, status)

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (%s, %s)"""

        cur.executemany(sql_to_users, users)


        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (%s, %s, %s, %s)"""


        cur.executemany(sql_to_tasks, tasks)

        con.commit()

if __name__ == "__main__":
    users, tasks, status = prepare_data(*generate_fake_data(NUMBER_USERS, NUMBER_OF_TASKS, STATUS_NAME))
    insert_data_to_db(users, tasks, status)

