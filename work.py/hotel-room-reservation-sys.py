class Guest:
    def __init__(self, name): self.name = name

class Room:
    def __init__(self, type_, rate): self.type, self.rate = type_, rate

class Reservation:
    def book(self, guest, room, nights):
        total = room.rate * nights  # Formula: Room Price × Nights
        
        print("="*50)
        print("              HOTEL INVOICE")
        print("="*50)
        print(f"\nGuest Name     : {guest.name}")
        print(f"Room Type      : {room.type}\n")
        print(f"Nights Stayed  : {nights}\n")
        print(f"Total Amount   : ₹{total}\n")
        print("="*50)

# Test Case
g = Guest("Sophia")
r = Room("Deluxe", 3500)
Reservation().book(g, r, 3)