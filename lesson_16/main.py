import datetime
from models import app, db, Departments, Employees, Customers, Orders
from flask import request, render_template


@app.route("/create_dep")
def create_dep():
    if not request.args:
        page_title = 'Cоздание департамента'
        return render_template('create_dep.html', title=page_title)
    else:
        new_dep = Departments(**request.args)
        db.session.add(new_dep)
        db.session.commit()
        request.args = {"Департаменты": new_dep.id}
        return search()


@app.route("/create_customer")
def create_customer():
    if not request.args:
        page_title = 'Регистрация Клиента '
        return render_template('create_customer.html', title=page_title)
    else:
        new_cli = Customers(**request.args)
        db.session.add(new_cli)
        db.session.commit()
        request.args = {"Клиенты": new_cli.id}
        return search()


@app.route("/create_emp")
def create_emp():
    if len(request.args) < 2:
        page_title = 'Регистрация Сотрудника '
        return render_template('create_emp.html', title=page_title, id=request.args['id'])
    else:
        new_emp = Employees(**request.args)
        db.session.add(new_emp)
        db.session.commit()
        request.args = {"Сотрудники": new_emp.id}
        return search()


def create_ord_rabbit(a):
    date = {'created': datetime.datetime.now(), 'updated': datetime.datetime.now()}
    date.update(**a)
    new_ord = Orders(**date)
    db.session.add(new_ord)
    db.session.commit()
    return new_ord


@app.route("/create_ord")
def create_ord():
    if len(request.args) < 2:
        page_title = 'Регистрация Заявки'
        customers = Customers.query.all()
        return render_template(
                               'create_order.html',
                               title=page_title,
                               creator=request.args['creator'],
                               customers=customers)
    else:
        new_ord = create_ord_rabbit(request.args)
        request.args = {"Заявки": new_ord.id}
        return search()



if __name__ == "__main__":
    app.run()
