from UMFT380.proekt380Kamilov import MinNumber

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

check = MinNumber(a, b, c)
print("Наименьшее число:", check.find_min())


from project380TursunovJavoxir import NumberType
from jasurxudayberdiyev import check_year
from rahmonberdievBehzod9zadacha import process_numbers

num = int(input("Введите число: "))
check = NumberType(num)
print(check.result())
print(check_year(300))



A=float(input("Введите A: "))
B=float(input("Введите B: "))
C=float(input("Введите C: "))

A, B, C = process_numbers(A,B,C)

print("A =", int(A))
print("B =", int(B))
print("C =", int(C))