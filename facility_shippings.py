from ast import Dict
from haversine import Unit, haversine
from numpy import long
from dataclasses import dataclass
from typing import Tuple

@dataclass
class Facility:
    object_id: int
    latitude: long
    longitude: long

    @property
    def position(self) -> Tuple[float, float]:
        return (self.latitude, self. longitude)

facilities = [
    Facility(object_id=14169, latitude=38.639842, longitude=-121.375627),
    Facility(object_id=8761, latitude=38.640552, longitude=-121.270352),
    Facility(object_id=22156, latitude=38.628266, longitude=-121.383062),
    Facility(object_id=12072, latitude=38.63599, longitude=-121.382828),
    Facility(object_id=15257, latitude=38.614271, longitude=-121.382833),
    Facility(object_id=10553, latitude=38.623154, longitude=-121.262295),
    Facility(object_id=17329, latitude=38.606743, longitude=-121.267905),
    Facility(object_id=10955, latitude=38.662804, longitude=-121.27621),
    Facility(object_id=4292, latitude=38.605739, longitude=-121.38305),
    Facility(object_id=3694, latitude=38.661062, longitude=-121.272069),
    Facility(object_id=18670, latitude=38.621356, longitude=-121.259911),
    Facility(object_id=22010, latitude=38.654186, longitude=-121.384669),
    Facility(object_id=12614, latitude=38.654208, longitude=-121.386227),
    Facility(object_id=16417, latitude=38.601754, longitude=-121.281785),
    Facility(object_id=4945, latitude=38.595205, longitude=-121.271461),
    Facility(object_id=17919, latitude=38.667263, longitude=-121.274088),
]
shipments = [
    {'id': 1,'pickup': 14169, 'delivery': 8761},
    {'id': 2,'pickup': 22156, 'delivery': 12072},
    {'id': 3,'pickup': 15257, 'delivery': 10553},
    {'id': 4,'pickup': 17329, 'delivery': 10955},
    {'id': 5,'pickup': 4292, 'delivery': 3694},
    {'id': 6,'pickup': 18670, 'delivery': 22010},
    {'id': 7,'pickup': 12614, 'delivery': 16417},
    {'id': 8,'pickup': 4945, 'delivery': 17919},
]
truck_position = {
  "latitude": 42.614586,
  "longitude": -73.702861,
}

def calculate_distance(point_a, point_b):
    return haversine(point_a, point_b, unit=Unit.MILES)

facilities_map: dict[int, Facility] = {}

for facility in facilities:
    facilities_map[facility.object_id] = facility

shipment_distances = {}
for shipment in shipments:
    facility_pickup = facilities_map[shipment["pickup"]]
    facility_delivery = facilities_map[shipment["delivery"]]

    distance = calculate_distance(facility_pickup.position, facility_delivery.position)
    shipment_distances[shipment["id"]] = distance

print(shipment_distances)

min_distance = None
max_distance = None

menor_valor = {}
maior_valor = {}

for shipment_id, distance in shipment_distances.items():
    if min_distance is None or distance < min_distance:
        min_distance = distance
        menor_valor = {shipment_id: distance}
    if max_distance is None or distance > max_distance:
        max_distance = distance
        maior_valor = {shipment_id: distance}

print(f"{menor_valor=} . {maior_valor=} ")