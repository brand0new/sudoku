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
                if row < 9:
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
                if self.solveSudoku():
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


def solve(s):
    result = Sudoku(s)

    start = time.time()
    result.solveSudoku()
    end = time.time()
    duration = end - start

    result_in_string = ""

    for value in result.rows.values():
        for item in value:
            result_in_string += item

    return result.rows, result_in_string, duration
