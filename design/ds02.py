class PasswordValidator:
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }
    
    def __init__(self, **kwards):
        self.options = {
            key: value 
            for key, value in kwards.items()
            if key in PasswordValidator.OPTIONS
        }
        for key, default in PasswordValidator.OPTIONS.items():
            self.options.setdefault(key, default)
    # BEGIN (write your solution here)
    def validate(self, password):
        errors = {}
        
        # Проверка минимальной длины — всегда нужна
        if len(password) < self.options['min_len']:
            errors['min_len'] = 'too small'
            
        # Проверку на цифры делаем только если она включена    
        if self.options.get('contain_numbers'):
            if not self._has_number(password):
                errors['contain_numbers'] = 'should contain at least one number'
                
        return errors
    # END
    def _has_number(self, password):
        return any(char.isdigit() for char in password)