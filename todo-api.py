from flask import Flask
import sqlite3

app = Flask(__name__)


def connect_db():
    return sqlite3.connect('todos.db')


@app.route("/db")
def text_from_db():
    db = connect_db()
    result = db.execute('select demotext from demotable')

    return result.fetchall()[-1]

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()