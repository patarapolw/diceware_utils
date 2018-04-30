from diceware_utils.policy import Conformize


def test_conformize():
    print(Conformize().conformize(['unlikely', 'piezo', 'electric', 'grounds']))


if __name__ == '__main__':
    test_conformize()