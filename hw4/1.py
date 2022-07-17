last_cities = input("Enter cities where you have been: ")
future_cities = input("Enter cities where you want to see: ")

last_cities_set = set()
for city in last_cities.split(" "):
    last_cities_set.add(city.capitalize())

future_cities_set = set()
for city in future_cities.split(" "):
    future_cities_set.add(city.capitalize())

favorite_cities_set = last_cities_set.intersection(future_cities_set)
if favorite_cities_set:
    favorite_cities = " ".join(favorite_cities_set)
    print(f"Your favorite cities are {favorite_cities}")
else:
    print("You are open for something new")
