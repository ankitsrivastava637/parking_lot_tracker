from typing import Optional, Dict, Union
from parking_lot.parking_level import ParkingLevel

class ParkingLot:

    def __init__(self):
        # Initialize a parking lot with two parking levels (A and B)
        self.levels = {
            'A': ParkingLevel('A', 20),
            'B': ParkingLevel('B', 20)
        }


    def assign_parking_spot(self, vehicle_number: str) -> Optional[Dict[str, Union[str, int]]]:
        # Assign a parking spot to a vehicle
        for level in ['A', 'B']:
            result = self.levels[level].assign_spot(vehicle_number)

            if result:
                return result
            
        return {"message": "Parking lot is full. Cannot assign a spot."}
    

    def get_parking_spot(self, vehicle_number: str) -> Optional[Dict[str, Union[str, int]]]: 
        # Retrieve the parking spot of a vehicle
        for level in ['A', 'B']:
            result = self.levels[level].get_spot(vehicle_number)

            if result:
                return result
            
        return {"message": "Vehicle not found in the parking lot."}
    

    def print_parking_lot_status(self):
        # Print the status of the parking lot (occupied and available spots)
        print("Parking Lot Status:")
        for level in ['A', 'B']:
            print(f"Level {level}: {self.levels[level].occupied_spots}")

        print("Available Spots:")
        for level in ['A', 'B']:
            print(f"Level {level}: {self.levels[level].available_spots}")
