immutable_var = (23, "Hello", True, ["hi", 9])
print(f"Immutable tuple: {immutable_var}")
# immutable_var[1] = (
#     "Hi"  # 'tuple' object does not support item assignment Кортеж неизменяемый
# )

mutable_list = [9, False, "Trees"]
mutable_list[0] = 34
mutable_list[1] = True
mutable_list[2] = "Bushes"
print(f"Mutable list: {mutable_list}")

