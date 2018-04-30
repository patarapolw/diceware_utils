# Diceware Utilities

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
```
