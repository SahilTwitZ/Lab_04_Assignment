# MD SHAHIL
# E22CSEU0017
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}\nName: {self.name}\nAge: {self.age}\nSalary: {self.salary}"

def search_employees(employees, parameter, value):
    results = []
    if parameter == 1:  # Search by Age
        for emp in employees:
            if emp.age == value:
                results.append(emp)
    elif parameter == 2:  # Search by Name
        for emp in employees:
            if emp.name.lower() == value.lower():
                results.append(emp)
    elif parameter == 3:  # Search by Salary
        for emp in employees:
            if emp.salary >= value:
                results.append(emp)
    else:
        print("Invalid search parameter!")
        return

    if len(results) == 0:
        print("No results found.")
    else:
        for emp in results:
            print(emp)
            print()

# Create employee objects
employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

# User input for search
print("Search Options:")
print("1. Age")
print("2. Name")
print("3. Salary")
search_param = int(input("Enter the search parameter: "))

if search_param in [1, 2, 3]:
    search_value = input("Enter the search value: ")
    search_employees(employees, search_param, search_value)
else:
    print("Invalid search parameter!")