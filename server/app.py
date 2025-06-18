# server/app.py
#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route("/earthquakes/<int:id>")
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake:
        return jsonify({
            'id': earthquake.id,
            'location': earthquake.location,
            'magnitude': earthquake.magnitude,
            'year': earthquake.year
        })
    else:
        return jsonify({'message': f'Earthquake {id} not found.'}), 404
    
@app.route("/earthquakes/magnitude/<float:magnitude>")
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()

     # Prepare the list of earthquake dictionaries
    quakes_data = []
    for quake in quakes:
        quakes_data.append({
            "id": quake.id,
            "location": quake.location,
            "magnitude": quake.magnitude,
            "year": quake.year
        })

    # Return the response with count and the list of quakes
    return jsonify({
        "count": len(quakes_data),
        "quakes": quakes_data
    }), 200 # Always return 200 OK for this endpoint, even if count is 0

# --- Existing User, Workout, and Exercise Endpoints ---


if __name__ == '__main__':
    app.run(port=5555, debug=True)
