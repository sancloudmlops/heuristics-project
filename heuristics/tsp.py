import random
from heuristics.cities import distance


def tsp_route(city_list):
    cities = city_list[:]
    random.shuffle(cities)

    route = [cities.pop(0)]

    while cities:
        last = route[-1]
        next_city = min(cities, key=lambda c: distance(last, c))
        route.append(next_city)
        cities.remove(next_city)

    return route


def total_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(route[i], route[i + 1])
    return dist


def run_simulation(city_list, iterations=50):
    best_route = None
    best_dist = float("inf")

    for _ in range(iterations):
        route = tsp_route(city_list)
        dist = total_distance(route)

        if dist < best_dist:
            best_dist = dist
            best_route = route

    return best_route, best_dist