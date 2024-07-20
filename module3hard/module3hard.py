data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, list) or isinstance(arg, set) or isinstance(arg, tuple):
            summa += calculate_structure_sum(*arg)
        if isinstance(arg, dict):
            for key, value in arg.items():
                summa += len(key)
                if isinstance(value, int):
                    summa += value
                elif isinstance(value, str):
                    summa += len(value)
                else:
                    summa += calculate_structure_sum(*value)
        if isinstance(arg, int):
            summa += arg
        if isinstance(arg, str):
            summa += len(arg)

    return summa


result = calculate_structure_sum(*data_structure)
print(result)
