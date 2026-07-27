from design.ds06 import format


raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]

expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']}]


def test_format():
    assert format(raw) == expected