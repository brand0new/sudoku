from app import app
from flask import request


# the complete directory is seen as the flask webapp and so will create an object named app which can be used
# for routing. in this app it means both sudoku.py and api.py are now part of a webapp.

# ROUTES
# these routes are part of the WSGI. this means that using a webserver (like NGINX) to route incoming traffic
# these routes will then make sure the traffic is routed to the right

# this will serve the UI
@app.route("/")
def home():
    return "This is the sudoku webapp"


# api definitions
@app.route('/api/solve', methods=['POST'])
def api():

    if len(request.json['sudoku']) != 81:
        return 'You did not submit a 81 string containing numbers', 400
    else:
        return api.solveSudoku(request.json['sudoku'])


@app.errorhandler(500)
def oops():
    api.logger.error('Something went wrong...', request.path)
    return 500
