#!/usr/bin/python3
"""This module implements an endpoint to search for Place objects"""
from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.amenity import Amenity
from flasgger.utils import swag_from

@app_views.route("/places_search", methods=["POST"], strict_slashes=False)
@swag_from('documentation/place/put_place.yml', methods=['PUT'])
def places_search():
    """Retrieve Place objects based on the request body"""
    body = request.get_json()
    
    if type(body) != dict:
        abort(400, description="Not a JSON")  # Abort with 400 status if the request data is not in JSON format
    
    id_states = body.get("states", [])
    id_cities = body.get("cities", [])
    id_amenities = body.get("amenities", [])
    
    places = []
    
    if id_states == id_cities == []:
        places = storage.all(Place).values()
    else:
        # Retrieve States based on provided state IDs
        states = [
            storage.get(State, _id) for _id in id_states
            if storage.get(State, _id)
        ]
        # Get Cities associated with retrieved States
        cities = [city for state in states for city in state.cities]
        # Include individual Cities from provided city IDs
        cities += [
            storage.get(City, _id) for _id in id_cities
            if storage.get(City, _id)
        ]
        cities = list(set(cities) )  # Ensure unique cities
        
        # Retrieve Place objects associated with Cities
        places = [place for city in cities for place in city.places]

    # Retrieve Amenity objects based on provided amenity IDs
    amenities = [
        storage.get(Amenity, _id) for _id in id_amenities
        if storage.get(Amenity, _id)
    ]

    res = []
    for place in places:
        res.append(place.to_dict())
        for amenity in amenities:
            if amenity not in place.amenities:
                res.pop()  # Remove Place from results if it doesn't have a required amenity
                break

    return jsonify(res)
