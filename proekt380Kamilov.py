class MinNumber:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def find_min(self) -> int:
        minimum = self.a

        if self.b < minimum:
            minimum = self.b

        if self.c < minimum:
            minimum = self.c

        return minimum