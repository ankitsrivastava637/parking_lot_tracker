# Parking Lot Tracker

This Python-based Parking Lot Tracker is a terminal-based application designed to manage a parking lot with two levels, A and B, each having a capacity to park 20 vehicles. It offers the following features:

1. Automatically assigns a parking space to a new vehicle.
2. Retrieves the parking spot number of any particular vehicle using its unique identifier (vehicle number).


## Features

### Automatic Parking Spot Assignment

- The application automatically assigns a parking spot to a new vehicle based on the availability of spots in both Level A and Level B.
- It ensures that vehicles are evenly distributed between the two levels.
- If the parking lot is full, it displays a message indicating that no parking spot is available.

### Vehicle Spot Retrieval

- You can retrieve the parking spot number of any particular vehicle by providing its unique vehicle number.
- The application will display the level (A or B) and the spot number where the vehicle is parked.

### Status Display

- You can print the current status of the parking lot, including occupied spots and available spots for both Level A and Level B.


## Code Structure

The code is organized into multiple files for modularity and cleanliness:

- `parking_lot/parking_level.py`: Defines the `ParkingLevel` class, responsible for managing individual parking levels (A and B).

- `parking_lot/parking_lot.py`: Defines the `ParkingLot` class, which manages the entire parking lot, including multiple levels.

- `main.py`: The main program that provides a user-friendly terminal interface to interact with the parking lot.


## Usage

To use the Parking Lot Tracker, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/ankitsrivastava637/parking-lot-tracker.git
   ```

2. Navigate to the project directory.

   ```bash
   cd parking-lot-tracker
   ```

3. Run the application.

   ```bash
   python main.py
   ```

4. You will see a menu with the following options:
   - Assign a parking spot to a new vehicle.
   - Retrieve parking spot number of a vehicle.
   - Print Parking Lot Status.
   - Quit the application.

5. Choose an option by entering the corresponding number and follow the prompts.


## Scalability

The code is designed with scalability in mind:

- **Modular Design**: Each parking level is encapsulated in its own class (`ParkingLevel`), allowing for easy addition of new levels if needed in the future.

- **Clean Separation of Concerns**: The code separates the responsibilities of parking levels and the overall parking lot, making it straightforward to add new features or extend functionality.

- **Efficient Data Structures**: The code uses efficient data structures like sets to manage available parking spots, ensuring fast lookups and assignments.

- **Clear Extensibility**: The code's structure and naming conventions make it easy to understand and extend. For instance, adding more parking levels is as simple as creating a new `ParkingLevel` instance.


## Dependencies

This project has no external dependencies and uses only Python's built-in libraries.


---

This `README.md` provides a clear and detailed overview of the project, its features, code structure, scalability, and instructions for usage. It is designed to help users understand the project and its goals.









