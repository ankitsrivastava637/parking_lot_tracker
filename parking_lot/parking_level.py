from typing import Dict, Union, Optional

class ParkingLevel:

    def __init__(self, level_name: str, capacity: int):
        # Initialize a parking level with a name and capacity
        self.level_name = level_name
        self.capacity = capacity
        self.available_spots = set(range(1, capacity + 1))  # Initialize available spots
        self.occupied_spots = {}  # Initialize occupied spots


    def assign_spot(self, vehicle_number: str) -> Optional[Dict[str, Union[str, int]]]:
        # Assign a parking spot to a vehicle
        if not self.available_spots:
            return None  # Parking level is full

        spot = self.available_spots.pop()
        self.occupied_spots[vehicle_number] = spot

        return {"level": self.level_name, "spot": spot}
    

    def get_spot(self, vehicle_number: str) -> Optional[Dict[str, Union[str, int]]]:
        # Retrieve the parking spot of a vehicle
        spot = self.occupied_spots.get(vehicle_number)
        
        if spot is not None:
            return {"level": self.level_name, "spot": spot}
        
        return None  # Vehicle not found in this level
