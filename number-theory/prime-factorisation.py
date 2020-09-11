class PrimeFactorisation():
    def __init__(self, num: int):
        self.num = num
        self.__primeFactors = []

    def __factorise(self, num: int, f: int = 2) -> None:

        if num <= 0:
            raise ValueError("num must be greater than 0.")

        if num == 1:
            self.__primeFactors.append(num)
            return
        elif num == f:
            self.__primeFactors.append(num)
            return
        elif num % f == 0:
            self.__primeFactors.append(f)
            self.__factorise(num // f)
        else:
            self.__factorise(num, f + 1)

    def __compute(self):
        self.__primeFactors = []
        self.__factorise(self.num)

    def get(self) -> list:
        self.__compute()
        return self.__primeFactors

    def print(self):
        """
        prints the prime factorisation
        """
        self.__compute()
        print(f"prime factors of {self.num}: {self.get()}")


PrimeFactorisation(75).print()
