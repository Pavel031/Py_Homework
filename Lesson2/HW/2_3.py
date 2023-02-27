#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("enter max number: "))
s = 1
while s <= n:
    print(s, end=" ")
    s*=2