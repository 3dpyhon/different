"""

Задача 7. Совместное проживание

Логика действий человека определяется следующим образом:

Генерируется число кубика от 1 до 6.
Если сытость < 20, то поесть.
Иначе, если еды в доме < 10, то сходить в магазин.
Иначе, если денег в доме < 50, то работать.
Иначе, если кубик равен 1, то работать.
Иначе, если кубик равен 2, то поесть.
Иначе играть.

переписать цикл, добавить счётчик дней.
"""
import random


class Human:
    hunger = 50

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return "{}, hunger: {}".format(self.name, self.hunger)

    def self_info(self):
        print("{}, hunger: {}".format(self.name, self.hunger))

    def eat(self, other):
        print('{} is eating...'.format(self.name))
        self.hunger += 10
        other.food -= 10

    def work(self, other):
        print("{} is working...".format(self.name))
        other.money += 10
        self.hunger -= 10

    def play(self):
        print("{} is playing...".format(self.name))
        self.hunger -= 10

    def shop(self, other):
        print("{} is shopping...".format(self.name))
        other.money -= 10
        other.food += 10

    def die(self):
        print('{} RIP'.format(self.name))
        raise BaseException("GAME OVER!")


class House:
    food = 50
    money = 0

    def house_info(self):
        print('\nFood left: {}\nMoney left: {}'.format(self.food, self.money))


def dice_info(dice):
    print('Number on the dice is {}'.format(dice))


def logic(person, house, dice):
    """ Функция определяет логику поведения персонажа """
    if person.hunger <= 0:
        person.die()
    elif person.hunger < 20:
        person.eat(house)
    elif house.food <= 10:
        person.shop(house)
    elif house.money < 50:
        person.work(house)
    elif dice == 1:
        dice_info(dice)
        person.work(house)
    elif dice == 2:
        dice_info(dice)
        person.eat(house)
    else:
        person.play()


house = House()
humanOne = Human('Biba', house)
humanTwo = Human('Boba', house)
humanThree = Human('Kuka', house)
print(humanOne)

house.house_info()

days = 1

while days < 366:
    print("*" * 20, "\nDay -", days, "\n", "*" * 20)
    humanOne.self_info()
    humanTwo.self_info()
    humanThree.self_info()
    house.house_info()
    print('*' * 20)
    dice_throw = random.randint(1, 6)
    logic(humanOne, house, dice_throw)
    logic(humanTwo, house, dice_throw)
    logic(humanThree, house, dice_throw)

    days += 1