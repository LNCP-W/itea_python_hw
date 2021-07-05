from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("my_app")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost/postgres"
db = SQLAlchemy(app)


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer)

    def __str__(self):
        return f"Department {self.name} with id:{self.id} located in {self.location}"

    def __repr__(self):
        res = {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "phone": self.phone
            }
        return str(res)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    dep_id = db.Column(db.Integer, db.ForeignKey('departments.id', ondelete='CASCADE'), nullable=False)

    def __str__(self):
        return f"Employee {self.name} with id:{self.id} worked on position {self.position} " \
               f"in department {self.dep_id}, phone number: {self.phone}."

    def __repr__(self):
        res = {
               "id": self.id,
               "name": self.name,
               "position": self.position,
               "phone": self.phone,
               "department_id": self.dep_id
               }
        return str(res)


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    status = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    descript = db.Column(db.String(200), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey("employees.id", ondelete='CASCADE'), nullable=False)
    serial = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Integer, default=0)
    updated = db.Column(db.DateTime)

    def __str__(self):
        return f"Order was created {self.created} by employee {str(self.creator)}. " \
               f"Actual status is {self.status}, type: {self.type}, description: {self.descript}, " \
               f"serial number: {self.serial}, last update: ."

    def __repr__(self):
        price = self.price
        if not self.price:
            price = ''
        res = {
              "id": self.id,
              "created": self.created.strftime('%d.%m.%Y %H:%M'),
              "status": self.status,
              "type": self.type,
              "description": self.descript,
              "creator": self.creator,
              "serial": self.serial,
              "price": price,
              }
        return str(res)


@app.route("/create_dep")
def create_dep():
    print(request.args)
    new_dep = Departments(**request.args)
    db.session.add(new_dep)
    db.session.commit()
    return str(new_dep)


@app.route('/edit_department', methods=["GET"])
def edit_department():
    dep = Departments.query.filter_by(id=request.args["id"]).first()
    dep.name = request.args["name"]
    dep.location = request.args["location"]
    dep.phone = request.args["phone"]
    db.session.commit()
    return str(dep)


@app.route("/delete_dep")
def delete_dep():
    dep = Departments.query.filter_by(id=request.args['id']).first()
    db.session.delete(dep)
    db.session.commit()
    return f"Департамент №{request.args['id']} удален"


@app.route('/search_dep', methods=["GET"])
def search_dep():
    return Departments.query.filter_by(id=request.args['id']).first(),


@app.route("/create_emp")
def create_emp():
    new_emp = Employees(**request.args)
    db.session.add(new_emp)
    db.session.commit()
    return str(new_emp)


@app.route('/edit_employee', methods=["GET"])
def edit_employee():
    emp = Employees.query.filter_by(id=request.args["id"]).first()
    emp.name = request.args["name"]
    emp.position = request.args["position"]
    emp.phone = request.args["phone"]
    emp.dep_id = request.args["dep_id"]
    db.session.commit()
    return str(emp)


@app.route("/delete_emp")
def delete_emp():
    emp = Employees.query.filter_by(id=request.args['id']).first()
    db.session.delete(emp)
    db.session.commit()
    return f"Сотрудник №{request.args['id']} удален"


@app.route('/search_emp', methods=["GET"])
def search_emp():
    return Employees.query.filter_by(id=request.args['id']).first()


@app.route("/create_ord")
def create_ord():
    date = {'created': datetime.datetime.now(), 'updated': datetime.datetime.now()}
    date.update(**request.args)
    new_ord = Orders(**date)
    db.session.add(new_ord)
    db.session.commit()
    return str(new_ord)


@app.route('/edit_order', methods=["GET"])
def edit_order():
    order = Orders.query.filter_by(id=request.args["id"]).first()
    order.creator = request.args["creator"]
    order.status = request.args["status"]
    order.type = request.args["type"]
    order.descript = request.args["descript"]
    order.serial = request.args["serial"]
    order.price = request.args["price"]
    order.updated = datetime.datetime.now()
    db.session.commit()
    return str(order)


@app.route("/delete_ord")
def delete_ord():
    order = Orders.query.filter_by(id=request.args['id']).first()
    db.session.delete(order)
    db.session.commit()
    return f"Заявка №{request.args['id']} удалена"


@app.route('/search_ord', methods=["GET"])
def search_ord():
    return Orders.query.filter_by(id=request.args['id']).first()


@app.route('/search', methods=["GET"])
def search():
    for x in request.args.items():
        dict_do = {
            'Заявки': Orders.query.filter_by(id=x[1]).first(),
            'Сотрудники': Employees.query.filter_by(id=x[1]).first(),
            'Департаменты': Departments.query.filter_by(id=x[1]).first()
            }
        res = dict_do[x[0]]

    if not res:
        return "Нет такого id"
    return str(res)


@app.route('/all_orders')
def all_orders():
    data = Orders.query.limit(10).all()
    return str(data)


@app.route('/all_employees')
def all_employees():
    data = Employees.query.limit(10).all()
    return str(data)


@app.route('/all_departments')
def all_departments():
    data = Departments.query.limit(10).all()
    return str(data)


app.run()
