# travel_log = {
#     "Bangladesh": ["Dhaka", "Cumilla", "Myminsingh"],
#     "USA": ["Los Angelos", "california", "New York"]
# }
# for key in travel_log:
#     # print(key, ": ", travel_log[key])
#     for cities in travel_log[key]:
#         print(cities)
# print()
# travel_log2 = {
#     "Bangladesh": {"Dhaka": 15, "Cumilla": 10, "Myminsingh": 5},
#     "USA": {"Los Angelos": 15, "california": 25, "New York": 20}
# }
# for key in travel_log2:
#     # print(key, ": ", travel_log[key])
#     for cities in travel_log2[key]:
#         print(cities, ": ", travel_log2[key][cities])

# country = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }
# for key in country:
#     for cities in country[key]["cities_visited"]:
#         print(cities)
country2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]
for i in country2:
    # print(i)
    for jj in i["cities_visited"]:
        print(jj)

