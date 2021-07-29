cities = ["mumbai","new york","parish"]
countries = ["india", "usa", "france"]
# z = zip(cities, countries)

# for zip in z:
#     print(zip)

d = {city:country for city, country in zip(cities, countries)}
print("dic comprehension",d)    