def display_menu():
    # Display the main menu.
    choosed_option = input("""\n1. Display department employees
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
    department_choice = input("Select a department (1-6): ")
    return department_choice

def display_employees(department): # almina
    # Display employees in the selected department.
    pass

def assign_weekly_tasks(department): # yunus
    # Collect and save weekly tasks. Allow replacement of existing assignments only after report rejection.
    if department == "1":
        # Logic for software department
        dept_name = "Software"
        pass
    elif department == "2":
        # Logic for Artificial Intelligence department
        dept_name = "Artificial Intelligence"
        pass
    elif department == "3":
        # Logic for Research and Development department
        dept_name = "Research and Development"
        pass
    elif department == "4":
        # Logic for Quality Assurance department
        dept_name = "Quality Assurance"
        pass
    elif department == "5":
        # Logic for IT Operations department 
        dept_name = "IT Operations"
        pass
    elif department == "6":
        # Logic for Human Resources department 
        dept_name = "Human Resources"
        pass
    elif department == "0":
        print("Turning back to the main menu.")
        display_menu()
    else:
        print("Invalid department selection.")
        assign_weekly_tasks(select_department())
    pass

def generate_meeting_report(department): #eren
    # Collect missing meeting metadata and build the report.
    pass

def display_meeting_report(department): #çınar
    # Display the report, or explain that none exists.
    pass

def authenticate_manager(manager_id, password, department): #almina
    # Return True only when all authentication checks pass.
    pass

def review_meeting_report(department): #yunus
    # Handle login attempts, decision input and report updates.
    pass

def display_task_summary(department): #eren
    # Calculate and display counts, total hours and average.
    pass

def main():
    # Run the menu loop and call the other functions.
    display_menu()
    pass

if __name__ == "__main__":
    main()
