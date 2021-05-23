import psycopg2
from psycopg2 import sql
from datetime import datetime

conn = psycopg2.connect("postgres://postgres:StrongPassword@localhost:5432/order_service_db")
cursor = conn.cursor()


def create_tb(tab_to_create):
    with conn, conn.cursor() as cursor:
        for i in tab_to_create:
            cursor.execute(i)


def add_some(table, columns, val):
    with conn, conn.cursor() as cursor:
        many_arg = ("%s, " * len(columns.split()))[:-2]  # опрределяет количество аргументовдля вставки %s
        for i in val:
            sql1 = sql.SQL(f"INSERT INTO {table} ({columns}) VALUES ({many_arg})")
            cursor.execute(sql1, i)


def add_department(dep):
    add_some('departments', 'department_name', dep)


def add_employee(empl):
    add_some("employees", "fio, position, department_id", empl)


def add_order(order, time=datetime.now()):
    for i in order:
        i.insert(0, time)
    add_some(
        "orders",
        "created_dt, order_type, description, status, serial_no, creator_id",
        order)


create = [
    """CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name TEXT NOT NULL
    );""",

    """CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    fio TEXT NOT NULL,
    position TEXT NOT NULL,
    department_id INTEGER NOT NULL,
    FOREIGN KEY (department_id) REFERENCES departments (department_id)
    );""",

    """CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    created_dt TIMESTAMP NOT NULL,
    updated_dt TEXT,
    order_type TEXT NOT NULL,
    description TEXT NOT NULL,
    status TEXT NOT NULL,
    serial_no INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES employees (employee_id)
    );"""
    ]

create_tb(create)

departments = [
  ["Central office", ],
  ["Lviv department", ],
  ["Odesa department", ],
  ["Kyiv department", ]
    ]

add_department(departments)

employees = [
    ['Ivanov Ivan', 'Big Boss', 1],
    ['Petrenko Petro', 'Central Manager', 1],
    ['Levko Lev', 'Small Boss', 2],
    ['Pavlovskyi Pavlo', 'Local Manager', 2],
    ['Andtienko Andrii', 'Local Engineer', 2],
    ['Klymenko Klym', 'Small Boss', 3],
    ['Ignatenko Ignat', 'Local Manager', 3],
    ['Yurchenko Yurii', 'Local Engineer', 3],
    ['Hordiyenko Hordij', 'Small Boss', 4],
    ['Ostapcuk Ostap', 'Local Manager', 4],
    ['Semenov Semen', 'Local Engineer', 4]
    ]

add_employee(employees)

orders = [
    ['paid', 'no sound', 'new', 13254351, 4],
    ['paid', 'no vibro', 'new', 53843535, 4],
    ['garant', 'water damage', 'new', 643543973, 7],
    ['paid', 'low battary', 'new', 567863434, 7],
    ['garant', 'broken screan', 'new', 374139876, 10],
    ['paid', 'silent speaker', 'again', 74319896, 10],
    ['paid', 'no charge', 'new', 13543347, 4],
    ['garant', 'broken camera', 'again', 3654349, 10],
    ['paid', 'button stuck', 'new', 345733531, 7],
    ['paid', 'paypass fail', 'new', 35473357, 7],
    ['paid', 'broken screan', 'new', 79456933, 4],
    ['paid', 'water damage', 'new', 6983451, 4],
    ['paid', 'no charge', 'new', 687743354, 10],
    ['garant', 'no vibro', 'again', 53843535, 10]
    ]

add_order(orders)

result1 = cursor.execute("""SELECT * FROM orders 
    WHERE status='new' a
    nd creator_id=4 
    and created_dt 
    BETWEEN '2021-05-23' and now()""")
for row in cursor.fetchall():
    print(row)

result2 = cursor.execute("""SELECT fio, position, department_name 
    FROM employees LEFT JOIN departments ON employees.department_id=departments.department_id 
    ORDER BY fio""")
for row in cursor.fetchall():
    print(row)

result3 = cursor.execute("SELECT * FROM orders WHERE status='again' ORDER BY created_dt")
for row in cursor.fetchall():
    print(row)
