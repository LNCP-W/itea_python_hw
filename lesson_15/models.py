from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("my_app")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/postgres"
db = SQLAlchemy(app)


class Departments(db.Model):
    d_id = db.Column(db.Integer, primary_key=True)
    d_name = db.Column(db.String(50), unique=True, nullable=False)
    d_location = db.Column(db.String(50), nullable=False)
    d_phone = db.Column(db.Integer)

    def __str__(self):
        return f"Department {self.d_name} with id:{self.d_id} located in {self.d_location}"

    def __repr__(self):
        res = {
            "id": self.d_id,
            "name": self.d_name,
            "location": self.d_location,
            "phone": self.d_phone
            }
        return str(res)


class Employees(db.Model):
    e_id = db.Column(db.Integer, primary_key=True)
    e_name = db.Column(db.String(50), unique=True, nullable=False)
    e_position = db.Column(db.String(50), nullable=False)
    e_phone = db.Column(db.Integer, nullable=False)
    e_dep_id = db.Column(db.Integer, db.ForeignKey('departments.d_id'), nullable=False)

    def __str__(self):
        return f"Employee {self.e_name} with id:{self.e_id} worked on position {self.e_position} " \
               f"in department {self.e_dep_id}, phone number: {self.e_phone}."

    def __repr__(self):
        res = {
               "id": self.e_id,
               "name": self.e_name,
               "position": self.e_position,
               "phone": self.e_phone,
               "department_id": self.e_dep_id
               }
        return str(res)


class Clients(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(50), unique=True, nullable=False)
    c_phone = db.Column(db.Integer, nullable=False)
    c_is_problem = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"Client {self.c_name}{'!!!'*bool(self.c_is_problem)} with id:{self.c_id}, phone number: {self.c_phone}."

    def __repr__(self):
        res = {
               "id": self.c_id,
               "name": self.c_name,
               "phone": self.c_phone,
               "problem":self.c_is_problem
               }
        return str(res)


class Orders(db.Model):
    o_id = db.Column(db.Integer, primary_key=True)
    o_created = db.Column(db.DateTime)
    o_status = db.Column(db.String(50), nullable=False)
    o_type = db.Column(db.String(50), nullable=False)
    o_descript = db.Column(db.String(200), nullable=False)
    o_creator = db.Column(db.Integer, db.ForeignKey("employees.e_id"), nullable=False)
    o_serial = db.Column(db.String(20), nullable=False)
    o_price = db.Column(db.Integer)
    o_client = db.Column(db.Integer, db.ForeignKey("clients.c_id"), nullable=False)

    def __str__(self):
        return f"Order was created {self.o_created} by employee {str(self.o_creator)}. " \
               f"Actual status is {self.o_status}, type: {self.o_type}, description: {self.o_descript}, " \
               f"serial number: {self.o_serial}, last update: ."

    def __repr__(self):
        res = {
              "id": {self.o_id},
              "created": {self.o_created},
              "status": {self.o_status},
              "type": {self.o_type},
              "description": {self.o_descript},
              "creator": {self.o_creator},
              "serial": {self.o_serial},
              "price": {self.o_price},
              "client": {self.o_client}
              }
        return str(res)


# db.create_all()
