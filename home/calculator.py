"""14.12.2022 - калькулятор"""

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        print(self.a + self.b)

    def __sub__(self):
        print(self.a - self.b)

    def __mul__(self):
        print(self.a * self.b)

    def __truediv__(self):
        print(self.a / self.b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

calculator = Calculator(a, b)

print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
oper = int(input("Выберите операцию:"))
if oper == 1:
    print(calculator.__add__())
elif oper == 2:
    print(calculator.__sub__())
elif oper == 3:
    print(calculator.__mul__())
elif oper == 4:
    print(calculator.__truediv__())
else:
    print("Ошибка!")