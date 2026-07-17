from design.ds03 import PasswordValidator


def test_validate_with_default_options():
    validator = PasswordValidator()
    errors1 = validator.validate('qwertyui')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {'min_len': 'too small'}

    errors3 = validator.validate('another-password')
    assert not errors3


def test_validate_with_options():
    options = {'contain_numbers': True}
    validator = PasswordValidator(**options)
    errors1 = validator.validate('qwertya3sdf')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {
        'min_len': 'too small',
        'contain_numbers': 'should contain at least one number'
        }
    errors3 = validator.validate('q23ty')
    assert errors3 == {'min_len': 'too small'}


def test_validate_with_incorrect_options():
    validator = PasswordValidator(contain_numberz=None)
    errors1 = validator.validate('qwertya3sdf')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {'min_len': 'too small'}