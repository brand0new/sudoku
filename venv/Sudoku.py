class Sudoku:
    def __init__(self, sudoku):
        self.x = 0
        self.y = 0
        self.rows = self.createRows(sudoku)

    def createRows(self, sudoku):
        rows = {}
        rows['r' + str(self.x)] = []
        pos = 0
        for c in sudoku:
            if pos < 8:
                rows['r' + str(self.x)].append(c)
                pos += 1
            else:
                rows['r' + str(self.x)].append(c)
                self.x += 1
                rows['r' + str(self.x)] = []
                pos = 0
        print(rows)
        return rows

    def validInRow(self, n, r):
        if n in r:
            return true
        else:
            return false

    def validInCol(self):
        for n in range(1,10):
            if n in self.rows['r' + str(self.x)][self.y]):
                return false
            else:
                return true

    def validInSq(self):
            return true

    def solveSudoku(self):
        for c in self.rows:
            if c == '0':
                for n in range(1,10):
                    if self.validInCol(n):
                        if self.validInRow(n):
                            c == n
                        else:
                            continue
                    else:
                        continue
            else:
                continue





easy = '501607900009003250827090000902051370300980000005706000406075032010000705003000196'
Sudoku = Sudoku(easy)

row = 0
col = 2

print(Sudoku.rows['r'+str(row)][col])
