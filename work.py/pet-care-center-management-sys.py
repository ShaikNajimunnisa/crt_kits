class Owner:
    def __init__(self, name): 
        self.name = name

class Pet:
    def __init__(self, name): 
        self.name = name

class Appointment:
    def __init__(self):
        self.appointments = []  # List → Appointments
    
    def book(self, owner, pet, service, charge):
        self.appointments.append((owner, pet, service, charge))
        print("="*50)
        print("            SERVICE RECEIPT")
        print("="*50)
        print(f"\nOwner Name : {owner.name}")
        print(f"Pet Name   : {pet.name}\n")
        print(f"Service    : {service}\n")
        print(f"Amount     : ₹{charge}\n")
        print("="*50)

# Test Case
o = Owner("Ethan")
p = Pet("Bruno")
Appointment().book(o, p, "Grooming", 800)