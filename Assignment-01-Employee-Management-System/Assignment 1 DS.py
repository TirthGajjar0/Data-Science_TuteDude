employees = {
    101: { 
        "name" : "Tirth",
        "age" : 20,
        "department":"IT",
        "salary":50000
    },
    
    102: { 
        "name" : "Jainil",
        "age" : 21,
        "department":"HR",
        "salary":30000
    }

}  

def add_employee() :
        
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists\n")
            return
        
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = int(input("Enter Employee Salary: "))

        employees[emp_id] = {
                "name" : name,
                "age" : age,
                "department" : department,
                "salary" : salary
            }
        print("Employee added successfully\n")


def view_employees():
     
        if not employees:
            print("No employees found\n")
        else:
            print("ID\tName\tAge\tDepartment\tSalary")
           
            for emp_id, details in employees.items():
                print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")
                print()


def search_employee():
     
        emp_id = int(input("Enter Employee ID: "))
        
        if emp_id in employees:
           
            details = employees[emp_id]
           
            print(f"Employee ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        
        else:
            print("Employee not found\n")



while True:
    
    print("EMS Menu:")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")
   
    try:
        choices = int(input("Enter your choice (1-4): "))
    
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    if choices == 1:
            add_employee()

    elif(choices == 2):
            view_employees()


    elif(choices == 3):
            search_employee()

    elif(choices == 4):
            print("exited successfully!")
            break

    else:
        print("Invalid choice")