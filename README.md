Serving Python with Flask
The goal is to enable visitors to use the created Sudoku.py program and expose an API to which visitors can send their sudoku’s to be solved.

Flask
This micro framework is used to serve python web applications. Based on the Flask package it’s possible to create light weight webapps. Flask is created using the Werkzeug WSGI toolkit and Jinja template engine

Explicit application object created for three specific reasons:
Allows for multiple application instances (used for unit testing purposes)
Package naming is used to load needed resources for the application(s)
Application object is the Web Service Gateway Interface (WSGI) application

Problems
Can’t get structure right: api.py (importing Flask) seems to immediately start running sudoku.py when in the same directory. Moving sudoku.py to /application unables an import of the sudoku module. 
I had to take in account that Flask wants to host application directly meaning: any line of executable code WILL be run directly. The current Sudoku application was written to be controlled from the terminal. This caused a direct execution of the code that was written when approached through Flask. 
The solution was to change out a few lines and add a function that can be called through Flask to execute the solving of the puzzle.

Python
A functional programming language mainly created to be accessible all the while without limiting the user.

Problems
sudoku.py consists of one class (Sudoku) containing all methods. To create a RESTful API there needs to be a more separated approach.
