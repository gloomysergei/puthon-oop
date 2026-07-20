class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

# BEGIN (write your solution here)
    def __init__(self, **config):
        # Начинаем с дефолтных настроек
        self.config = self.OPTIONS.copy()
        # Обновляем переданными параметрами (например, length=3)
        self.config.update(config)
            
            
    def truncate(self, text, **options):
        current_config = self.config.copy()
        current_config.update(options)
        max_len = current_config['length']
        sep = current_config['separator']
        if len(text) <= max_len: # 'one two'
            return text
        return text[:max_len] + sep
# END