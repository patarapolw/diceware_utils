from time import time
import os
import yaml
from random import randrange
try:
    from secrets import choice
except ImportError:
    from random import choice

from leetpass.dir import ROOT


class Leetify:
    def __init__(self):
        with open(os.path.join(ROOT, 'leetspeak.yaml')) as f:
            self.leet = yaml.load(f)

    def sub_one(self, password, profile='min', timeout=5):
        start = time()
        while True:
            if time() - start > timeout:
                raise TimeoutError('Cannot substitute')

            i = randrange(len(password))
            char = password[i]
            for k, v in self.leet[profile].items():
                if k == char:
                    new_char = choice(v)
                    return password[:i] + new_char + password[i+1:]

    def sub_full(self, password, profile='min'):
        new_password = ''
        for char in password:
            appended = False
            for k, v in self.leet[profile].items():
                if k == char:
                    v.append(char)
                    new_password += choice(v)
                    appended = True
                    break
            if not appended:
                new_password += char

        return new_password


if __name__ == '__main__':
    print(Leetify().sub_full('password'))
