def custom_write(file_name, strings):
    positions = {}
    with open(file_name, "w", encoding="utf-8") as file:
        for index, string in enumerate(strings, 1):
            positions[(index, file.tell())] = string
            file.write(f"{string}\n")
    return dict(zip(positions, strings))


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
