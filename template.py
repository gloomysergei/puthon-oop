class PasswordValidator:
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
    }

    def __init__(self, **options):
        self.options = PasswordValidator.OPTIONS | options

options = {'contain_numbers': True}
validator = PasswordValidator(**options)
print(validator.options)