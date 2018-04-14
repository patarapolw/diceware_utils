from random import randrange
from passwordstrength.passwordmeter import PasswordStrength
from time import time
try:
    from secrets import choice
except ImportError:
    from random import choice

from leetpass.leetify import Leetify


class Strengthen:
    def __init__(self):
        self.leetify = Leetify()

    def strengthen(self, password, target=70, timeout=5):
        start = time()
        while True:
            if time() - start > timeout:
                raise TimeoutError('Timeout: {}'.format(time() - start))

            if PasswordStrength(password).strength() > target:
                break

            password = choice([self.leetify.sub_one(password),
                               self.change_case_one(password, timeout)])

        return password

    @staticmethod
    def change_case_one(password, timeout=5):
        start = time()
        while True:
            if time() - start > timeout:
                raise TimeoutError('Cannot substitute')

            i = randrange(len(password))
            char = password[i]
            if char.isalpha():
                if char.isupper():
                    new_char = char.lower()
                else:
                    new_char = char.upper()
                return password[:i] + new_char + password[i+1:]


if __name__ == '__main__':
    print(Strengthen().strengthen('hellofromnewworld'))
