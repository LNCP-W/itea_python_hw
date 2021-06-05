""" Преобразовать все самописные классы-модели из прошлых ДЗ (из задачи 1: Заявки - Orders, Департаменты
- Departments,
Сотрудники - Employees) в модели для использования в MongoDB. Предусмотреть необходимые связи, валидацию
данных и ограничения.
Написать функции, которые будут:
создавать/изменять/удалять новую заявку/сотрудника/департамент
Подсказка: у вас должно получиться 3 модели и 9 функций =)"""

import mongoengine as me
from datetime import datetime
from time import sleep
import json


me.connect("hw_9")


class Departments(me.Document):
    dep_name = me.StringField(required=True, min_length=3, unique=True)
    location = me.StringField()

    def __str__(self):
        return f"Department {self.dep_name} located in {self.location}"

    def __repr__(self):
        return f"{self.dep_name} in {self.location}"


class Employees(me.Document):
    fio = me.StringField(required=True, min_length=3, unique=True)
    position = me.StringField(required=True)
    department_id = me.ReferenceField(Departments, reverse_delete_rule=me.CASCADE)

    def __str__(self):
        return f"Employee {self.fio} worked on position {self.position} " \
               f"in department #{self.department_id}"

    def __repr__(self):
        return f"{self.fio} {self.position} in {self.department_id}"

class Orders(me.Document):
    type  = me.StringField(required=True, min_length=3)
    status  = me.StringField(required=True, min_length=3)
    serial = me.IntField(required=True)
    time_create = me.DateTimeField()
    description =me.StringField()
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
        return super().update(updated = datetime.now(), *args, **kwargs)


dep1 = Departments(dep_name="piu-pasau-A")
res = dep1.save()
print(res.id)
print(dep1)
sleep(3)
dep1.update(location='bla-bla-bla')
sleep(3)
print(dep1)


emp1 = Employees(fio="piu-aspiu-pu", position="slave", department_id=dep1)
res = emp1.save()
print(emp1)
sleep(3)
emp1.update(position="free")
print(res.id)
print(emp1)

order1 = Orders(type='gardant', status='new', serial=654353, description='Some broken phone', creator=emp1)
res = order1.save()
print(order1)
sleep(3)
order1.update(status='well done')
print(res.id)
print(order1)

sleep(10)
dep1.delete()

