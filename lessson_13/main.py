# import json
#
# import mongoengine as me
# from datetime import datetime
#
# import mongoengine.errors
# from flask import Flask, request, render_template
# from concurrent.futures import ThreadPoolExecutor
#
# me.connect("hw_9")
# my_app = Flask('CRM_orders')
#
#
# class Departments(me.Document):
#     dep_name = me.StringField(required=True, min_length=3, max_length=99, unique=True)
#     location = me.StringField(min_length=2, max_length=99)
#
#     def __str__(self):
#         return f"Department {self.dep_name} located in {self.location}"
#
#     def __repr__(self):
#         res = f"\"id\": \"{self.__getitem__('id')}\", \"name\": \"{self.dep_name}\", \"location\": \"{self.location}\""
#         return "{" + res + "}"
#
#     def write_to_json(self):
#         json_data = self.to_json()
#         self_id = self.save().id
#         with open(f"{self_id}.json", "w") as f:
#             f.write(json_data)
#
#
# @my_app.route('/new_department/<string:name>,<string:loc>', methods=["POST"])
# def new_dep(name, loc=None):
#     dep1 = Departments(dep_name=name, location=loc)
#     res = dep1.save()
#     return f"{str(res.id)} created"
#
#
# @my_app.route('/edit_department/<upd_id>,<loc>', methods=["POST"])
# def edit_dep(upd_id, loc):
#     Departments.objects(id=upd_id).update(location=loc)
#     return f"{upd_id} edited"
#
#
# @my_app.route('/delete_department/<upd_id>', methods=["DELETE"])
# def del_dep(upd_id):
#     Departments.objects(id=upd_id).delete()
#     return f"{upd_id} deleted"
#
#
# @my_app.route('/search_department/<upd_id>', methods=["GET"])
# def search_department(upd_id):
#     return f'{Departments.objects(id=upd_id)} finded'
#
#
# class Employees(me.Document):
#     fio = me.StringField(required=True, min_length=3, unique=True)
#     position = me.StringField(required=True)
#     department_id = me.ReferenceField(Departments, reverse_delete_rule=me.CASCADE)
#
#     def __str__(self):
#         return f"Employee {self.fio} worked on position {self.position} " \
#                f"in department {self.department_id}"
#
#     def __repr__(self):
#         res = f"\"id\": \"{self.__getitem__('id')}\", " \
#               f"\"name\": \"{self.fio}\", " \
#               f"\"position\": \"{self.position}\", " \
#               f"\"department\": \"{self.department_id}\""
#         return "{" + res + "}"
#
#     def write_to_json(self):
#         json_data = self.to_json()
#         self_id = self.save().id
#         with open(f"{self_id}.json", "w") as f:
#             f.write(json_data)
#
#
# @my_app.route('/new_employee/<name>,<pos>,<dep>', methods=["POST"])
# def new_epm(name, pos, dep):
#     emp1 = Employees(fio=name, position=pos, department_id=dep)
#     res = emp1.save()
#     return f"{str(res.id)} created"
#
#
# @my_app.route('/edit_employee/<upd_id>,<pos>', methods=["POST"])
# def edit_emp(upd_id, pos):
#     Employees.objects(id=upd_id).update(position=pos)
#     return f'{upd_id} edited'
#
#
# @my_app.route('/delete_employee/<upd_id>', methods=["DELETE"])
# def del_emp(upd_id):
#     Employees.objects(id=upd_id).delete()
#     return f'{upd_id} deleted'
#
#
# @my_app.route('/search_employee/<upd_id>', methods=["GET"])
# def search_employee(upd_id):
#     return f'{Employees.objects(id=upd_id)} finded'
#
#
# class Orders(me.Document):
#     order_type = me.StringField(required=True, min_length=3)
#     order_status = me.StringField(required=True, min_length=3)
#     serial = me.IntField(required=True)
#     time_create = me.DateTimeField()
#     description = me.StringField()
#     order_creator = me.ReferenceField(Employees, reverse_delete_rule=me.CASCADE)
#     updated = me.DateTimeField()
#
#     def __str__(self):
#         return f"Order was created {self.time_create} by employee #{str(self.order_creator)}. " \
#                f"Actual status is {self.order_status}, type: {self.order_type}, description: {self.description}, " \
#                f"serial number: {self.serial}, last update: {self.updated}."
#
#     def __repr__(self):
#         res = f"\"id\": \"{self.__getitem__('id')}\", " \
#               f"\"date\": \"{str(self.time_create.strftime('%d.%m.%Y %H:%M'))}\", " \
#               f"\"employee\": [\"{self.order_creator.id}\", \"{self.order_creator.fio}\"], " \
#               f"\"status\":\"{self.order_status}\", " \
#               f"\"type\": \"{self.order_type}\", " \
#               f"\"description\": \"{self.description}\", " \
#               f"\"serial number\": \"{self.serial}\", " \
#               f"\"updated\": \"{str(self.updated.strftime('%d.%m.%Y %H:%M'))}\""
#         return "{" + res + "}"
#
#     def save(self, *args, **kwargs):
#         self.time_create = datetime.now()
#         self.updated = datetime.now()
#         return super().save(*args, **kwargs)
#
#     def update(self, *args, **kwargs):
#         self.updated = datetime.now()
#         return super().update(*args, **kwargs)
#
#     def write_to_json(self):
#         json_data = self.to_json()
#         self_id = self.save().id
#         with open(f"{self_id}.json", "w") as f:
#             f.write(json_data)
#
#
# @my_app.route('/new_order', methods=["POST"])
# def new_order():
#     input_data = json.loads(request.data)
#     ord1 = Orders(**input_data).save()
#     return f"{str(ord1.id)} created"
#
#
# @my_app.route('/edit_order', methods=["POST"])
# def edit_order():
#     input_data = json.loads(request.data)
#     upd_id = input_data.pop('order_id')
#     Orders.objects(id=upd_id).update(**input_data, updated=datetime.now())
#     return f'{upd_id} edited'
#
#
# @my_app.route('/delete_order/<upd_id>', methods=["DELETE"])
# def del_order():
#     Orders.objects(id=upd_id).delete()
#     return f'{upd_id} deleted'
#
#
# @my_app.route('/search_orders', methods=["POST"])
# def search_orders():
#     input_data = json.loads(request.data)
#     data = []
#
#     def f(oid):
#         x = json.loads(str(Orders.objects(id=oid))[1:-1])
#         data.append(x)
#     with ThreadPoolExecutor(max_workers=len(input_data)) as pool:
#         for i in input_data:
#             pool.submit(f, i)
#     return json.dumps(data, sort_keys=True, indent=4)


@my_app.route('/search', methods=["GET"])
def search():
    page_title = "Результат поиска"
    try:
        for x in request.args.items():  # /search?Сотрудники=60bfe821f98dbc8e792f900b
            dict_do = {
                'Заявки': Orders.objects(id=x[1]),
                'Сотрудники': Employees.objects(id=x[1]),
                'Департаменты': Departments.objects(id=x[1])
                }
        return render_template('search_result.html', title=page_title, results=dict_do[x[0]])
    except mongoengine.errors.ValidationError:
        return render_template('search_result.html', title=page_title, results='Нет такой заявки')


@my_app.route('/all_orders')
def all_orders():
    data = Orders.objects.limit(10)
    data = json.loads(str(data))
    for i in range(10-len(data)):
        data.append({"id": "None", 'employee': ['None']})
    page_title = "Заявки"
    return render_template('orders.html', title=page_title, results=data)


@my_app.route('/all_employees')
def all_employees():
    data = Employees.objects.limit(10)
    data = json.loads(str(data))
    for i in range(10 - len(data)):
        data.append({'id': 'Пусто'})
    page_title = 'Сотрудники'
    return render_template('employees.html', title=page_title, results=data)


@my_app.route('/all_departments')
def all_departments():
    data = Departments.objects.limit(10)
    data = json.loads(str(data))
    for i in range(10-len(data)):
        data.append({'id': 'Пусто'})
    page_title = 'Департаменты'
    return render_template('departments.html', title=page_title, results=data)


@my_app.route("/index")
def index():
    page_title = 'Главная страница'
    return render_template('index.html', title=page_title)

my_app.run()
