class Board:
    def __init__(self):
        self.cells = [[0 for i in range(15)] for i in range(15)]
        self.cells_attack = [[True for i in range(15)] for i in range(15)]
        self.turn = 1
    def read_cell(self, row, col):
        return self.cells[row][col]
    def read_cells_attack(self, row, col):
        return self.cells_attack
    def write_cell(self, row, col, val):
        self.cells[row][col] = val
        self.turn *= -1
        if val == 0:
            self.cells_attack[row][col] = True
        else:
            self.cells_attack[row][col] = False


def number_chains(gameboard, player):
    joins = [0, 0, 0, 0, 0, 0]

    #row
    for row in range(15):
        col = 0
        while col < 11:
            counter = 0
            for x in range(5):
                
                if gameboard.read_cell(row, col + 4 - x) == player*(-1):
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row, col + 4 - x) == player:
                        counter += 1              
            col += 1
            joins[counter] += 1

    #col
    for col in range(15):
        row = 0
        while row < 11:
            counter = 0
            for x in range(5):
                
                if gameboard.read_cell(row + 4 - x, col) == player*(-1):
                    row += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col) == player:
                        counter += 1              
            row += 1
            joins[counter] += 1

    #diagonal1 ->, v
    for col1 in range(11):
        col = 0 + col1
        row = 0
        while col < 11:
            counter = 0
            for x in range(5):
                        
                if gameboard.read_cell(row + 4 - x, col + 4 - x) == -player:
                    row += 4 - x
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col + 4 - x) == player:
                        counter += 1
            row += 1
            col += 1              
            joins[counter] += 1

    for row1 in range(11):
        row = 0 + row1
        col = 0
        while row < 11:
            counter = 0
            for x in range(5):
                if gameboard.read_cell(row + 4 - x, col + 4 - x) == -player:
                    row += 4 - x
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + 4 - x, col + 4 - x) == player:
                        counter += 1
            row += 1
            col += 1              
            joins[counter] += 1
    #diag2 -> ^
    for col1 in range(0, 11):
        col = 0 + col1
        row = 14
        while col < 11:
            counter = 0
            for x in range(5):
                        
                if gameboard.read_cell(row + x - 4, col + 4 - x) == -player:
                    row += x - 4
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + x - 4, col + 4 - x) == player:
                        counter += 1
            row -= 1
            col += 1              
            joins[counter] += 1

    for row1 in range(4, 15):
        row = 0 + row1
        col = 0
        while row > 3:
            counter = 0
            for x in range(5):
                if gameboard.read_cell(row + x - 4, col + 4 - x) == -player:
                    row += x - 4
                    col += 4 - x
                    counter = 0
                    break
                else:
                    if gameboard.read_cell(row + x - 4, col + 4 - x) == player:
                        counter += 1
            row -= 1
            col += 1              
            joins[counter] += 1

    return joins