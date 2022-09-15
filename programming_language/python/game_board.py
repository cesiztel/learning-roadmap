class Cell:
    positions = []
    STATUS_VALUE = 0
    FLAGGED = 4

    def __init__(self, positions):
        self.positions = positions
    
    def isFlagged(self): # https://martinfowler.com/bliki/TellDontAsk.html Tell-Don't-Ask
        return self.positions[self.STATUS_VALUE] == self.FLAGGED


class Game:
    game_board = [Cell([0, 0, 0]), Cell([4, 0, 0])]

    def get_flagged_cells(self):
        flagged_cells = []
        for cell in self.game_board:
            if cell.isFlagged():
                flagged_cells.append(cell)
        return flagged_cells

game = Game()
print(game.get_flagged_cells())