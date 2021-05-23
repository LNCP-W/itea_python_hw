create table employees (
employee_id SERIAL primary key,
fio text not null,
position text not null,
department_id integer not null,
foreign key (department_id) references departments (department_id)
);

create table departments (
department_id serial primary key,
department_name text not null
);

create table orders (
order_id serial PRIMARY key,
created_dt text not null,
updated_dt text,
ordrt_type text not null,
description text not null,
status text not null,
serial_no integer not null,
creator_id integer not null,
foreign key (creator_id) references employees (employee_id)
);

insert into departments (department_name) values ('central Office');
insert into departments (department_name) values ('Lviv Office');

insert into employees values (1, 'Ivanov Ivan', 'Big Boss', 1);
insert into employees (fio, position, department_id) values ('Petrenko Petro', 'Middle Boss', 1);
insert into employees (fio, position, department_id) values ('Semenov Semen', 'Little Boss', 2);
insert into employees (fio, position, department_id) values ('Arturov Artur', 'Manager', 2);

insert into orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	values ('11.05.2021', 'paid', 'not started', 'new', '2588624',4);

insert into orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	values ('12.05.2021', 'guaranty', 'bad battry', 'new', '33556688',4);

insert into orders (created_dt, ordrt_type, description, status, serial_no, creator_id)
	values ('08.05.2021', 'paid', 'broken screen', 'new', '123456888',4);

select * from orders;

select fio, position from employees;

select * from orders order by created_dt;

select * from orders where ordrt_type = 'guaranty';
