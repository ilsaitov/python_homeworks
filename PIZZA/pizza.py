from typing import Literal, Dict


Pizza_Size = Literal["L", "XL"]


class Basic_Pizza:

    recipe_base = {
        "🍅 tomato sauce": None,
        "🧀 mozarella": None,
    }

    def __init__(self, name: str, size: Pizza_Size, recipe: Dict[str, None]):
        self.__dict__.update(self.recipe_base)
        self.__dict__.update(recipe)

        self.name = "{name} {size}".format(name=name, size=size)
        self.size = size

    def dict(self) -> Dict:
        """
        Prints out pizza recipe as a Dict
        :return: Dict
        """
        recipe = self.__dict__.copy()
        recipe.pop("name")
        recipe.pop("size")
        return recipe

    def __eq__(self, other) -> bool:
        """
        Compares two pizzas
        :param other:
        :return: bool
        """
        return self.dict() == other.dict()

    def __str__(self) -> str:
        """
        Prints out recipe as a string
        :return: string of pizza recipe
        """
        return "{}".format(self.name)


class Pepperoni(Basic_Pizza):

    name = "Pepperoni🍕"
    recipe = {
        "🌭 pepperoni": None,
        "🌶 pepper": None,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


class Margherita(Basic_Pizza):

    name = "Margherita🧀"
    recipe = {
        "🧀 parmesan": None,
        "🍅 tomato": None,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


class Hawaii(Basic_Pizza):

    name = "Hawaii🍍"
    recipe = {
        "🍍 pineapple": None,
        "🐔 chicken": None,
    }

    def __init__(self, size):
        super().__init__(self.name, size, self.recipe)


if __name__ == '__main__':
    print("Чтобы узнать меню, "
          "наберите в терминале: "
          "python cli.py menu\n", end="")
