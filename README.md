# Parking Lot Tracker

A Python-based terminal application for tracking vehicles in a parking lot with two levels (A and B), each having a capacity to park 20 vehicles. The code is designed to efficiently assign parking spots to new vehicles and retrieve parking spot numbers for specific vehicles.

## Features

- Automatic assignment of parking spots to new vehicles.
- Retrieval of parking spot numbers for specific vehicles.
- Displaying the current parking lot status.
- Scalable and efficient code design.
- Clean and modular codebase.

## Code Structure

The code is organized into multiple files for modularity and cleanliness:

- `parking_lot/parking_level.py`: Defines the `ParkingLevel` class, responsible for managing individual parking levels (A and B).

- `parking_lot/parking_lot.py`: Defines the `ParkingLot` class, which manages the entire parking lot, including multiple levels.

- `main.py`: The main program that provides a user-friendly terminal interface to interact with the parking lot.

## Scalability

The code is designed with scalability in mind:

- **Modular Design**: Each parking level is encapsulated in its own class (`ParkingLevel`), allowing for easy addition of new levels if needed in the future.

- **Clean Separation of Concerns**: The code separates the responsibilities of parking levels and the overall parking lot, making it straightforward to add new features or extend functionality.

- **Efficient Data Structures**: The code uses efficient data structures like sets to manage available parking spots, ensuring fast lookups and assignments.

- **Clear Extensibility**: The code's structure and naming conventions make it easy to understand and extend. For instance, adding more parking levels is as simple as creating a new `ParkingLevel` instance.

## Cleanliness

The code follows best practices for clean and maintainable code:

- **Code Comments**: Detailed comments are provided to explain the purpose and functionality of classes and methods.

- **Modularization**: The code is divided into separate files for different components, promoting code organization and reusability.

- **Descriptive Naming**: Meaningful variable and method names enhance code readability.

- **Error Handling**: The code includes error handling to gracefully handle cases like a full parking lot or missing vehicles.

## Usage

To run the code, execute `main.py`:

```bash
python main.py
```

Follow the on-screen menu to perform parking lot operations.

## Dependencies

This project has no external dependencies and uses only Python's built-in libraries.

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.


---

This `README.md` provides a clear and detailed overview of the project, its features, code structure, scalability, cleanliness, and instructions for usage and contribution. It is designed to help users and potential contributors understand the project and its goals.
