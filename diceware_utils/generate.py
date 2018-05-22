from diceware_utils.policy import Conformize
from diceware_utils.wordlist import Wordlist


class GeneratePassword:
    def __init__(self, word_list=None):
        self.conformize = Conformize()
        self.wordlist = Wordlist(word_list=word_list)

    def generate(self, number_of_words=None, conformize=True, weak=False):
        if weak and number_of_words is None:
            number_of_words = 3
        if number_of_words is None:
            number_of_words = 6

        keywords = [self.wordlist.get_random_word() for _ in range(number_of_words)]
        if not conformize:
            return keywords
        else:
            return self.conformize.conformize(keywords, weak=weak)


if __name__ == '__main__':
    gp = GeneratePassword()
    for _ in range(100):
        print(gp.generate(weak=True))
