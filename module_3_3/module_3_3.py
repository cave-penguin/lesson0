def print_params(a=1, b="строка", c=True):
    print(a, b, c)


print_params("One")
print_params(b=12)
print_params()
print_params(
    1,
    2,
    3,
)
print_params(c=False, a="Second")
list_ = ["third", 5.4]
print_params(c=37, *list_)
dict_ = {"c": "Fourth", "a": False}
print_params(**dict_, b=43)


print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [[1, 2], False, "Hello"]
values_dict = {"a": "Hi", "b": False, "c": 54.87}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [45.123, "String"]
print_params(*values_list_2, 42)

