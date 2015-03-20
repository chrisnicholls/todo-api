from flask import Flask, request, jsonify, send_from_directory
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

@app.route("/todo", methods=['POST'])
def create_todo():
    todo = request.get_json()

    db = connect_db()
    db.execute("insert into todos (title,completed) values (?,?)", (todo['title'], todo['completed']))

    db.commit()
    db.close()

    return ""

@app.route("/todos")
def get_all():
    db = connect_db()

    result = []

    cur = db.execute("select * from todos")
    for row in cur.fetchall():
        result.append({'id': row[0], 'title': row[1], 'completed': bool(row[2])})

    return jsonify(todos=result)

@app.route("/todos/active")
def get_active():
    return get_all()


@app.route('/todomvc/<path:path>')
def send_todomvc(path):
    print "path %s" % path
    return send_from_directory('/Users/cnicholls/Documents/YES/todomvc/examples/jquery-rest', path)

if __name__ == "__main__":
    app.run()