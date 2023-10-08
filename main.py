from parking_lot.parking_lot import ParkingLot

def main():
    parking_lot = ParkingLot()

    while True:
        print("Options:")
        print("1. Assign a parking spot to a new vehicle")
        print("2. Retrieve parking spot number of a vehicle")
        print("3. Print Parking Lot Status")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.assign_parking_spot(vehicle_number)

            if "message" in result:
                print(result["message"])
            else:
                print(f"Parking spot assigned: {result}")
        
        elif choice == '2':
            vehicle_number = input("Enter vehicle number: ")
            result = parking_lot.get_parking_spot(vehicle_number)
            
            if "message" in result:
                print(result["message"])
            else:
                print(f"Vehicle is parked at: {result}")
        
        elif choice == '3':
            parking_lot.print_parking_lot_status()
        
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
