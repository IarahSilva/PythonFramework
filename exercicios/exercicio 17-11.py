class Calculadora():
    def somar(self, num1:int, num2:int):
        self.num1 = num1
        self.num2 = num2
        return num1 + num2

calc = Calculadora()
result = calc.somar(10, 10)
print(result)

    