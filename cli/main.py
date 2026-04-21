import click
from torch import dist
from heuristics.greedy_coin import greedy_coin
from heuristics.tsp import run_simulation
from heuristics.cities import cities
import json


@click.group()
def cli():
    pass


@cli.command()
@click.argument("amount", type=int)
def coin(amount):
    """Return minimum coins"""
    result = greedy_coin(amount)
    click.echo(json.dumps(result))


@cli.command()
@click.option("--iterations", default=50)
def tsp(iterations):
    """Run TSP simulation"""
    city_list = list(cities.keys())
    route, dist = run_simulation(city_list, iterations)

    output = {
    "route": route,
    "distance_km": round(dist, 2)
        }
    click.echo(json.dumps(output))


if __name__ == "__main__":
    cli()