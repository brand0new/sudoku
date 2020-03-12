import time

class Sudoku:
    def __init__(self, sudoku):
        self.rows = self.createRows(sudoku)
        self.columns = self.createColumns(self.rows)
        self.emptyPlace = [0,0]

    def createRows(self, sudoku):
        row = 0
        rows = {row: []}

        for c in sudoku:
            rows[row].append(c)

            if len(rows[row]) % 9 == 0:
                row += 1
                rows[row] = []

        return rows

    def createColumns(self, rows):
        column = 0
        columns = {column: []}

        for i in range(9):
            for j in range(9):
                columns[column].append(rows[j][i])
            column += 1
            columns[column] = []

        return columns

    def solveSudoku(self):
        # goal: not finding an empty space
        if not self.findNextEmptySpace():
            return True

        # assign coordinates to row and column
        row = self.emptyPlace[0]
        column = self.emptyPlace[1]

        # for all needed numbers
        for i in range(1,10):

            # if the number is not in the same row, column or square, place it
            if (str(i) not in self.rows[row]) and (str(i) not in self.columns[column]) and (str(i) not in self.validateSquare(row, column)):

                # assign possible solving value to position
                self.rows[row][column] = str(i)
                self.columns[column][row] = str(i)

                # check if entered result solves the puzzle
                if(self.solveSudoku(row, column)):
                    return True

                # if not solved undo set value
                self.rows[row][column] = '0'
                self.columns[column][row] = '0'

        # trigger backtracking
        return False

    def findNextEmptySpace(self):
        for i in range(9):
            for j in range(9):
                if self.rows[i][j] == '0':
                    # if there is an empty space set coordinates
                    self.emptyPlace[0] = i
                    self.emptyPlace[1] = j
                    return True
        return False

    def validateSquare(self, row, column):
        square = []
        for i in self.rows:
            # a square is always 3x3. To make sure all numbers are compared within the right square a floor division
            # is done. this will enable a determination of the right rows and columns (0,1,2 // 3 == 0, etc.)
            if int(row) // 3 == i // 3:
                for j in self.columns:
                    if int(column) // 3 == j // 3:
                        # while iterating through all the right numbers
                        square.append(self.rows[i][j])
        return square

    def printSudoku(self):
        # modulo 3 is used to print dividers at the appropriate places
        # the end parameter in print is used to paste different prints together
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
start = time.time()
Sudoku.solveSudoku()
end = time.time()

print('Solving took: ' + str(end - start) + ' seconds')
print('Solved! Here is the result')
Sudoku.printSudoku()

print('Thanks for using my Sudoku solver!')
input()