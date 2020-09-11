class GCD():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __euclideanAlgorithm(self, a: int, b: int) -> int:
        """
        recursively calls the euclidean algorithm until a remainder of 0 is found
        """
        r = a % b
        if r == 0:
            return b
        else:
            return self.__euclideanAlgorithm(b, r)

    def __validateInput(self) -> int:
        """
        provides value checking for the arguments passed to the euclidean algorithm
        """
        if self.a <= 0:
            raise ValueError("a must be greater than 0")
        elif self.b <= 0:
            raise ValueError("b must be greater than 0")

        if self.a < self.b:
            self.a, self.b = self.b, self.a
        return self.__euclideanAlgorithm(self.a, self.b)

    def get(self) -> int:
        """
        returns the gcd
        """
        return self.__validateInput()

    def print(self) -> int:
        """
        prints the formatted equation
        """
        print(f"GCD({self.a}, {self.b}) = {self.get()}")


GCD(201, 291).print()
GCD(75, 325).print()
