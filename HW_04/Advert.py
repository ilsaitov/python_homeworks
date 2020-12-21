import json


class ColorizeMixin:
    """
    Class that enables changing text
    color when displayed in console
    :param code: color code
    """

    def __init__(self, code):
        self.code = code
        print(f'\033[1;{self.code};40m')


class _Ad_Attribute:
    """
    Class that deals with advertisement attribute
    :param file: ad file
    """

    def __init__(self, file):
        self.file = file
        for key in self.file:
            if key == 'location':
                for k in self.file['location']:
                    self.__setattr__(k, self.file['location'][k])


class Advert(ColorizeMixin):

    """
    Objects of this class work with JSON files
    and can return attributes
    :param file: JSON file
    """

    repr_color_code = 33
    color = ColorizeMixin(repr_color_code)

    def __init__(self, file):
        self.file = file
        for key in self.file:
            if key == 'class':
                self.__setattr__('class_', self.file[key])
            elif key != 'price':
                self.__setattr__(key, self.file[key])
        self.location = _Ad_Attribute(file)

        self.price = 0
        if 'price' in self.file:
            if self.file['price'] < 0:
                print('ValueError: price should be greater than 0')
            else:
                self.price = self.file['price']

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == "__main__":
    iphone_json = """{
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, ул. Мориса Тереза, 50", "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""

    corgi_json = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
      }
    }"""

    iphone_load = json.loads(iphone_json)
    corgi_load = json.loads(corgi_json)
    # print(file)

    iphone = Advert(iphone_load)
    print(iphone.title)
    print(iphone.price)
    print(iphone)
    print(iphone.location.address)

    corgi = Advert(corgi_load)
    print(corgi.class_)
    print(corgi)
