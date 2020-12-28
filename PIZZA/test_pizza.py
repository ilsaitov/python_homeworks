import pytest
import random
from unittest.mock import patch
from click.testing import CliRunner
from pizza import Pepperoni, Hawaii, Margherita
from pizza_decorators import bake, delivery, pickup
from cli import menu, order


def test_dict():
    excepted = {
        '🍅 tomato sauce': None,
        '🧀 mozarella': None,
        '🌭 pepperoni': None,
        '🌶 pepper': None
    }

    assert Pepperoni(size="L").dict() == excepted


def test_order_pickup():
    runner = CliRunner()
    my_randint = 15
    with patch.object(random, "randint", return_value=my_randint):
        result = runner.invoke(order, ["hawaii", "xl"])
        assert result.exit_code == 0
        actual = result.output
        excepted = (
            "👨‍🍳 Приготовили Hawaii🍍 XL за 15 мин.!\n"
            "🚶 🏠 Самовывоз Hawaii🍍 XL за 15 мин.!\n"
        )
        assert actual == excepted


def test_str():
    excepted = (
        "Pepperoni🍕 XL"
    )
    assert str(Pepperoni(size="XL")) == excepted


def test_bake_no_decorator():
    original_bake = bake.__wrapped__
    assert original_bake(Hawaii(size="XL")) == "👨‍🍳 Приготовили"


def test_delivery_no_decorator():
    original_delivery = delivery.__wrapped__
    assert original_delivery(Margherita(size="XL")) == "🛵 🚚 Доставка"


def test_pickup_no_decorator():
    original_pickup = pickup.__wrapped__
    assert original_pickup(Pepperoni(size="XL")) == "🚶 🏠 Самовывоз"


def test_bake_L_decorated():
    my_randint = 17
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            bake(Pepperoni(size="L"))
            == "👨‍🍳 Приготовили Pepperoni🍕 L за 17 мин.!"
        )


def test_bake_XL_decorated():
    my_randint = 21
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            bake(Pepperoni(size="XL"))
            == "👨‍🍳 Приготовили Pepperoni🍕 XL за 21 мин.!"
        )


def test_delivery_decorated():
    my_randint = 19
    with patch.object(random, "randint", return_value=my_randint):
        assert (
            delivery(Margherita(size="L"))
            == "🛵 🚚 Доставка Margherita🧀 L за 19 мин.!"
        )


def test_pickup_decorated():
    my_randint = 22
    with patch.object(random, "randint", return_value=my_randint):
        assert pickup(Hawaii(size="XL")) == "🚶 🏠 Самовывоз Hawaii🍍 XL за 22 мин.!"


def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    actual = result.output
    assert (
        "Меню:" in actual
        and "-Pepperoni🍕 L" in actual
        and "-Margherita🧀 XL" in actual
    )


def test_order_delivery():
    runner = CliRunner()
    my_randint = 21
    with patch.object(random, "randint", return_value=my_randint):
        result = runner.invoke(order, ["pepperoni", "l", "--delivery"])
        assert result.exit_code == 0
        actual = result.output
        excepted = (
            "👨‍🍳 Приготовили Pepperoni🍕 L за 21 мин.!\n"
            "🛵 🚚 Доставка Pepperoni🍕 L за 21 мин.!\n"
        )
        assert actual == excepted
