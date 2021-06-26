from models import app, db, Departments, Employees, Clients, Orders
from flask import Flask, request, render_template

@app.route('/search', methods=["GET"])
def search():
    page_title = "Результат поиска"
    for x in request.args.items():  # /search?Сотрудники=60bfe821f98dbc8e792f900b
        dict_do = {
            'Заявки': Orders.query.filter_by(o_id=x[1]).first(),
            'Сотрудники': Employees.query.filter_by(e_id=x[1]).first(),
            'Департаменты': Departments.query.filter_by(d_id=x[1]).first()
            }
    return render_template('search_result.html', title=page_title, results=dict_do[x[0]])
    # except mongoengine.errors.ValidationError:
    #     return render_template('search_result.html', title=page_title, results='Нет такой заявки')


@app.route('/all_orders')
def all_orders():
    data = Orders.query.limit(10).all()
    page_title = "Заявки"
    return render_template('orders.html', title=page_title, results=data)


@app.route('/all_employees')
def all_employees():
    data = Employees.query.limit(10).all()
    page_title = 'Сотрудники'
    return render_template('employees.html', title=page_title, results=data)


@app.route('/all_departments')
def all_departments():
    data = Departments.query.limit(10).all()
    page_title = 'Департаменты'
    return render_template('departments.html', title=page_title, results=data)


@app.route("/index")
def index():
    page_title = 'Главная страница'
    return render_template('index.html', title=page_title)

app.run()
