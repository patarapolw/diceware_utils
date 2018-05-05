# Diceware Utilities

[![Build Status](https://travis-ci.org/patarapolw/diceware_utils.svg?branch=master)](https://travis-ci.org/patarapolw/diceware_utils)
[![PyPI version shields.io](https://img.shields.io/pypi/v/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI license](https://img.shields.io/pypi/l/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI status](https://img.shields.io/pypi/status/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)

A collection of tools to make diceware passphrase conform with ["password policy"](https://en.wikipedia.org/wiki/Password_policy)

For a selection of words, please see [other packages inside PyPI](https://pypi.org/search/?q=diceware).

## Installation

```commandline
pip install diceware_utils
```

or

```commandline
pipenv install -e git+https://github.com/patarapolw/diceware_utils.git#egg=diceware_utils
```

## Usage

```pycon
>>> from diceware_utils.policy import Conformize
>>> conformize = Conformize()
>>> conformize.conformize(['unlikely', 'piezo', 'electric', 'grounds'])
';U$Piezo33lGrounds'
>>> conformize.update_policy(new_policy)
>>> from diceware_utils.wordlist import Wordlist
>>> Wordlist().get_random_word()
'ladybug'
```

## Adapting to the policy of your choice 

- Policy is now updateable. It is of format:

```yaml
both_upper_and_lower: true
digit_count: 2
punctuation_count: 2
length:
  min: 10
  max: 20
```

## Found in

- https://github.com/patarapolw/memorable-password
