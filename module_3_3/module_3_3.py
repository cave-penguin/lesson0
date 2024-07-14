def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [[1, 2], False, "Hello"]
values_dict = {"a": 32, "b": False, "c": 54.87}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["45,123", [1, 2, 3]]
print_params(*values_list_2, 42)
