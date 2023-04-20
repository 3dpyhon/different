import random


"""
- создаётся поле и заполняется экземлярами клеток
- первый игрок выбирает за кого играть
- игроки по очереди выбирают клетки, куда поставить Х или О
- проверка победителя, или когда на поле не остаётся ни одной свободной клетки - ничья 
"""


class Cell:
    """
    У клетки есть номер :int, значение :str и состояние :bool
    """
    def __init__(self, number, value=None, empty=True):
        self.number = number
        self.value = value
        self.empty = empty

    def __str__(self):
        return f'Клетка {self.number} {self.empty}'

    def __repr__(self):
        if self.value:
            return str(self.value)
        else:
            return str(self.number)

    def set_cell(self, player_side):
        """
        Sets player side and removes empty flag
        """
        if player_side:
            self.value = player_side
            self.empty = False


class Board:
    """
    У поля есть 9 клеток
    2 игрока
    проверка поля, комбинации (1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)
    """
    cells = [Cell(number) for number in range(1, 10)]
    win = ((1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7))

    def __str__(self):
        return f'{self.cells[:3]}\n{self.cells[3:6]}\n{self.cells[6:9]}'

    def __repr__(self):
        return 'This is TTT board'

    def winner_check(self, player_side):
        for i_line in self.win:
            flag = True
            for i_num in i_line:
                if self.cells[i_num - 1].value != player_side:
                    flag = False
                    break
            if flag:
                print(f'\nИгрок {player_side} побеждает!\n')
                return flag

    def board_full(self):
        for i_cell in self.cells:
            if i_cell.empty:
                return False
                break
        else:
            print('\nНичья!\n')
            return True


class Player:
    """
    Игрок выбирает сторону и клетку на которую ходить
    """
    sides = ['X', 'O']

    def __init__(self, name='', side=None):
        self.name = name
        self.side = side

    def __str__(self):
        return 'Player {}'.format(self.name)

    def __repr__(self):
        return self.name

    def choose_side(self):
        # Юзер выбирает сторону и она удаляется из списка сторон sides
        self.side = self.sides.pop(int(input('За кого играем?\nX - 1\nO - 2\n')) - 1)

    def move(self, side):
        # TODO: Добавить try, чтобы дать возможность сделать повторный ход
        moveTo = int(input(f'Игрок {side} ходит: ')) - 1

        # TODO: привязать к экземпляру Board и продумать наследование!!!!!!!!!!!!!!!!!!!!!!!!!

        if Board.cells[moveTo].empty:
            Board.cells[moveTo].set_cell(self.side)
        else:
            print(f'{Board.cells[moveTo]} занята, попробуй ещё раз!')


class Game:
    """
    Алгоритм игры за 2х игроков
    """
    is_running = True
    winner = None

    # def process(self, board, player):
    #     print(board)
    #     player.move()
    #     if board.winner_check(player.side):
    #         print(board)
    #         break

    myBoard = Board()

    playerOne = Player('Biba')
    playerTwo = Player('Boba')

    playerOne.choose_side()
    if playerOne.side:
        playerTwo.side = Player.sides[0]

    while is_running:
        print(myBoard)
        playerOne.move(playerOne.side)
        if myBoard.winner_check(playerOne.side):
            print(myBoard)
            break

        if myBoard.board_full():
            print(myBoard)
            break

        print(myBoard)
        playerTwo.move(playerTwo.side)
        if myBoard.winner_check(playerTwo.side):
            print(myBoard)
            break
