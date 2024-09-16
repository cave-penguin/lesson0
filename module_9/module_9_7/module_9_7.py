def is_prime(func):
    def wrapper(*args):
        func_result = func(*args)
        if func_result % 2 == 0:
            print("Составное")
        else:
            print("Простое")
        return func_result

    return wrapper


@is_prime
def sum_three(*args):
    summ = 0
    for num in args:
        summ += num
    return summ


result = sum_three(2, 3, 6)
print(result)
result1 = sum_three(4, 3, 2, 9)
print(result1)
