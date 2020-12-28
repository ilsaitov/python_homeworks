import click
from pizza import Pizza_Size, Pepperoni, Margherita, Hawaii
import pizza_decorators
from pizza_decorators import bake, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.argument("pizza", nargs=1)
@click.argument("size", nargs=1)
@click.option("--delivery", default=False, is_flag=True)
def order(pizza: str, size: Pizza_Size, delivery: bool) -> None:
    """
    Cooks and delivers ordered pizza
    """
    pizza = pizza.lower().title()
    size = size.upper()
    pizza_class = globals()[pizza]
    print(bake(pizza_class(size=size)))
    if delivery:
        print(pizza_decorators.delivery(pizza_class(size=size)))
    else:
        print(pickup(pizza_class(size=size)))


@cli.command()
def menu() -> None:
    """
    Pizzeria menu
    """
    print("Меню:\n", end="")
    pizza_list = [
        Pepperoni(size="L"),
        Pepperoni(size="XL"),
        Margherita(size="L"),
        Margherita(size="XL"),
        Hawaii(size="L"),
        Hawaii(size="XL"),
    ]
    for element in pizza_list:
        print("-{pizza}".format(pizza=element))

    print("Чтобы заказать пиццу, "
          "наберите в терминале: python cli.py order "
          "название_пиццы размер_пиццы, "
          "и если вы хотите доставку, "
          "допишите --delivery :\n", end="")

if __name__ == "__main__":
    cli()
    
