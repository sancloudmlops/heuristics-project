from geopy.distance import geodesic

cities = {
    "New York": (40.7128, -74.0060),
    "Chicago": (41.8781, -87.6298),
    "Los Angeles": (34.0522, -118.2437),
    "Houston": (29.7604, -95.3698),
    "Miami": (25.7617, -80.1918),
}


def distance(city1, city2):
    return geodesic(cities[city1], cities[city2]).km