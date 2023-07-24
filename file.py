print("Hello World")


class Fio:
    def __init__(self):
        self.name = "Igor"
        self.surname = "Bezruk"

    def meet(self):
        return f"Hello, I'm {self.name} {self.surname}"


human = Fio()
print(human.meet())
