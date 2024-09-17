# Задача "Потоковая запись в файлы"


from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for num in range(1, word_count + 1):
            file.write(f'Какое-то слово № {num}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_1 = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_1 = datetime.now()

print(end_1 - start_1)

start_2 = datetime.now()

first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(200, 'example7.txt'))
forth = Thread(target=write_words, args=(100, 'example8.txt'))


first.start()
second.start()
third.start()
forth.start()

first.join()
second.join()
third.join()
forth.join()

end_2 = datetime.now()

print(end_2 - start_2)
