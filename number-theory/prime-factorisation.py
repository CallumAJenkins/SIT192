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


if __name__ == "__main__":
    PrimeFactorisation(70).print()
    PrimeFactorisation(131).print()
    PrimeFactorisation(147).print()
    PrimeFactorisation(75).print()
    PrimeFactorisation(180).print()
    PrimeFactorisation(311).print()
    PrimeFactorisation(311).print()

    PrimeFactorisation(32).print()
    PrimeFactorisation(72).print()

    PrimeFactorisation(117).print()
    PrimeFactorisation(273).print()

    PrimeFactorisation(12).print()
    PrimeFactorisation(140).print()

    PrimeFactorisation(73).print()
    PrimeFactorisation(245).print()

    PrimeFactorisation(84).print()
    PrimeFactorisation(1254).print()

    PrimeFactorisation(120).print()
    PrimeFactorisation(18).print()
