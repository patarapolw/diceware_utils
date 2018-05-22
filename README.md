# Diceware Utilities

[![Build Status](https://travis-ci.org/patarapolw/diceware_utils.svg?branch=master)](https://travis-ci.org/patarapolw/diceware_utils)
[![PyPI version shields.io](https://img.shields.io/pypi/v/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI license](https://img.shields.io/pypi/l/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)
[![PyPI status](https://img.shields.io/pypi/status/diceware_utils.svg)](https://pypi.python.org/pypi/diceware_utils/)

A collection of tools to make diceware passphrase conform with ["password policy"](https://en.wikipedia.org/wiki/Password_policy)

## Update

- (2017.05.22) Allow "weak" password generation.

```pycon
>>> from diceware_utils.generate import GeneratePassword
>>> GeneratePassword().generate(weak=True)
'+"75ImposeRompSudoku'
```

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
>>> from diceware_utils.generate import GeneratePassword
>>> GeneratePassword().generate()
',Ab17HaRLanky-RoyalS'
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
## Database sources

`leetspeak.yaml`, `policy.yaml` and Conformization algorithm are original. Wordlists are taken from [pwgen-passphrase](https://github.com/xmikos/pwgen-passphrase), which belongs to the respective authors.

Main wordlist to generate the password is `eff-long.txt`, which is from Electronic Frontier Foundation.

Another interesting wordlist in this series is `aspell-en.txt` which is maintained by Kevin Atkinson. I exported these two files to the Android app below.

The idea of diceware password is from [https://xkcd.com/936/](https://xkcd.com/936/).

## Web demo

http://diceware-utils.herokuapp.com

<img src="https://i.imgur.com/yy7EoW1.png">

## Mobile application

Please see [Keepass DX - memorable password](https://github.com/patarapolw/KeePassDX-memorable-password) -- an Android password manager with this generator.

I might plan to create a dedicated app for this password generator (probably without manager), because of the relatively slow start-up time of the SentenceMaker.

## Related projects

- [randomsentence](https://github.com/patarapolw/randomsentence) - a random sentence maker based on a list of keywords.
