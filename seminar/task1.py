#Дан список чисел. Определить сколько уникальных значений

counter = int(input("Сколько элементов списка?: "))
numbers = []
for i in range(counter):
    numbers.append(int(input("введите число ")))
print(numbers)
num_value = len(set(numbers))
print(num_value)
    