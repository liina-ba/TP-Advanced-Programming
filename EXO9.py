
city = input("Enter a city name : ")
cities = []
cityPopulation = []

while( city.lower() != "stop"):
    cities.append(city)
    cityPopulation.append(len(city) * 1_000_000)
    city = input("Enter a city name (or type 'stop' to finish): ")

sortedCities = sorted(cities , key=len , reverse=True)
sortedCityPopulation = sorted(cityPopulation , reverse=True)

print("\nCities and their populations:")
for city , population in zip(sortedCities , sortedCityPopulation):
    print(f"{city}: {population:,} citizens")




