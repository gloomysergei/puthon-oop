from solution import Url


URL1 = 'http://hexlet.io?key=value&key2=value2'
URL2 = 'https://google.com:80?a=b&c=d&lala=value'


def test_url1():
    url = Url(URL1)
    assert url.get_scheme() == 'http'
    assert url.get_hostname() == 'hexlet.io'
    assert url.get_query_params() == {
        'key': ['value'],
        'key2': ['value2'],
        }
    assert url.get_query_param('key') == 'value'
    assert url.get_query_param('key2', 'lala') == 'value2'
    assert url.get_query_param('new', 'ehu') == 'ehu'
    assert url == (Url(URL1))
    assert not url == (Url(URL2))


def test_url2():
    url = Url(URL2)
    assert url.get_scheme() == 'https'
    assert url.get_hostname() == 'google.com'
    assert url.get_query_params() == {
        'a': ['b'],
        'c': ['d'],
        'lala': ['value'],
        }
    assert url.get_query_param('key') is None
    assert url.get_query_param('key2', 'lala') == 'lala'
    assert url.get_query_param('new', 'ehu') == 'ehu'
    assert url == (Url(URL2))
    assert not url == (Url(URL1))
    assert not url == (Url('https://google.com'))
    assert not url == (Url(URL2.replace('80', '443')))