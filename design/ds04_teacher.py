class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

# BEGIN
    def __init__(self, **options):
        self.options = Truncater.OPTIONS | options
        # также можно использовать оператор распаковки **
        # self.options = {**Truncater.OPTIONS, **options}

    def truncate(self, text, **options):
        current_options = self.options | options
        # или через **
        # current_options = {**self.options, **options}
        if len(text) <= current_options['length']:
            return text
        substr = text[:current_options['length']]
        return f"{substr}{current_options['separator']}"
# END