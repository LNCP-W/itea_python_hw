import json

import mongoengine as me
from datetime import datetime
from flask import Flask, request

me.connect("hw_9")
my_app = Flask('CRM_orders')


class Departments(me.Document):
    dep_name = me.StringField(required=True, min_length=3, max_length=99, unique=True)
    location = me.StringField(min_length=2, max_length=99)

    def __str__(self):
        return f"Department {self.dep_name} located in {self.location}"

    def __repr__(self):
        return f"{self.dep_name} in {self.location}"

    def write_to_json(self):
        json_data = self.to_json()
        self_id = self.save().id
        with open(f"{self_id}.json", "w") as f:
            f.write(json_data)


@my_app.route('/new_department/<string:name>,<string:loc>', methods=["POST"])
def new_dep(name, loc=None):
    res = Departments(dep_name=name, location=loc).save()
    return f"{str(res.id)} created"


@my_app.route('/edit_department/<upd_id>,<loc>', methods=["POST"])
def edit_dep(upd_id, loc):
    Departments.objects(id=upd_id).update(location=loc)
    return f"{upd_id} edited"


@my_app.route('/delete_department/<upd_id>', methods=["DELETE"])
def del_dep(upd_id):
    Departments.objects(id=upd_id).delete()
    return f"{upd_id} deleted"


@my_app.route('/search_department/<upd_id>', methods=["GET"])
def search_department(upd_id):
    return f'{Departments.objects(id=upd_id)} finded'


class Employees(me.Document):
    fio = me.StringField(required=True, min_length=3, unique=True)
    position = me.StringField(required=True)
    department_id = me.ReferenceField(Departments, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"Employee {self.fio} worked on position {self.position} " \
               f"in department #{self.department_id}"

    def __repr__(self):
        return f"{self.fio} {self.position} in {self.department_id}"

    def write_to_json(self):
        json_data = self.to_json()
        self_id = self.save().id
        with open(f"{self_id}.json", "w") as f:
            f.write(json_data)


@my_app.route('/new_employee/<name>,<pos>,<dep>', methods=["POST"])
def new_epm(name, pos, dep):
    res = Employees(fio=name, position=pos, department_id=dep).save()
    return f"{str(res.id)} created"


@my_app.route('/edit_employee/<upd_id>,<pos>', methods=["POST"])
def edit_emp(upd_id, pos):
    Employees.objects(id=upd_id).update(position=pos)
    return f'{upd_id} edited'


@my_app.route('/delete_employee/<upd_id>', methods=["DELETE"])
def del_emp(upd_id):
    Employees.objects(id=upd_id).delete()
    return f'{upd_id} deleted'


@my_app.route('/search_employee/<upd_id>', methods=["GET"])
def search_employee(upd_id):
    return f'{Employees.objects(id=upd_id)} finded'


class Orders(me.Document):
    order_type = me.StringField(required=True, min_length=3)
    order_status = me.StringField(required=True, min_length=3)
    serial = me.IntField(required=True)
    time_create = me.DateTimeField()
    description = me.StringField()
    order_creator = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)
    updated = me.DateTimeField()

    def __str__(self):
        return f"Order was created {self.time_create} by employee #{str(self.order_creator)}. " \
               f"Actual status is {self.order_status}, type: {self.order_type}, description: {self.description}, " \
               f"serial number: {self.serial}, last update: {self.updated}."

    def __repr__(self):
        return f"date:{self.time_create} employee :{str(self.order_creator)}, " \
               f"status:{self.order_status}, type: {self.order_type}, description: {self.description}, " \
               f"serial number: {self.serial}, updated: {self.updated}."

    def save(self, *args, **kwargs):
        self.time_create = datetime.now()
        return super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.updated = datetime.now()
        return super().update(*args, **kwargs)

    def write_to_json(self):
        json_data = self.to_json()
        self_id = self.save().id
        with open(f"{self_id}.json", "w") as f:
            f.write(json_data)


@my_app.route('/new_order', methods=["POST"])
def new_order():
    ord1 = json.loads(request.data).save()
    return f"{str(ord1.id)} created"


@my_app.route('/edit_order', methods=["POST"])
def edit_order():
    input_data = json.loads(request.data)
    upd_id = input_data.pop('order_id')
    Orders.objects(id=upd_id).update(**input_data, updated=datetime.now())
    return f'{upd_id} edited'

@my_app.route('/delete_order/<upd_id>', methods=["DELETE"])
def del_order(upd_id):
    Orders.objects(id=upd_id).delete()
    return f'{upd_id} deleted'


@my_app.route('/search_order/<upd_id>', methods=["GET"])
def search_order(upd_id):
    return f'{Orders.objects(id=upd_id)} finded'


my_app.run()
