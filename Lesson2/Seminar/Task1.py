# Факториал числа

n = int(input("Введите число "))
fact = 1
sum = 1
while sum < n+1:
    fact *= sum
    sum+=1
print(fact)