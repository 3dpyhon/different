import random


class Warrior:

    def __init__(self, name, health=100, damage=20, is_alive=True):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = is_alive

    def stats(self):
        print('Warrior name: {}\nHealth - {}\nDamage - {}'.format(
            self.name, self.health, self.damage)
        )

    def attack(self, other):
        if self.is_alive or other.is_alive:
            other.health -= self.damage
            print("{a} deals {b} damage to {c},\n{c} has {d} hitpoints left".format(
                a=self.name, b=self.damage, c=other.name, d=other.health)
            )
        if other.health <= 0:
            other.death()
            other.is_alive = False

    def death(self):
        print("{} RIP".format(self.name))
        self.is_alive = False


warriorOne = Warrior("Biba")
warriorOne.damage = random.randint(5, 20)
warriorOne.stats()

warriorTwo = Warrior("Boba")
warriorTwo.damage = random.randint(5, 20)
warriorTwo.stats()

for i in range(6):
    random.choice([warriorOne.attack(warriorTwo), warriorTwo.attack(warriorOne)])
warriorOne.stats()
warriorTwo.stats()