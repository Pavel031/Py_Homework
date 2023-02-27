# Выбрать самый легкий и самый тяжелый арбуз.
# Пользователь вводит одно число N - количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число- это масса соответствующего арбуза.

N = int(input("enter q sugarwater: "))
n_min=1000
n_max=0
for i in range(N):
    massa=int(input("масса арбуза: "))
    if massa<n_min:
        n_min=massa
    if massa>n_max:
        n_max=massa
print(n_min,n_max)
