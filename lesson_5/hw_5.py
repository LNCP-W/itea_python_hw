CREATE TABLE employees (
employee_id SERIAL PRIMARY KEY,
fio TEXT NOT NULL,
position TEXT NOT NULL,
department_id INTEGER NOT NULL,
FOREIGN KEY (department_id) REFERENCES departments (department_id)
);

CREATE TABLE departments (
department_id SERIAL PRIMARY KEY,
department_name TEXT NOT NULL
);

CREATE TABLE orders (
order_id SERIAL PRIMARY KEY,
created_dt TEXT NOT NULL,
updated_dt TEXT,
ordrt_type TEXT NOT NULL,
description TEXT NOT NULL,
status TEXT NOT NULL,
serial_no INTEGER NOT NULL,
creator_id INTEGER NOT NULL,
FOREIGN KEY (creator_id) REFERENCES employees (employee_id)
);

INSERT INTO departments (department_name) VALUES ('central Office');
INSERT INTO departments (department_name) VALUES ('Lviv Office');

INSERT INTO employees VALUES (1, 'Ivanov Ivan', 'Big Boss', 1);
INSERT INTO employees (fio, position, department_id) VALUES ('Petrenko Petro', 'Middle Boss', 1);
INSERT INTO employees (fio, position, department_id) VALUES ('Semenov Semen', 'Little Boss', 2);
INSERT INTO employees (fio, position, department_id) VALUES ('Arturov Artur', 'Manager', 2);

INSERT INTO orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	VALUES ('11.05.2021', 'paid', 'NOT started', 'new', '2588624',4);

INSERT INTO orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	VALUES ('12.05.2021', 'guaranty', 'bad battry', 'new', '33556688',4);

INSERT INTO orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	VALUES ('08.05.2021', 'paid', 'broken screen', 'new', '123456888',4);

SELECT * FROM orders;

SELECT fio, position FROM employees;

SELECT * FROM orders ORDER BY created_dt;

SELECT * FROM orders WHERE ordrt_type = 'guaranty';
