class Sudoku:
    def __init__(self, sudoku):
        self.rows = self.createRows(sudoku)
        self.columns = self.createColumns(self.rows)

    def createRows(self, sudoku):
        row = 0
        rows = {}
        rows[row] = []

        for c in sudoku: #81 5 0 1
            rows[row].append(c)

            if len(rows[row]) % 9 == 0:
                row += 1
                rows[row] = []

        return rows

    def createColumns(self, rows):
        column = 0
        columns = {}
        columns[column] = []

        for i in range(9): #9
            for j in range(9): #9
                columns[column].append(rows[j][i])
            column += 1
            columns[column] = []

        return columns

    def solveSudoku(self, row, column):
        #base case
        if row == -1:
            return True
        while column < len(self.rows[row]):
            if self.rows[row][column] != '0':
                self.solveSudoku(row, column + 1)
            if self.rows[row][column] == '0':
                for number in self.possibleNumbers(row, column):
                    # if valid set the number
                    self.rows[row][column] = number
                    continue
                if len(self.possibleNumbers(row, column)) == 0:
                    self.rows[row][column] = 0
                    self.solveSudoku(row, column - 1)
        column = 0
        self.solveSudoku(row + 1, column)

        return False

    def validateSquare(self, number, row, column):
        square = []
        for i in self.rows:
            if int(row) // 3 == i // 3:
                for j in self.columns:
                    if int(column) // 3 == j // 3:
                        square.append(self.rows[i][j])

        if number not in square:
            return True

    def possibleNumbers(self, row, column):
        possibleNumbers = []
        for n in range(1,10):
            if n not in self.rows[row]:
                if n not in self.columns[column]:
                    if self.validateSquare(str(n), row, column):
                        possibleNumbers.append(str(n))

        print(possibleNumbers)
        return possibleNumbers

    def printSudoku(self):
        for row in range(9):
            if row % 3 == 0:
                print(13 * '- ')
            for column in range (9):
                if column % 3 == 0:
                    print('| ', end = "")
                print(self.rows[row][column] + " ", end = "")
            print("|")
        print(13 * '- ')
        return

# prefilled sudoku
prefills = {
    'easy'      : '501607900009003250827090000902051370300980000005706000406075032010000705003000196',
    'medium'    : '100000000008009100004300056910000005000100300425000609000000021306000500000080400',
    'hard'      : '650008109000000000090400008004006021000305000089000300000000000205860000001002090',
    'master'    : '800000000003600000070090200050007000000045700000100030001000068008500010090000400'
}

# initiating needed variables
sudoku = ''

# start of interaction
print('Welcome to my python Sudoku solver')
print('Solve own (o) sudoku or a prefilled one (p)?')
choice = input()

while choice not in ['o','p']:
    choice = input()
    print('Please enter a valid value')

if choice == 'o':
    print('Enter your Sudoku as a 81-character string')
    sudoku = input()

if choice == 'p':
    print('Select difficulty you want to solve: easy/medium/hard/master')
    difficulty = input()

    while difficulty not in ['easy', 'medium', 'hard', 'master']:
        difficulty = input()
        print('Please enter a valid value')

    sudoku = prefills.get(difficulty)

# create instance of sudoku class
Sudoku = Sudoku(sudoku)

print('This is your chosen Sudoku:')
Sudoku.printSudoku()

print('Press any key to solve')
input()
Sudoku.solveSudoku(0,0)

print('Solved! Here is the result')
Sudoku.printSudoku()

print('Thanks for using my Sudoku solver!')
input()