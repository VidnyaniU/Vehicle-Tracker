import googlemaps
from datetime import datetime

GMAPS_API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=GMAPS_API_KEY)

def calculate_route(origin, destination):
    directions_result = gmaps.directions(
        origin,
        destination,
        mode="driving",
        departure_time=datetime.now()
    )
    return directions_result
