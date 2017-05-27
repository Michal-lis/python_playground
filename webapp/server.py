from flask import Flask, request, g, jsonify, abort, render_template
import records

app = Flask(__name__)  # __name zawiera main


@app.route("/persons/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def person(id):
    if request.method == 'GET':
        return jsonify(g.persons[id])  # jsonify serializuje Pythonowy slownik i zamienia go w stringa
    elif request.method == 'PUT':
        data = request.get_json()
        for field in ['name', 'age']:
            if data.get(field) is not None:  # get zwraca none jak nie istnieje
                g.persons[id][field] = data[field]
        return '', 204,
    else:  # dotyczy to DELETE
        del g.persons[id]
        return '', 204,


@app.route("/persons", methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        lista = []
        for each in sorted(g.persons):
            lista.append(g.persons[each])
        # lista2 = [g.persons[key] for key in sorted(g.persons)]
        return jsonify(lista)
    else:  # to dotyczy metody POST
        data = request.get_json()
        new_person = {'id': g.id_counter}
        for field in ['name', 'age']:
            if data.get(field) is not None:
                new_person[field] = data[field]
            else:
                abort(400)
        else:
            g.persons[g.id_counter] = new_person
            g.id_counter += 1
            return '', 204,


@app.route("/query")
def query():
    q = """
    SELECT name, seat, room, screenings.datetime, title
    FROM users, tickets, screenings, films
    WHERE users.id = 2 AND tickets.user_id = users.id AND tickets.screening_id = screenings.id
    AND screenings.film_id = films.id
    """
    return jsonify(g.db.query(q).as_dict())


@app.route('/<string:home>')
def static_page(home):
    return render_template('%s.html' % home)


@app.teardown_appcontext
def shutdown_session():
    g.db.close()


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

if __name__ == "__main__":
    # with app.app_context():
    #     g.db = records.Database('sqlite:///db.db')
    #     app.run()
    with app.app_context():
        g.persons = {
            0: {
                'id': 0,
                'name': 'Klaudia',
                'age': 22
            },
            1: {
                'id': 1,
                'name': 'Janek',
                'age': 21
            },
            2: {
                'id': 2,
                'name': 'Janek',
                'age': 21
            }
        }
        g.id_counter = 2
        app.run()
