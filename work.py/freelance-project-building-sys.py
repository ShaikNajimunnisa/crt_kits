class Client:
    def __init__(self, name): 
        self.name = name

class Project:
    def __init__(self, name, hrs, rate): 
        self.name = name 
        self.hrs = hrs 
        self.rate =  rate

class Invoice:
    def generate(self, client, project):
        amount = project.hrs * project.rate  # Formula: Hours × Hourly Rate
        
        print("="*50)
        print("                CLIENT INVOICE")
        print("="*50)
        print(f"\nClient Name   : {client.name}")
        print(f"Project Name  :\n{project.name}\n")
        print(f"Hours Worked  : {project.hrs}\n")
        print(f"Total Amount  : ₹{amount}\n")
        print("="*50)

# Test Case
c = Client("Olivia")
p = Project("Portfolio Website", 20, 1000)
Invoice().generate(c, p)