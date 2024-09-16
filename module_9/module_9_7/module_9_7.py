def is_prime(func):
    def wrapper(*args):
        func_result = func(*args)
        for i in range(2, int(func_result**0.5) + 1):
            if func_result % i == 0:
                print("Составное")
                return func_result
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
result1 = sum_three(5, 3, 2)
print(result1)
