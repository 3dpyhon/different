"""

БЛЕК ДЖЕК

Карты имеют такие «ценовые» значения:

от двойки до десятки — от 2 до 10 соответственно;
у туза — 1 или 11 (11, пока общая сумма не больше 21, далее 1);
у «картинок» (король, дама, валет) — 10.
Напишите программу, которая вначале случайным образом выдаёт пользователю и компьютеру по две карты и затем запрашивает у пользователя действие: взять карту или остановиться. На экран должна выдаваться информация о руке пользователя. После того как игрок останавливается, выведите на экран победителя.

Представление карты реализуйте с помощью класса.

Дополнительно: сделайте так, чтобы карты не могли повторяться.

Ваши классы в этой задаче могут выглядеть так:

class Card:

    # Карта, у которой есть значения
    # — масть
    # — ранг/принадлежность: 2, 3, 4, 5, 6, 7 и так далее

class Deck:
    # Колода создаёт у себя объекты карт

class Player:
    # Игрок, у которого есть имя и какие-то карты на руках

"""

# TODO: Проверить берут ли экземпляры класса карты из одной колоды?
# TODO: Сделать AI и Player

import random


class Deck:
    ranks = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
        'Ace': 11
    }  # Попробовать написать условие для туза прямо в рангах

    # кажется .copy() тут не нужен, т.к. несколько игроков играют отдельными колодами.
    suites = {'Diamonds': ranks.copy(),
              'Clubs': ranks.copy(),
              'Hearts': ranks.copy(),
              'Spades': ranks.copy()
              }

    def __init__(self):
        """Логика такая: экземпляр наследует случайный ключ масти и ранга, чтобы потом удалять из колоды карты (ключи) и возвращать удалённые значения. Ага, лучше бы ключ возвращал."""

        self.suite = random.choice(list(self.suites.keys()))
        """
        Логика: 
        - по масти экземпляра ищет в ключах соответствующую копию словаря рангов: dict  
        - преобразуется в список ключей рангов: list
        - из списка мастей выбирается рандомное знчение: str
        - затем карта удаляется
    
        """
        self.rank = random.choice(list(self.suites[self.suite].keys()))
        self.remCard()

    def __str__(self):
        return ("Card \"{} {}\"".format(self.rank, self.suite))


class Card(Deck):

    def __init__(self):
        super().__init__()

    def __str__(self):
        return super().__str__()

    def __add__(self, other):
        """ Складывает номиналы карт"""

        if isinstance(self, Deck) and isinstance(other, Deck):
            return self.ranks[self.rank] + other.ranks[other.rank]

    def __radd__(self, other):
        """ Зеркально складывает номиналы карт"""

        return self.ranks[self.rank] + other

    # @classmethod
    def remCard(self):
        """Перегрузка функции pop: удаляет ранг заданной масти и возвращает None (или ранг или похер что возвращает)"""

        self.suites[self.suite].pop(self.rank)
        return None  # self.rank


class Player:

    def __init__(self, name: str):
        self.name = name
        self.deck = [Card() for i_card in range(2)]

    def __str__(self):
        return self.name

    def getCard(self):
        # тут возможно стоит написать замену значений туза.
        print('{} takes another card'.format(self.name))
        self.deck.append(Card())

    def playAI(self):
        if self.playerScore() <= 20:
            self.getCard()
        else:
            self.playerPass()

    def playerPass(self):
        print('{} passes'.format(self.name))
        pass

    def playerScore(self):

        "Метод считает номиналы карт у игрока"

        score = 0
        for i_card in self.deck:
            score += i_card
        return score


def getPlayerInfo(player, *args):
    "Функция выдаёт информацию о картах игрока и их общий номинал"

    print('*' * 30)
    print('\nPlayer {}\'s cards:'.format(player), ('\n{}' * len(player.deck)).format(*player.deck))
    print('Total points: {}\n'.format(player.playerScore()))
    print('*' * 30)


def theWinnerIs(playOne, playTwo):
    "Функция определяет победителя"

    if playTwo.playerScore() < playOne.playerScore() < 21:
        return playOne.name
    elif playOne.playerScore() < playTwo.playerScore() < 21:
        return playTwo.name
    elif playOne.playerScore() == playTwo.playerScore():
        print('Draw')
    elif playOne.playerScore() > 21 and playTwo.playerScore() > 21:
        print('Petty loosers')
    else:
        if playOne.playerScore() < playTwo.playerScore():
            return playOne.name
        else:
            return playTwo.name


playerOne = Player('BibaUser')
playerTwo = Player('BobaAI')

""" Логика игры USER vs AI """

while True:
    getPlayerInfo(playerOne, playerOne.deck)
    getPlayerInfo(playerTwo, playerTwo.deck)

    try:
        playerChoice = int(input('1 - Take another card\n2 - Pass\n3 - Stop\nYour choice: '))

        if playerChoice == 1:
            playerOne.getCard()
        elif playerChoice == 2:
            playerOne.playerPass()
        elif playerChoice == 3:
            print('And the winner is: {}'.format(theWinnerIs(playerOne, playerTwo)))
            break
    except:
        print('\nPlease enter 1 to take another card, 2 to pass or 3 to stop')

    playerTwo.playAI()

""" Логика игры для AI vs AI"""

# while True:
#   getPlayerInfo(playerOne, playerOne.deck)
#   getPlayerInfo(playerTwo, playerTwo.deck)

#   if playerOne.playerScore() < 22 or playerTwo.playerScore() < 22:
#     playerOne.playAI()
#     playerTwo.playAI()
#     if playerOne.playerPass() or playerTwo.playerPass():
#       theWinnerIs(playerOne, playerTwo)
#       break
#   else:
#     theWinnerIs(playerOne, playerTwo)
#     break1