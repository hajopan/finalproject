import os
from config import db
from models import Person
from app import connex_app

# Data to initialize database with
PEOPLE = [
    {'fname': 'Rizky', 'lname': 'Akbar'},
    {'fname': 'Rinintha', 'lname': 'Anggie'},
    {'fname': 'Safran','lname': 'Wijaya'}
]

# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')

# Create the database
with connex_app.app.app_context():
    db.create_all()

    # Iterate over the PEOPLE structure and populate the database
    for person in PEOPLE:
        p = Person(lname=person['lname'], fname=person['fname'])
        db.session.add(p)

    db.session.commit()