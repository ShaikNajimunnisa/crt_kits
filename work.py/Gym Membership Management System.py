class Member:
    def __init__(self, name):
        self.name = name

class MembershipPlan:
    def __init__(self, name, monthly_fee): 
        self.name = name
        self.fee =  monthly_fee

class Gym:
    def register(self, member, plan, months):
        total = plan.fee * months  # Formula: Monthly Fee × Duration
        
        print("="*50)
        print("             MEMBERSHIP RECEIPT")
        print("="*50)
        print(f"\nMember Name : {member.name}\n")
        print(f"Plan        : {plan.name}\n")
        print(f"Duration    : {months} Months\n")
        print(f"Total Fee   : ₹{total}\n")
        print("="*50)

# Test Case
m = Member("Ava")
p = MembershipPlan("Premium", 2000)
Gym().register(m, p, 6)