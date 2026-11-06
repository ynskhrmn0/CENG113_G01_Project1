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

def select_department(): #çınar #done
    print("""\n
    Departments:
    1.Software Development
    2.Artificial Intelligence
    3.Research and Development
    4.Quality Assurance
    5.IT Operations
    6.Human Resources
    0.Return to main menu\n""")
    department_choice = input("Select a department (0-6): ")
    return department_choice #returns string, not int

def display_employees(department): # almina #done
        with open("employees.txt", "r") as f:
                if department == "1":
                    for i in range(1,71):
                        print(f.readline().rstrip('\n'))
                elif department == "2":
                    for i in range(71,134):
                        print(f.readline().rstrip('\n'))
                elif department == "3":
                    for i in range(134,190):
                        print(f.readline().rstrip('\n'))
                elif department == "4":
                    for i in range(190,246):
                        print(f.readline().rstrip('\n'))
                elif department == "5":
                    for i in range(246,302):
                        print(f.readline().rstrip('\n'))
                elif department == "6":
                    for i in range(302,350):
                        print(f.readline().rstrip('\n'))

def assign_weekly_tasks(department): # yunus #done
    # Collect and save weekly tasks. Allow replacement of existing assignments only after report rejection.
    if department == "1":
        dept_name = "Software Development"
    elif department == "2":
        dept_name = "Artificial Intelligence"
    elif department == "3":
        dept_name = "Research and Development"
    elif department == "4":
        dept_name = "Quality Assurance"
    elif department == "5":
        dept_name = "IT Operations"
    elif department == "6":
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
    pass

def authenticate_manager(manager_id, password, department): #almina
    with open("manager_passwords.txt", "r") as pass_check:
        for line in pass_check:
                if manager_id == line.rstrip('\n'):
                    continue
                else:
                    print("Manager ID not found.")
                    return False
                    break
            if password == line.rstrip('\n'):
                continue
            else:
                print("Incorrect password.")
                return False
    with open("employees.txt", "r") as passdep_check:
        for line in passdep_check:
            if manager_id == line.rstrip('\n'):
                for i in range(5):
                    passdep_check.readline()
                if department == line.rstrip('\n'):
                    passdep_check.readline()
                    if str(passdep_check.readline().rstrip('\n')) == "Manager":
                        return True
                    else:
                        print("User is not a manager.")
                        return False
                        break
                else:
                    print("Manager does not belong to the selected department.")
                    return False
                    break

def review_meeting_report(department): #yunus
    # Handle login attempts, decision input and report updates.
    if department == "1":
        dept_name = "Software Development"
    elif department == "2":
        dept_name = "Artificial Intelligence"
    elif department == "3":
        dept_name = "Research and Development"
    elif department == "4":
        dept_name = "Quality Assurance"
    elif department == "5":
        dept_name = "IT Operations"
    elif department == "6":
        dept_name = "Human Resources"

    try:
        with open(f"review_{department}.txt", "r") as rev_file:
            status = rev_file.readline().rstrip("\n")
            rev_id = rev_file.readline().rstrip("\n")
            rev_name = rev_file.readline().rstrip("\n")
            rev_comment = rev_file.readline().rstrip("\n")
            meeting_date = rev_file.readline().rstrip("\n")
            meeting_note = rev_file.readline().rstrip("\n")
            
        if status != "Pending Approval":
            print(f"This report is already {status}.")
            return
        else:
            print("Pending approval report details:")
            
    except FileNotFoundError:
        print("Error: No existing report found to review.")
        return

    attempts = 3
    auth_success = False
    logged_in_id = ""
    manager_full_name = ""
    
    while attempts > 0:
        mgr_id_input = input("\nManager ID: ")
        mgr_pass_input = input("Password: ")
        
        if authenticate_manager(mgr_id_input, mgr_pass_input, department):
            auth_success = True
            logged_in_id = mgr_id_input
            break
        else:
            attempts -= 1
            print("Invalid manager ID or password, or unauthorized department.")
            
    if not auth_success:
        return

    with open("employees.txt", "r") as emp_file:
        while True:
            e_id = emp_file.readline().rstrip("\n")
            if not e_id:
                break
            e_name = emp_file.readline().rstrip("\n")
            e_surname = emp_file.readline().rstrip("\n")
            e_title = emp_file.readline().rstrip("\n")
            e_dept = emp_file.readline().rstrip("\n")
            e_role = emp_file.readline().rstrip("\n")
            emp_file.readline() 
            
            if e_id == logged_in_id:
                manager_full_name = e_name + " " + e_surname
                break
    print("\n--- MEETING REPORT ---")
    try:
        with open(f"meeting_report_{department}.txt", "r") as rep_file:
            while True:
                line = rep_file.readline().rstrip("\n")
                if not line:
                    break
                print(line)
    except FileNotFoundError:
        print("Error: Meeting report file is missing.")
        return
    print("----------------------")
    while True:
        decision = input("\nDecision - (A)pprove, (R)eject, (C)ancel: ").upper()
        if decision == "C" or decision == "CANCEL":
            print("Review cancelled. Returning to main menu.")
            return
        elif decision == "A" or decision == "APPROVE":
            new_status = "Approved"
            comment = input("Approval comment (optional): ")
            if comment == "":
                comment = "-"
            break
        elif decision == "R" or decision == "REJECT":
            new_status = "Rejected"
            while True:
                comment = input("Rejection comment (required): ")
                if comment != "":
                    break
                print("Error: Rejection comment cannot be empty.")
            break
        else:
            print("Invalid choice. Please enter A, R, or C.")
    with open(f"review_{department}.txt", "w") as rev_file:
        rev_file.write(f"{new_status}\n{logged_in_id}\n{manager_full_name}\n{comment}\n{meeting_date}\n{meeting_note}\n")

    try:
        employee_count = 0
        total_hours = 0
        with open("employees.txt", "r") as emp_file, \
             open(f"tasks_{department}.txt", "r") as task_file, \
             open(f"meeting_report_{department}.txt", "w") as report_file:
            report_file.write(f"Department: {dept_name}\n")
            report_file.write(f"Meeting Date: {meeting_date}\n")
            report_file.write(f"Meeting Note: {meeting_note}\n")
            report_file.write(f"Status: {new_status}\n\n")

            while True:
                emp_id = emp_file.readline().rstrip("\n")
                if emp_id == "":
                    break
                name = emp_file.readline().rstrip("\n")
                surname = emp_file.readline().rstrip("\n")
                title = emp_file.readline().rstrip("\n")
                emp_dept = emp_file.readline().rstrip("\n")
                emp_file.readline()  # role
                emp_file.readline()  # blank line
                if emp_dept != dept_name:
                    continue

                task_file.readline()  # task owner ID
                task_desc = task_file.readline().rstrip("\n")
                hours = int(task_file.readline())
                task_file.readline()  # blank line

                report_file.write(f"ID: {emp_id} | {name} {surname} | {title}\n")
                report_file.write(f"Task: {task_desc}\n")
                report_file.write(f"Estimated Hours: {hours}\n\n")
                employee_count += 1
                total_hours += hours

            if employee_count > 0:
                average = total_hours / employee_count
            else:
                average = 0
            report_file.write(f"Number of employees: {employee_count}\n")
            report_file.write(f"Total estimated hours: {total_hours}\n")
            report_file.write(f"Average estimated hours: {average:.2f}\n\n")
    except FileNotFoundError:
        print("Error: The tasks file is missing.")
        return

    print(f"The report has been {new_status.lower()}.")
    
def display_task_summary(department): #eren
    # Calculate and display counts, total hours and average.
    pass

def main():
    while True:
        display_menu()

if __name__ == "__main__":
    main()
