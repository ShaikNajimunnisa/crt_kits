try:
    monthly_salary = float(input("Enter Monthly Salary: "))
    if(monthly_salary<=0):
        raise ValueError
    annual_salary = monthly_salary * 12
    print("Annual Salary: ",annual_salary)
except ValueError:
    print("Please enter  a valid salary amount.")    