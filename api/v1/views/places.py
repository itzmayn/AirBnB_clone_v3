from flask import jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity

@app_views.route('/places_search', methods=['POST'])
def places_search():
    """Search for Place objects based on JSON request data."""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    states = data.get('states', [])
    cities = data.get('cities', [])
    amenities = data.get('amenities', [])

    places = storage.all(Place).values()

    if not states and not cities and not amenities:
        return jsonify([place.to_dict() for place in places])

    result = []

    if states:
        for state_id in states:
            state = storage.get(State, state_id)
            if state:
                for city in state.cities:
                    if city not in cities:
                        cities.append(city.id)

    for place in places:
        if place.city_id in cities and all(amenity_id in place.amenities for amenity_id in amenities):
            result.append(place.to_dict())

    return jsonify(result)
