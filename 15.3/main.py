# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
#
# Wczytaj od użytkownika informacje o:
#
# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
# a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
#
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import calculations.calc

value = int(input("Jaki kapitał chcesz wpłacić na początku? "))
percentage = float(input("Jakie masz oprocentowanie lokaty? "))
years = int(input("Ile lat chcesz posiadać lokate? "))

print(f"Po {years} latach, Twoja lokata będzie wynosić {calculations.calc.amount(value, percentage, years)}")
