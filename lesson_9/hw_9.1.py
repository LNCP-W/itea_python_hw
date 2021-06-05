import mongoengine as me
from datetime import datetime

me.connect("hw_9")


class Departments(me.Document):
    dep_name = me.StringField(required=True, min_length=3, unique=True)
    location = me.StringField()

    def __str__(self):
        return f"Department {self.dep_name} located in {self.location}"

    def __repr__(self):
        return f"{self.dep_name} in {self.location}"

    def write_to_json(self):
        json_data = self.to_json()
        self_id = self.save().id
        with open(f"{self_id}.json", "w") as f:
            f.write(json_data)


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


class Orders(me.Document):
    type = me.StringField(required=True, min_length=3)
    status = me.StringField(required=True, min_length=3)
    serial = me.IntField(required=True)
    time_create = me.DateTimeField()
    description = me.StringField()
    creator = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)
    updated = me.DateTimeField()

    def __str__(self):
        return f"Order was created {self.time_create} by employee #{str(self.creator)}. " \
               f"Actual status is {self.status}, type: {self.type}, description: {self.description}, " \
               f"serial number: {self.serial}, last update: {self.updated}."

    def __repr__(self):
        return f"date:{self.time_create} employee :{str(self.creator)}, " \
               f"status:{self.status}, type: {self.type}, description: {self.description}, " \
               f"serial number: {self.serial}, updated: {self.updated}."

    def save(self, *args, **kwargs):
        self.time_create = datetime.now()
        return super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        return super().update(updated=datetime.now(), *args, **kwargs)

    def write_to_json(self):
        json_data = self.to_json()
        self_id = self.save().id
        with open(f"{self_id}.json", "w") as f:
            f.write(json_data)


dep1 = Departments(dep_name="Central Office")
res = dep1.save()
print(res.id)
dep1.write_to_json()
print(dep1)
dep1.update(location='Odessa')
print(dep1)
emp1 = Employees(fio="Ivanon Ivan", position="slave", department_id=dep1)
emp1.write_to_json()
emp1.save()
print(emp1)
emp1.update(position="free")
order1 = Orders(type='gardant', status='new', serial=654353, description='Some broken phone', creator=emp1)
order1.save()

order1.write_to_json()

print(order1)
order1.update(status='well done')
# dep1.delete()
