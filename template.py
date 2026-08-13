data = [{'turkey': ['istambul', 'antalia']}, {'russia': ['samara', 'moscow']}]

merged = {}
for d in data:
    merged.update(d)
#print(merged)

sorted_country = sorted(merged.items())
result = {country: sorted(city) for country, city in sorted_country}
print(result)