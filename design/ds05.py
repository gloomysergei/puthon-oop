from urllib.parse import urlparse, parse_qs


# BEGIN (write your solution here)
class Url:
    def __init__(self, url: str)-> None:
        self.parsed = urlparse(url) # возвращает объект ParseResult
        
    def get_scheme(self):
        return self.parsed.scheme
    
    def get_hostname(self):
        return self.parsed.hostname
    
    def get_query_params(self) -> dict[str, list[str]]:
        return parse_qs(self.parsed.query)
    
    def get_query_param(self, key, default = None):
        params = parse_qs(self.parsed.query)
        values = params.get(key)
        if not values:
            return default
        else:
            return values[0]
        
    def __eq__(self, other):
        if not isinstance(other, Url):
            return NotImplemented
        return self.parsed == other.parsed
# END


