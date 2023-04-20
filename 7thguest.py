class Cell:
    """

    __counter: int - counts occupied cells
    state: bool - true if cell is empty
    mutable: bool - true if state can be changed
    set_cell - method to change cell.mutable
    returns bool (?)
    deactivate_cells - method to deactivate state and mutable for cells in the same row, column and diagonal

    """

    __counter = 0

    def __init__(self, x, y, state=True, mutable=True):
        self.x = x
        self.y = y
        self.state = state
        self.mutable = mutable

    def __str__(self):
        if self.state and self.mutable:
            return "0"
        elif self.state and not self.mutable:
            return "X"
        elif not (self.state and self.mutable):
            return "-"

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def increment_counter(self):
        self.__counter += 1

    def get_counter(self):
        return self.__counter

    def set_cell(self):
        if self.mutable:
            self.increment_counter()
            self.mutable = False
            self.deactivate_cells()
            return True
        else:
            return False

    def deactivate_cells(self):
        # TODO: define logic of position of a cell on the board in order to deactivate appropriate cells
        for iIndex, iCell in enumerate(Board.cells):
            if iCell.mutable:
                if self.x == iCell.x or self.y == iCell.y:
                    iCell.state = False
                    iCell.mutable = False
        # left_margin = self.x - (8 - (self.x + 1))
        # right_margin = self.x + (8 - (self.x - 1))
        # for iNum in range(left_margin, right_margin+1):
        #     if iCell.mutable:
        #         if Board.cells[iNum].x == iNum:
        #             Board.cells[iNum].state = False
        #             Board.cells[iNum].mutable = False


class Board:
    cells = [Cell(i + 1, y + 1) for i in range(8) for y in range(8)]

    def __str__(self):
        for iInd, iCell in enumerate(self.cells):
            if iInd % 8 == 0:
                print()
            print(f"{iCell}", end="  ")
        return "\n\nHad to return something"


myBoard = Board()
print(myBoard)

myBoard.cells[27].set_cell()
print(myBoard)
print(myBoard.cells[27].x)

