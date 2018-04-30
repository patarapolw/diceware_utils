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
pipenv install -e git+https://github.com/patarapolw/diceware_utils.git
```

## Usage

```pycon
>>> from diceware_utils.policy import Conformize
>>> Conformize().conformize(['unlikely', 'piezo', 'electric', 'grounds'])
'unlikElypiEzo&lt;ElectriC73grOunds'
>>> from diceware_utils.wordlist import Wordlist
>>> Wordlist().get_random_word()
'ladybug'
```
