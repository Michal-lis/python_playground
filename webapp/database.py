import records

db = records.Database('sqlite:///db.db')


query = """
select name, seat, room, screenings.datetime, title
from users, tickets, screenings, films
where users.id = 2 and tickets.user_id = users.id and tickets.screening_id = screenings.id
and screenings.film_id = films.id
"""

rows = db.query(query)

for row in rows:
    print(row.as_dict())
