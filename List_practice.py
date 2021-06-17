cities_list = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "LA", "Denver", "New Orleans"]
print(cities_list)

foods_list = ["apple", "banana", "cheese", "beef", "fish", "oyster", "onion", "ketchup", "lamb", "ham"]
print(foods_list)

print(cities_list[0:3])
print(cities_list[4:7])

cities_list[0] = "San Francisco"
cities_list[2] = "Brooklyn"
cities_list[7] = "Hollywood"
cities_list[5] = "Tampa"
print(cities_list)

cities_list.append("Oakland")
cities_list.extend(["LA", "New York City"])
cities_list.insert(0, "Maimi")
print(cities_list)

cities_list.pop(3)
del cities_list("Oakland")
cities_list.remove("Denver")
print(cities_list)