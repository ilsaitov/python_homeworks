import random
from typing import Callable
from functools import wraps
from pizza import Basic_Pizza


def log(str_for_print: str) -> Callable:
    """
    Parametric decorator
    """

    def simple_decorator(process: Callable) -> Callable:
        """
        Simple decorator
        """

        @wraps(process)
        def get_str_for_print(pizza: Basic_Pizza) -> str:
            """
            Returns the string obtained from log decorator
            """
            process_name = process(pizza)
            process_time = random.randint(10, 30)

            return str_for_print.format(process_name, pizza.name, process_time)

        return get_str_for_print

    return simple_decorator


@log("{} {} за {} мин.!")
def bake(pizza: Basic_Pizza) -> str:
    """Returns message that the pizza is ready"""
    return "👨‍🍳 Приготовили"


@log("{} {} за {} мин.!")
def delivery(pizza: Basic_Pizza) -> str:
    """Returns message that the pizza was delivered"""
    return "🛵 🚚 Доставка"


@log("{} {} за {} мин.!")
def pickup(pizza: Basic_Pizza) -> str:
    """Returns message that pizza was self-taken"""
    return "🚶 🏠 Самовывоз"
