import pytest

from leetpass.strengthen import Strengthen

strengthen = Strengthen()


@pytest.mark.parametrize('password', ['pass'])
def test_strengthen_fail(password):
    with pytest.raises(TimeoutError) as e:
        strengthen.strengthen(password)

    assert 'Cannot substitute' in str(e)


@pytest.mark.parametrize('password', ['averylongpassword'])
def test_strengthen_pass(password):
    print(strengthen.strengthen(password))
