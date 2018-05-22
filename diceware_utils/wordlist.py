import lzma
try:
    from secrets import choice
except ImportError:
    from random import choice

from diceware_utils.dir import wordlist_path

__doctest_skip__ = ['Wordlist.get_random_word']


class Wordlist:
    def __init__(self, word_list=None):
        if word_list is None:
            word_list = 'eff-long'
        with lzma.open(wordlist_path('{}.txt.xz'.format(word_list))) as f:
            self.wordlist = f.read().decode().strip().split('\n')

    def __len__(self):
        return len(self.wordlist)

    def get_random_word(self):
        """

        :return:
        >>> Wordlist().get_random_word()
        'ladybug'
        """
        return choice(self.wordlist)


if __name__ == '__main__':
    for word_list in ('aspell-en', 'bip0039','cracklib-small', 'diceware',
                      'eff-long', 'eff-short', 'eff-short2', 'skey'):
        wl = Wordlist(word_list=word_list)
        print(len(wl))
        for i in range(10):
            print(wl.get_random_word())
        print()

