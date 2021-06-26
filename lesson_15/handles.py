@app.route('/search', methods=["GET"])
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


@app.route('/all_orders')
def all_orders():
    data = Orders.objects.limit(10)
    page_title = "Заявки"
    return render_template('orders.html', title=page_title, results=data)


@app.route('/all_employees')
def all_employees():
    data = Employees.objects.limit(10)
    page_title = 'Сотрудники'
    return render_template('employees.html', title=page_title, results=data)


@app.route('/all_departments')
def all_departments():
    data = Departments.objects.limit(10)
    page_title = 'Департаменты'
    return render_template('departments.html', title=page_title, results=data)


@app.route("/index")
def index():
    page_title = 'Главная страница'
    return render_template('index.html', title=page_title)