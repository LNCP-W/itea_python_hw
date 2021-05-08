import uuid
import datetime
class Request:


    def __init__(self, name, serial, status):
        self.status = status
        self.name = name
        self.serial = serial
        self.__id = uuid.uuid4().hex
        self.time_create = datetime.datetime.today()



    def in_active(self):
        if self.status == "not_active":
            return "This request not active"
        x = datetime.datetime.today().date()-self.time_create.date()
        x = str(x).split()[0]
        if x == "0:00:00":
            return f"Request is active 0 days"
        return f"Request is active {x} days"

    def change_status(self, new_status):
        self.status = new_status
        return f"New status is: {self.status}"

    def req_id(self):
        return f"Request id is: {self.__id}"



r2=Request("ivan", 556586, "new")

print(r2.in_active())
print (r2.change_status("not_active"))
print(r2.in_active())
print(r2.req_id())
