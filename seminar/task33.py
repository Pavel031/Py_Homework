import random

n = int(input('Введите количество оценок: '))
array = [random.randint(1, 5) for i in range(n)]
print(array)
num_min=min(array)
num_max=max(array)
num = [num_min if i == num_max else i for i in array]
print(num)