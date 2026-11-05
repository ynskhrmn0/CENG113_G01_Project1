def display_menu():
    # Display the main menu.
    print("1. Display department employees\n2. Assign weekly tasks\n3. Generate meeting report\n4. Display meeting report\n5. Review meeting report\n6. Display task summary\n0. Exit")
    pass

def select_department(): #çınar
    # Validate and return a choice from 1 to 6.
    pass

def display_employees(department): # almina
    # Display employees in the selected department.
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
    # Run the menu loop and call the other functions.
    display_menu()
    pass

if __name__ == "__main__":
    main()