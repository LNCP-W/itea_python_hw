import mongoengine as me
from datetime import datetime

me.connect("hw_9")


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


def new_dep(name, loc=None):
    dep1 = Departments(dep_name=name, location=loc)
    res = dep1.save()
    return res.id


def edit_dep(upd_id, loc):
    Departments.objects(id=upd_id).update(location=loc)


def del_dep(upd_id):
    Departments.objects(id=upd_id).delete()


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


def new_epm(name, pos, dep):
    emp1 = Employees(fio=name, position=pos, department_id=dep)
    res = emp1.save()
    return res.id


def edit_emp(upd_id, pos, dep_id=None):
    if not dep_id:
        Employees.objects(id=upd_id).update(position=pos)
    else:
        Employees.objects(id=upd_id).update(position=pos, department_id=dep_id)


def del_emp(upd_id):
    Employees.objects(id=upd_id).delete()


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


def new_order(status, o_type, sn, desc, creator):
    ord1 = Orders(order_status=status, order_type=o_type, serial=sn, description=desc, order_creator=creator)
    res = ord1.save()
    return res.id


def edit_order(upd_id, status, o_type, desc):
    Orders.objects(id=upd_id).update(order_status=status, order_type=o_type, description=desc, updated=datetime.now())


def del_order(upd_id):
    Orders.objects(id=upd_id).delete()
