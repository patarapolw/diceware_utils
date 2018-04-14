# Leetpass

A leetspeak-based password strengthener, while attempting minimalistic change.

## Installation

```
pip install leetpass
```

## Usage

```
>>> from leetpass.strengthen import Strengthen
>>> strengthen = Strengthen()
>>> strengthen.strengthen("averylongpassword")
'avErylongpassword'
>>> strengthen.strengthen("averylongpassword")
'&v3rylongpa5sWord'
```

## Found In

https://mnemopass.herokuapp.com (https://github.com/patarapolw/mnemopass)
