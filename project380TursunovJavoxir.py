class NumberType:
    def __init__(self, number: int):
        self.number = number

    def parity(self) -> str:
        if self.number % 2 == 0:
            return "четное"
        else:
            return "нечетное"

    def digits(self) -> str:
        if 1 <= self.number <= 9:
            return "однозначное число"
        elif 10 <= self.number <= 99:
            return "двузначное число"
        elif 100 <= self.number <= 999:
            return "трехзначное число"
        else:
            return "число вне диапазона"

    def result(self) -> str:
        return f"{self.parity()} {self.digits()}"