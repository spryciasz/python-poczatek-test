# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych
# długości przyprostokątnych.
#
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
#
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
#
# sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
# # pow(x, y) - podnosi x do potęgi y

import math

def bok_c(bok_a, bok_b):
    return math.sqrt(math.pow(bok_a, 2)+ math.pow(bok_b,2))

bok_a = float(input("Jaka jest długość boku a? "))
bok_b = float(input("Jaka jest długość boku b? "))

calculated_c = bok_c(bok_a, bok_b)
print(f"Przeciwprostokątna wynosi {calculated_c:.2f}")
