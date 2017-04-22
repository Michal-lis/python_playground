from flask import Flask, request, g
import json

app = Flask(__name__)


@app.route("/persons/<int:id>")
def person(id):
    return json.dumps(g.persons[id])


@app.route("/persons")
def persons():
    return json.dumps(g.persons)

if __name__ == "__main__":
    with app.app_context():

        g.persons = [
            {
                'id': 0,
                'name': 'Janek',
                'age': 21
            },
            {
                'id': 1,
                'name': 'Klaudia',
                'age': 22
            }
        ]
        app.run()


# {
#     'id': 1,
#     'name': 'Michał',
#     'age': 21
# }
