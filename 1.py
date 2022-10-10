def show_employee(name="anonymous", salary=9000):
    print(f"{name} gets the salary {salary}")


name = input("Enter Employe name : ")
salary = input("Enter Salary : ")

show_employee(name, salary)
show_employee()
show_employee(salary=5000)
show_employee(name="Python")
