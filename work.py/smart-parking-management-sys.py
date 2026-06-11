class Vehicle:
    def __init__(self, no): self.no = no

class ParkingSlot:
    def __init__(self, id): self.id, self.free = id, True

class ParkingManager:
    def __init__(self, rate): self.rate, self.slots = rate, [ParkingSlot(i) for i in range(1, 101)]
    
    def park(self, v_no, hrs):
        for s in self.slots:
            if s.free:
                s.free = False
                fee = hrs * self.rate  # Formula: Hours × Rate
                print("="*50 + "\n              PARKING RECEIPT\n" + "="*50)
                print(f"\nVehicle Number : {v_no}\nHours Parked   : {hrs}\n\nParking Fee    : {fee}\n\n" + "="*50)
                return
        print("Parking full!")

# Test
ParkingManager(30).park("AP39AB1234", 5)