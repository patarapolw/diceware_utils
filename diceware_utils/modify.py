import yaml
import string
try:
    from secrets import choice, randbelow as randrange
except ImportError:
    from random import choice, randrange

from diceware_utils.dir import database_path


class Modify:
    def __init__(self):
        with open(database_path('leetspeak.yaml')) as f:
            self.leetspeak = yaml.safe_load(f)['min']

    def leetify_one(self, word_list):
        word_index = randrange(len(word_list))
        char_index = randrange(len(word_list[word_index]))
        char_to_substitute = word_list[word_index][char_index]
        char_substituted = choice(self.leetspeak.get(char_to_substitute.lower(), [char_to_substitute]))
        new_word_list = []
        for word in word_list:
            if word != word_list[word_index]:
                new_word_list.append(word)
            else:
                new_word_list.append(word[:char_index] + char_substituted + word[char_index+1:])

        return new_word_list

    @staticmethod
    def insert_symbol_one(word_list):
        index_to_insert = randrange(len(word_list))
        if word_list[index_to_insert].isalpha():
            if index_to_insert < 1 or word_list[index_to_insert - 1].isalpha():
                word_list.insert(index_to_insert, choice(string.punctuation))

        return word_list

    @staticmethod
    def insert_number_one(word_list, limit=100):
        index_to_insert = randrange(len(word_list))
        if word_list[index_to_insert].isalpha():
            if index_to_insert < 1 or word_list[index_to_insert - 1].isalpha():
                word_list.insert(index_to_insert, str(randrange(limit)))

        return word_list

    @staticmethod
    def switch_case_one(word_list):
        word_index = randrange(len(word_list))
        char_index = randrange(len(word_list[word_index]))
        char_to_substitute = word_list[word_index][char_index]
        char_substituted = char_to_substitute.upper() if char_to_substitute.islower() else char_to_substitute.lower()
        new_word_list = []
        for word in word_list:
            if word != word_list[word_index]:
                new_word_list.append(word)
            else:
                new_word_list.append(word[:char_index] + char_substituted + word[char_index + 1:])

        return new_word_list

    @staticmethod
    def switch_case_all(word_list):
        new_word_list = []
        for word in word_list:
            char_index = randrange(len(word))
            char_to_substitute = word[char_index]
            char_substituted = char_to_substitute.upper() if char_to_substitute.islower() else char_to_substitute.lower()
            new_word_list.append(word[:char_index] + char_substituted + word[char_index + 1:])

        return new_word_list

    @staticmethod
    def title_case_all(word_list):
        return [word.title() for word in word_list]

    @staticmethod
    def shorten_one(word_list, max_length=3):
        word_index = randrange(len(word_list))
        if word_list[word_index].isalpha():
            length = 1 + randrange(max_length - 1)
            new_word = word_list[word_index][:length]

            return [word if i != word_index else new_word for i, word in enumerate(word_list)]
        else:
            return word_list
