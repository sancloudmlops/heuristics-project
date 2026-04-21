import click
from heuristics.greedy_coin import greedy_coin
from heuristics.tsp import run_simulation
from heuristics.cities import cities


@click.group()
def cli():
    pass


@cli.command()
@click.argument("amount", type=int)
def coin(amount):
    """Return minimum coins"""
    result = greedy_coin(amount)
    click.echo(result)


@cli.command()
@click.option("--iterations", default=50)
def tsp(iterations):
    """Run TSP simulation"""
    city_list = list(cities.keys())
    route, dist = run_simulation(city_list, iterations)

    click.echo(f"Best Route: {route}")
    click.echo(f"Distance: {dist:.2f} km")


if __name__ == "__main__":
    cli()