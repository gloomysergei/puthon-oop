from ds06_collection import Collection


# BEGIN
def format(data):
    c = Collection(data)
    return c.map_(_normalise) \
        .unique() \
        .group_by(lambda row: (row['country'], row['name'])) \
        .map_(lambda row: {key: sorted(values) for key, values in row.items()}) \
        .sort_by(lambda row: list(row.keys())) \
        .all()


def _normalise(row):
    return {'name': row['name'].lower().strip(), 'country': row['country'].lower().strip()}