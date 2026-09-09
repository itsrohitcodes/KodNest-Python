# Process Different Employee Types Uniformly

class Employee:
    def show_details(self):
        pass


class PermanentEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        # Write your code here
        return f"{self.name} - Permanent - Salary: {self.salary}"


class ContractEmployee(Employee):
    def __init__(self, name, contract_months):
        self.name = name
        self.contract_months = contract_months

    def show_details(self):
        # Write your code here
        return f"{self.name} - Contract - Duration: {self.contract_months} months"


permanent_name = input()
salary = int(input())
contract_name = input()
contract_months = int(input())

# Create both objects
permanent = PermanentEmployee(permanent_name, salary)
contract = ContractEmployee(contract_name, contract_months)

# Store both objects in one list
employee_list = [permanent.show_details(), contract.show_details()]

# Process the list using one loop
for employee in employee_list:
    print(employee)