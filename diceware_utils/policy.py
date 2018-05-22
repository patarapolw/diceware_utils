import yaml
from time import time
import string
try:
    from secrets import choice, randbelow as randrange
except ImportError:
    from random import choice, randrange

from diceware_utils.modify import Modify
from diceware_utils.dir import database_path

__doctest_skip__ = ['Conformize.conformize']


class Conformize:
    def __init__(self):
        self.policy = Policy()
        self.modify = Modify()

    def conformize(self, word_list, timeout=3, weak=False):
        """

        :param list word_list:
        :param float timeout:
        :param bool weak:
        :return str | None:
        >>> Conformize().conformize(['unlikely', 'piezo', 'electric', 'grounds'])
        ';U$Piezo33lGrounds'
        """
        word_list = self.modify.title_case_all(word_list)
        if not weak:
            word_list = self.modify.insert_number_one(word_list)
            word_list = self.modify.insert_symbol_one(word_list)
        else:
            index_to_insert = randrange(len(word_list))
            word_list.insert(index_to_insert, ''.join(
                [choice(string.punctuation) for _ in range(self.policy.policy['punctuation_count'])]))
            index_to_insert = randrange(len(word_list))
            word_list.insert(index_to_insert, ''.join(
                [choice(string.digits) for _ in range(self.policy.policy['digit_count'])]))

        while not self.policy.length(''.join(word_list)):
            word_list = self.modify.shorten_one(word_list)

        start = time()
        while time()-start < timeout:
            if not self.policy.length(''.join(word_list)):
                word_list = self.modify.shorten_one(word_list)
            elif not self.policy.is_conform(''.join(word_list)):
                word_list = choice([self.modify.insert_symbol_one(word_list),
                                    self.modify.switch_case_one(word_list),
                                    self.modify.leetify_one(word_list)])
            else:
                return ''.join(word_list)

        print('Non-conformed password:', ''.join(word_list))
        return None

    def update_policy(self, policy_dict):
        """

        :param dict | None policy_dict:
        :return:
        """
        self.policy = Policy(policy_dict=policy_dict)

    def get_policy(self):
        return self.policy.get_policy()


class Policy:
    def __init__(self, policy_dict=None):
        """

        :param dict | None policy_dict:
        """
        if policy_dict is not None:
            self.policy = policy_dict
        else:
            with open(database_path('policy.yaml')) as f:
                self.policy = yaml.safe_load(f)['policy']

    @staticmethod
    def both_upper_and_lower(password):
        """

        :param str password:
        :return bool:

        >>> Policy.both_upper_and_lower('aB')
        True
        >>> Policy.both_upper_and_lower('ab')
        False
        >>> Policy.both_upper_and_lower('AB')
        False
        """
        if any([char.islower() for char in password]) and any([char.isupper() for char in password]):
            return True

        return False

    @staticmethod
    def digit_count(password):
        """

        :param password:
        :return:
        >>> Policy.digit_count('12')
        2
        """
        return len([char for char in password if char.isdigit()])

    @staticmethod
    def punctuation_count(password):
        """

        :param password:
        :return:
        >>> Policy().punctuation_count('@')
        1
        """
        return len([char for char in password if char in string.punctuation])

    def length(self, password):
        if self.policy['length']['min'] <= len(password) <= self.policy['length']['max']:
            return True
        else:
            return False

    def is_conform(self, password):
        if self.policy['both_upper_and_lower']:
            if not self.both_upper_and_lower(password):
                return False

        if self.digit_count(password) < self.policy['digit_count']:
            return False

        if self.punctuation_count(password) < self.policy['punctuation_count']:
            return False

        if not self.length(password):
            return False

        return True

    def get_policy(self):
        return self.policy
