# Завдання 3
# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle.

import json
import pickle


class Stadion:
    def __init__(self, name, city,capacity ):
        self.name = name
        self.city = city
        self.capacity = capacity
        self.employment = 0

    def free_places(self):
        return self.capacity - self.employment

    def зайняти_місця(self, number_seats):
        if self.free_places() >= number_seats:
            self.employment += number_seats
            print(f"Місця на стадіоні {self.name} успішно зайнято.")
        else:
            print("На жаль, недостатньо вільних місць на стадіоні.")

    def free_seats(self, number_seats):
        if self.employment >= number_seats:
            self.employment -= number_seats
            print(f"Місця на стадіоні {self.name} успішно звільнено.")
        else:
            print("На стадіоні немає настільки зайнятих місць.")

    def save_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.__dict__, file)

    def download_json(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.__dict__.update(data)

    def save_pickle(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)

    def download_pickle(self, filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            self.__dict__.update(data)

    def __str__(self):
        return f"Стадіон '{self.name}' у місті {self.city}. Вмістимість: {self.capacity}, Зайнятість: {self.employment}"


if __name__ == "__main__":
    stadion = Stadion("Олімпійський", "Київ", 70000)
    print("Початковий стан стадіону:")
    print(stadion)

    # Зберігаємо у JSON
    stadion.save_json("stadion.json")
    print("\nСтадіон збережено у JSON файлі.")

    # Зберігаємо у pickle
    stadion.save_pickle("stadion.pickle")
    print("\nСтадіон збережено у pickle файлі.")

    # Завантажуємо з JSON
    stadion.download_json("stadion.json")
    print("\nСтадіон завантажено з JSON файлу:")
    print(stadion)

    # Завантажуємо з pickle
    stadion.download_pickle("stadion.pickle")
    print("\nСтадіон завантажено з pickle файлу:")
    print(stadion)
