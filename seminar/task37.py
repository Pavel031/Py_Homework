def reorder(number):
    if number == 0:
        return ""
    stringer = input()
    return reorder(number - 1) + stringer
nums = int(input("Кол-во элементов: "))
print(reorder(nums))