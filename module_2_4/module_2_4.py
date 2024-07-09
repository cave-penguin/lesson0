numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# First solution

# for i in numbers[1:]:
#     counter = 0
#     for j in numbers[1:]:
#         is_prime = True
#         if i % j == 0:
#             counter += 1
#     if counter == 1:
#         primes += [i]
#     else:
#         not_primes += [i]

# Second solution

for i in numbers[1:]:
    is_prime = True
    for j in numbers[1 : numbers.index(i)]:
        if i % j == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime:
        primes += [i]
    else:
        not_primes += [i]

print("Primes:", primes)
print("Not primes:", not_primes)
