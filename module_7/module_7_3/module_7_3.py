class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = [*file_names]

    def get_all_words(self):
        all_words = {}
        chars_to_remove = [",", ".", "=", "!", "?", ";", ":", " - "]
        for file in self.file_names:
            with open(file) as f:
                list_of_strings = f.read().lower().splitlines()
                filtered_words = []
                for string in list_of_strings:
                    filtered_string = string
                    for char in chars_to_remove:
                        filtered_string = filtered_string.replace(char, "")
                    filtered_words.extend(filtered_string.split())
                all_words[file] = filtered_words
        return all_words

    def find(self, word):
        for file in self.file_names:
            for key, value in self.get_all_words().items():
                if file == key:
                    for item in value:
                        if item.lower() == word.lower():
                            return {file: value.index(item) + 1}

    def count(self, word):
        count_word = {}
        for file in self.file_names:
            counter = 0
            for key, value in self.get_all_words().items():
                if file == key:
                    for item in value:

                        if item.lower() == word.lower():
                            counter += 1
            count_word[file] = counter
        return count_word


finder2 = WordsFinder("test_file.txt")
print(finder2.get_all_words())  # Все слова
print(finder2.find("TEXT"))  # 3 слово по счёту
print(finder2.count("teXT"))  # 4 слова teXT в тексте всего
