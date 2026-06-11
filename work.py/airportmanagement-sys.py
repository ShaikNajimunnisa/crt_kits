class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number
        self.occupied_seats = set()  # Set → Occupied Seats
        self.passengers = []         # List → Passengers

    def assign_seat(self, passenger, seat):
        if seat in self.occupied_seats:
            return False
        self.occupied_seats.add(seat)
        self.passengers.append((passenger, seat))
        return True

class BoardingPass:
    def __init__(self, passenger, flight, seat):
        self.passenger = passenger
        self.flight = flight
        self.seat = seat
        self.status = "CHECK-IN COMPLETE"

    def generate_boarding_pass(self):
        print("=" * 50)
        print("               BOARDING PASS")
        print("=" * 50)
        print(f"\nPassenger Name : {self.passenger.name}")
        print(f"Flight Number  : {self.flight.flight_number}")
        print(f"Seat Number    : {self.seat}\n")
        print(f"Status         : {self.status}\n")
        print("=" * 50)

class Airport:
    def __init__(self):
        self.flights = {}

    def register_passenger(self, passenger_name, flight_number, seat):
        # create flight if not exists
        if flight_number not in self.flights:
            self.flights[flight_number] = Flight(flight_number)
        
        flight = self.flights[flight_number]
        passenger = Passenger(passenger_name)

        # assign seat
        if flight.assign_seat(passenger, seat):
            boarding_pass = BoardingPass(passenger, flight, seat)
            boarding_pass.generate_boarding_pass()
        else:
            print(f"Seat {seat} is already occupied on flight {flight_number}")

# Test Case
airport = Airport()
airport.register_passenger("Mason", "AI202", "12A")