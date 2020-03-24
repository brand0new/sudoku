from flask import Flask, request, json

from sudoku import solve

app = Flask(__name__)


@app.route('/solve', methods=['POST'])
def solveSudoku():
    sudoku = request.json['sudoku']

    if len(sudoku) != 81:
        return 'You did not submit a 81 string containing numbers', 400

    # call the solve function that returns a tuple
    solution = solve(sudoku)

    # assign tuple to resulting parameters
    solution_in_rows, solution_in_string, duration = solution

    # create response data
    data = {
        'in_string': solution_in_string,
        'in_rows': solution_in_rows,
        'time_to_solve_seconds': duration
    }

    # create json object to return
    response = json.dumps(data)

    return response


@app.errorhandler(500)
def oops(error):
    app.logger.error('Something went wrong...', (request.path))
    return 500


if __name__ == "__main__":
    app.run()