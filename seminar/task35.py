def is_simple(num):
    if num in [2 , 3]:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True
print(is_simple(int(input())))