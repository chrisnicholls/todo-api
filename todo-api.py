from flask import Flask, request, jsonify
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

@app.route("/todos")
def get_all():
    return jsonify("")

@app.route("/todos/active")
def get_active():
    return get_all()

@app.route("/todo", methods=['POST'])
def create_todo():
    print request.get_json()



if __name__ == "__main__":
    app.run()