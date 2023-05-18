class Duck:
    def quack(self):
        return "Quack!"

    def swim(self):
        return "using muscles"

    def color(self):
        return "brown"


class Goose(Duck):
    def color(self):
        return "white"


class ElectricToy:
    def has_batteries(self):
        return True

    def quack(self):
        return "Quack!"

    def swim(self):
        return "using electricity"

    def color(self):
        return "brown"