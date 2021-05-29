from uuid import uuid4
from datetime import date
import psycopg2
from envparse import Env


conn_str = Env().str('db_conn_str')
conn = psycopg2.connect(conn_str)
cursor = conn.cursor()


class Order:

    def __init__(self, order_type, description, serial, creator_id, status='new'):
        self.status = status
        self.creator_id = creator_id
        self.description = description
        self.order_type = order_type
        self.serial = serial
        self.__id = uuid4().hex
        self.time_create = date.today()
        data_insert = """
            INSERT INTO orders 
            (created_dt, order_type, description, serial_no, creator_id, status)
            VALUES (%s, %s, %s, %s, %s, %s) 
            RETURNING order_id
            """
        fields = (self.time_create, self.order_type, self.description, self.serial, self.creator_id, self.status)
        with conn, conn.cursor() as cursor:
            cursor.execute(data_insert, fields)
            self.order_id = cursor.fetchone()[0]

    def in_active(self):
        if self.status == "not_active":
            return "This Order not active"
        x = date.today() - self.time_create
        return f"Order is active {x.days} days."

    def change_status(self, new_status):
        self.status = new_status
        data_insert = """UPDATE orders SET status = %s, updated_dt = %s WHERE order_id=%s"""
        fields = (self.status, date.today(), self.order_id)
        with conn, conn.cursor() as cursor:
            cursor.execute(data_insert, fields)

    def change_description(self, new_description):
        self.description = new_description
        data_insert = """UPDATE orders SET description = %s, updated_dt = %s WHERE order_id=%s"""
        fields = (self.description, date.today(), self.order_id)
        with conn, conn.cursor() as cursor:
            cursor.execute(data_insert, fields)

    def changr_creator(self, new_creator):
        self.creator_id = new_creator
        data_insert = """UPDATE orders SET creator_id = %s, updated_dt = %s WHERE order_id = %s"""
        fields = (new_creator, date.today(), self.order_id)
        with conn, conn.cursor() as cursor:
            cursor.execute(data_insert, fields)

    def order_id(self):
        return f"Order id is: {self.__id}"


class Department:

    def __init__(self, department_name):
        self.name = department_name
        data_insert = """
        INSERT INTO  departments (department_name) 
        VALUES (%s) RETURNING department_id
        """
        with conn, conn.cursor() as cursor:
            cursor.execute(data_insert, (department_name, ))
            self.department_id = cursor.fetchone()[0]


class Employees:

    def __init__(self,  fio, position, department_id):
        self.fio = fio
        self.position = position
        self.department_id = department_id
        with conn, conn.cursor() as cursor:
            data_insert = """INSERT INTO employees (fio, position, department_id) VALUES (%s, %s, %s) RETURNING employee_id"""
            fields = (self.fio, self.position, self.department_id)
            cursor.execute(data_insert, fields)
            self.employee_id = cursor.fetchone()[0]






# x = Order('garent', 'broken all', 66666, 2)
# print(x.order_id)
# x.changr_creator(1)
# y=Department('dfdf')
# print(y.department_id)
z = Employees("Harry Potter", "office mad", 1)
print(z.employee_id)