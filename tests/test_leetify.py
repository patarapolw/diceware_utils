import pytest

from leetpass.leetify import Leetify

leetify = Leetify()


@pytest.mark.parametrize('password', ['password'])
def test_sub_one(password):
    print(leetify.sub_one(password))


@pytest.mark.parametrize('password', ['password'])
def test_sub_full(password):
    print(leetify.sub_full(password))
