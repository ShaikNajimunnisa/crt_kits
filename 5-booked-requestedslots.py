slots=list(map(str,input("enter the booked slots: ").split()))
time_slot=input("Enter the requested slots: ")
print("slot already booked" if time_slot in slots else "slot is available")