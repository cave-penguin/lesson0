import random

first_stone = random.choice([i for i in range(3, 21)])

second_stone = []


def get_code(number):
    get_all_list = []
    for i in range(1, number):
        for j in range(1, number):
            if number / (i + j) == int(number / (i + j)) and i != j:
                get_all_list.append([i, j])
            else:
                continue
    sorted_list = [sorted(i) for i in get_all_list]
    for i in sorted_list:
        if i not in second_stone:
            second_stone.append(i)
    return int("".join([f"{i[0]}{i[1]}" for i in second_stone]))


print(f"{first_stone} - {get_code(first_stone)}")
