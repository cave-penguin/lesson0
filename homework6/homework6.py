my_dict = {"Name": "Micky", "Age": 42}
print("Dict:", my_dict)
print("Existing value:", my_dict["Age"])
print(my_dict.get("Country", "Not existing value"))
my_dict.update({"Planet": "Earth", "Post index": 123321})
name = my_dict.pop("Name")
print("Deleted value:", name)
print("Modified dictionary:", my_dict)

my_set = {1, 1, "roof", "wall", "wall", (1, 2), False, False}
print("Set:", my_set)
my_set.add(8)
my_set.remove("wall")
print("Modified set:", my_set)
