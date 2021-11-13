#Nesting

#capitals = {
#        "France": "Paris",
#        "Germany": "Berlin",
#        "Germany": "Berlin",
#        }
#travel_log = {
#        "France": ["Paris", "Lille", "Dijon"],
#        "Germany": ["Berlin", "Hamburg", "Stuttgart"]
#        }
#print(travel_log)
#
#travel_log = {
#        "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#        "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5,}
#        }
#
#print(travel_log)
def add_new_country(country, visits, cities):
#    print(f"{country}, {visits}, {cities}\n") 
#    travel_log.append({"country": country, "cities_visited": cities, "total_visits": visits})
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = cities
    new_country["visits"] = visits
    travel_log.append(new_country)

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12,
        },
    {
       "country": "Germany", 
       "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
       "total_visits": 5,
       },
    ]

#print(travel_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(f"{travel_log}\n" + 3 * "###")
print(travel_log[2]["country"])
        
print(travel_log[2]["cities_visited"][1])
travel_log[2]["cities_visited"].append("Kalin")
print(10*"###")

print(travel_log[2]["cities_visited"])
