#Program na vypočítání čísla Pi
import random
#Porměné
n = input("Zadej počet bodů: ")
num_point_circle = 0
num_point_total = 0
#Bug fix vstupu
while True:
    try:
        n = int(n)
        break
    except ValueError as err:
        print(err)
        continue
#Výpočet čísla Pi
for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    distance = x**2 + y**2
    if distance <= 1:
        num_point_circle += 1
    num_point_total += 1

print(4*num_point_circle/num_point_total)