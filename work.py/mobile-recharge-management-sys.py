class Customer:
    def __init__(self, name, mobile):
        self.name = name 
        self.mobile = mobile

class RechargePlan:
    def __init__(self, name, amount):
        self.name = name 
        self.amount = amount

class Recharge:
    def select_plan(self, customer, plan):
        self.customer = customer
        self.plan =  plan
        self.generate_receipt()
    
    def generate_receipt(self):
        print("="*50)
        print("             RECHARGE RECEIPT")
        print("="*50)
        print(f"\nCustomer Name : {self.customer.name}")
        print(f"Mobile        : {self.customer.mobile}")
        print(f"\nPlan Selected : {self.plan.name}")
        print(f"Amount Paid   : ₹{self.plan.amount}\n")
        print("Status        : SUCCESSFUL\n")
        print("="*50)

# Test Case
c = Customer("Logan", "9876543210")
p = RechargePlan("Unlimited 84 Days", 799)
Recharge().select_plan(c, p)