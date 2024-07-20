data_structure = [
    [1, 2, 3],
    {"a": 4, "b": 5},
    (6, {"cube": 7, "drum": 8}),
    "Hello",
    ((), [{(2, "Urban", ("Urban2", 35))}]),
]


def calculate_structure_sum(args):
    summa = 0
    if isinstance(args, dict):
        for key, value in args.items():
            summa += len(key)
            if isinstance(value, int):
                summa += value
            elif isinstance(value, str):
                summa += len(value)
            elif (
                isinstance(value, list)
                or isinstance(value, tuple)
                or isinstance(value, dict)
                or isinstance(value, set)
            ):
                summa += calculate_structure_sum(value)
    else:
        for arg in args:
            if isinstance(arg, int):
                summa += arg
            elif isinstance(arg, str):
                summa += len(arg)
            else:
                summa += calculate_structure_sum(arg)
    return summa


result = calculate_structure_sum(*data_structure)
print(result)
