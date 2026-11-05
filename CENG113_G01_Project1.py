def display_menu():
    # Display the main menu.
    choosed_option = input("""
    \nMain Menu:\n
    1. Display department employees
    2. Assign weekly tasks
    3. Generate meeting report
    4. Display meeting report
    5. Review meeting report
    6. Display task summary
    0. Exit\n
    Please select an option: """)

    if choosed_option == "1":
        display_employees(select_department())
    elif choosed_option == "2":
        assign_weekly_tasks(select_department())
    elif choosed_option == "3":
        generate_meeting_report(select_department())
    elif choosed_option == "4":
        display_meeting_report(select_department())
    elif choosed_option == "5":
        review_meeting_report(select_department())
    elif choosed_option == "6":
        display_task_summary(select_department())
    elif choosed_option == "0":
        print("Exiting the program.")
        exit()
    else:
        print("Invalid option. Please try again.")
        display_menu()

def select_department(): #çınar
    print("""
    Departments:
    1. Software Development
    2. Artificial Intelligence
    3. Research and Development  n25
    4. Quality Assurance
    5. IT Operations
    6. Human Resources
    
    0. Return to main menu\n""")
    
    try:
        department_choice = int(input("Select a department (0-6): "))
    except ValueError:
        print("\nInvalid department selection. Please try again.")
        department_choice = select_department()
        
    
    if department_choice == 0:
        print("Turning back to the main menu.")
        display_menu()
    else:
        return department_choice #!!!!!!returns integer!!!!!!!!!!!!!!!!!!!!!111!!

def display_employees(department): # almina
        with open("employees.txt") as f:
                if department == 1:
                    for i in range(1,71):
                        print(f.readline())
                elif department == 2:
                    for i in range(71,134):
                        print(f.readline())
                elif department == 3:
                    for i in range(134,190):
                        print(f.readline())
                elif department == 4:
                    for i in range(190,246):
                        print(f.readline())
                elif department == 5:
                    for i in range(246,302):
                        print(f.readline())
                elif department == 6:
                    for i in range(302,350):
                        print(f.readline())
pass

def assign_weekly_tasks(department): # yunus
    # Collect and save weekly tasks. Allow replacement of existing assignments only after report rejection.
    if department == "1":
        # Logic for software Development department
        dept_name = "Software Development"
    elif department == "2":
        # Logic for Artificial Intelligence department
        dept_name = "Artificial Intelligence"
    elif department == "3":
        # Logic for Research and Development department
        dept_name = "Research and Development"
    elif department == "4":
        # Logic for Quality Assurance department
        dept_name = "Quality Assurance"
    elif department == "5":
        # Logic for IT Operations department 
        dept_name = "IT Operations"
    elif department == "6":
        # Logic for Human Resources department 
        dept_name = "Human Resources"
    elif department == "0":
        print("Turning back to the main menu.")
        display_menu()
    else:
        print("Invalid department selection.")
        assign_weekly_tasks(select_department())

    proceed = False
    task_exists = False
    try:
        with open(f"tasks_{department}.txt", "r") as file:
            task_exists = True
    except FileNotFoundError:
        print(f"No existing tasks found for {dept_name} department. You can assign new tasks.")
        proceed = True
    if task_exists:
        try:
            with open(f"review_{department}.txt", "r") as f_rev:
                status = f_rev.readline().rstrip('\n')
                if status == "Rejected":
                    onay = input("Existing tasks will be overwritten, are you sure? (y/n): ").upper()
                    if onay == "Y":
                        proceed = True
                    else: 
                        return
                else:
                    print("Error: Cannot overwrite existing tasks unless the report has been rejected.")
                    return
            print(f"Tasks for {dept_name} department have been successfully assigned.")
        except FileNotFoundError:
            print("Error: Review file not found. Cannot determine report status.")
            return

    if proceed:
        with open("employees.txt", "r") as emp_file, open(f"tasks_{department}.txt", "w") as task_file:
            while True:
                #Read employee details and save them to variables until the end of the file is reached.
                emp_id = emp_file.readline().rstrip("\n") #this checks if there is a id, if not it means file ended
                if not emp_id:
                    break
                name = emp_file.readline().rstrip("\n")
                surname = emp_file.readline().rstrip("\n")
                title = emp_file.readline().rstrip("\n")
                dept = emp_file.readline().rstrip("\n")
                role = emp_file.readline().rstrip("\n")
                empty_line = emp_file.readline().rstrip("\n")
                if dept == dept_name:
                    full_name = name + " " + surname
                    print(f"\nID: {emp_id} | {full_name} | {title}")
                    
                    while True:
                        task_desc = input("Task description: ")
                        if task_desc != "":
                            break
                        print("Error: Task description cannot be empty. Please enter a valid task description.")
                        
                    while True:
                        hours_str = input("Estimated time (1-40 hours): ")
                        try:
                            hours = int(hours_str)
                            if 1 <= hours <= 40:
                                break
                            else:
                                print("Error: Time must be between 1 and 40 hours.")
                        except ValueError:
                            print("Error: Please enter a valid integer.")
                            
                    task_file.write(f"{emp_id}\n{task_desc}\n{hours}\n\n")
        print(f"Tasks for {dept_name} department have been successfully assigned.")
    display_menu()

def generate_meeting_report(department): #eren
    # Collect missing meeting metadata and build the report.
    try:
        date=input("Enter the meeting date (YYYY-MM-DD): ")
        if not date: raise ValueError("Date cannot be empty.")

        note=input("Enter the meeting note: ")
        if not note: raise ValueError("Note cannot be empty.")
    except ValueError as e:
        print(f"Invalid input: {e}")

def display_meeting_report(department): #çınar
    # Display the report, or explain that none exists.
    try:
        with open("meeting_report_N.txt", "r") as f:
            print(f.read())
    
    except FileNotFoundError:
        print("No meeting report found.")
    
    else:
        print("Meeting report displayed successfully.")
    
    finally:
        pass

def authenticate_manager(manager_id, password, department): #almina
    # Return True only when all authentication checks pass.
    with open("managers.txt", "r") as f:
        for line in f:
            if manager_id == line.rstrip("\n"):
                print("Manager ID found.")
                break
            else:
                continue
        if password == f.readline().rstrip("\n"):
            print("Password verified.")
        
            

    pass

def review_meeting_report(department): #yunus
    # Handle login attempts, decision input and report updates.
    pass

def display_task_summary(department): #eren
    # Calculate and display counts, total hours and average.
    pass

def main():
    display_menu()
    pass

if __name__ == "__main__":
    main()