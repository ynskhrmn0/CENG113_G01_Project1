def display_menu():
    # Display the main menu.
    print("1. Display department employees\n2. Assign weekly tasks\n3. Generate meeting report\n4. Display meeting report\n5. Review meeting report\n6. Display task summary\n0. Exit")
    pass

def select_department(): #çınar
    print("0.Return to main menu\n Departments:\n 1.Software Development\n 2.Artificial Intelligence\n 3.Research and Development\n 4.Quality Assurance\n 5.IT Operations\n 6.Human Resources")
    department_choice = input("Select a department (0-6): ")
    return department_choice #returns string, not int

def display_employees(department): # almina
    while department != "1" or "2" or "3" or "4" or "5" or "6":
        print("Invalid department.")
        with open("employees.txt") as f:
                if department == "1":
                    for i in range(1,71):
                        print(f.readline())
                elif department == "2":
                    for i in range(71,134):
                        print(f.readline())
                elif department == "3":
                    for i in range(134,190):
                        print(f.readline())
                elif department == "4":
                    for i in range(190,246):
                        print(f.readline())
                elif department == "5":
                    for i in range(246,302):
                        print(f.readline())
                elif department == "6":
                    for i in range(302,350):
                        print(f.readline())
    pass

def assign_weekly_tasks(department): # yunus
    # Collect and save weekly tasks. Allow replacement of existing assignments only after report rejection.
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
    display_menu()
    department_choice = select_department()
    display_employees(department_choice)
    pass

if __name__ == "__main__":
    main()