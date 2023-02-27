# Дано натуральное число А>1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n,что ф(n)=А. 
# Если А не является числом Фибоначчи, выведите число -1.

count = 2
fibonacci = int(input("enter number: "))

a = 0
b = 1

while fibonacci >= b:
    if fibonacci == b:
        print(count)
        break
    a , b = b , a + b
    count += 1
else:
    print(-1)