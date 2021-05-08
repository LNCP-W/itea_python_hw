class Car:

    def __init__(self, speed = 0, color = "no color", name = "noname", is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def __str__(self):
        return f"It is {self.color} car named {self.name}, with speed {self.speed}km/h."

    def go(self):
        return f"{self.color} car started up."

    def stop(self):
        return f"{self.color} car stoped."

    def turn(self, direction):
        return f"{self.color} car turn {direction}."

    def show_speed(self):
        return f"{self.color} car speed is {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{self.color} car was speedind. Call police."
        return f"Car speed is {self.speed}"

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{self.color} car was speedind. Call police."
        return f"Car speed is {self.speed}"

class PoliceCar(Car):
    pass

car_1 = TownCar(45, "Red", "Hort")
print(car_1.show_speed())
print(car_1.go())
print(car_1.turn("left"))
print(car_1.stop())
print(car_1)
car_2 = WorkCar(55, "Yellow", "Worker")
print(car_2.show_speed())