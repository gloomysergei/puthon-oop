from ds06_collection import Collection


# BEGIN (write your solution here)
def format(city_list):
    instance = Collection(city_list)
    normalized = instance.map_(
        lambda row: {
            'name': row['name'].strip().lower(),
            'country': row['country'].strip().lower()
        }
    )
    unique = normalized.unique()
    sort_my = unique.sort_by(lambda x: (x['country'], x['name']))
    # sort_my.print()
    grouped = sort_my.reduce_(
        lambda acc, row: {
            **acc,
            row['country']: acc.get(row['country'], []) + [row['name']]
        },
        {}
    )
    # grouped.print() # [{'russia': ['moscow', 'samara'], 'turkey': ['antalia', 'istambul']}]
    result_dict= grouped.all()[0] # {'russia': ['samara', 'moscow'], 'turkey': ['antalia', 'istambul']}
    result = [{key: value} for key, value in  result_dict.items()]
    return result
# END

raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]

result = format(raw)
# expected = [{'russia': ['moscow', 'samara']},
            # {'turkey': ['antalia', 'istambul']}]
print(result)