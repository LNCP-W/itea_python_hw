from uuid import uuid4
from datetime import date


class Order:

    def __init__(self, name, serial, status):
        self.status = status
        self.name = name
        self.serial = serial
        self.__id = uuid4().hex
        self.time_create = date.today()

    def in_active(self):
        if self.status == "not_active":
            return "This Order not active"
        x = date.today() - self.time_create
        return f"Order is active {x.days} days."

    def change_status(self, new_status):
        self.status = new_status
        return f"New status is: {self.status}"

    def order_id(self):
        return f"Order id is: {self.__id}"


r2 = Order("ivan", 556586, "new")

print(r2.in_active())
print(r2.change_status("not_active"))
print(r2.in_active())
print(r2.order_id())
