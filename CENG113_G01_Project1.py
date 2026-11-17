# CENG113_G01_Project1.py

# Yunus Kahraman 330201034
# Eren Kulaksız 340201037
# Almina Coşkun 340201032
# Çınar Umut Öveyik 340201007

def display_menu(): # yunus
    # Display the main menu.
    try:
        choosed_option = int(input("""
    Main Menu:\n
        1. Display department employees
        2. Assign weekly tasks
        3. Generate meeting report
        4. Display meeting report
        5. Review meeting report
        6. Display task summary
        0. Exit\n
        Please select an option: """))
        if choosed_option == 1:
            display_employees(select_department())
        elif choosed_option == 2:
            assign_weekly_tasks(select_department())
        elif choosed_option == 3:
            generate_meeting_report(select_department())
        elif choosed_option == 4:
            display_meeting_report(select_department())
        elif choosed_option == 5:
            review_meeting_report(select_department())
        elif choosed_option == 6:
            display_task_summary(select_department())
        elif choosed_option == 0:
            print("Exiting the program.")
            exit()
        else:
            print("\nInvalid option. Please try again.")
            display_menu()
    except TypeError:
        print("\nInvalid option. Please try again.")
        display_menu()

def select_department(): # çınar
    department_choice = input("""
Departments:\n
    1. Software Development
    2. Artificial Intelligence
    3. Research and Development
    4. Quality Assurance
    5. IT Operations
    6. Human Resources
    0. Return to main menu\n
    Select a department to continue (0-6): """)

    while True:  #repeat until a valid input
        try:
            if 0 < int(department_choice) <=6:
                return department_choice # returns department choice as string (1-6)
            elif int(department_choice) == 0:
                print("\nReturning to the main menu.")
                display_menu() #return to menu if 0
            else:
                raise ValueError
        except ValueError:
            department_choice = input("""
Departments:\n
    1. Software Development
    2. Artificial Intelligence
    3. Research and Development
    4. Quality Assurance
    5. IT Operations
    6. Human Resources
    0. Return to main menu\n
    Invalid input.
    Enter a number 0-6 to continue: """)


def display_employees(department): # almina
        try:
            with open("employees.txt", "r") as f:
                if department == "1":
                    line_start, line_end = 1, 70
                elif department == "2":
                    line_start, line_end = 71, 133
                elif department == "3":
                    line_start, line_end = 134, 189
                elif department == "4":
                    line_start, line_end = 190, 245
                elif department == "5":
                    line_start, line_end = 246, 301
                elif department == "6":
                    line_start, line_end = 302, 350
                else:
                    return
                
                line_num = 1
                while line_num < line_start:
                    #skips lines until the start of the selected department
                    f.readline()
                    line_num += 1

                while line_num <= line_end:
                    line = f.readline()
                    if not line:
                        #stop early if the file ends unexpectedly idk
                        break
                    print(line.strip("\n"))
                    line_num += 1
        except FileNotFoundError:
            print("Error: employees.txt file not found.")
            
            line_num = 1
            while line_num < line_start:
                #skips lines until the start of the selected department
                f.readline()
                line_num += 1

            while line_num <= line_end:
                line = f.readline()
                if not line:
                    #stop early if the file ends unexpectedly idk
                    break
                print(line.strip("\n"))
                line_num += 1
            f.close()

def assign_weekly_tasks(department): # yunus
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
            file.close()
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
                f_rev.close()
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
                        if task_desc.strip() != "":
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
            task_file.close()
            emp_file.close() 
        print(f"Tasks for {dept_name} department have been successfully assigned.")


def generate_meeting_report(department): # eren
    # Collect missing meeting metadata and build the report.

    # map the department number to its name. needed when we read the employees.txt file and when we write the report files.
    if department == "1":
        department_name = "Software Development"
    elif department == "2":
        department_name = "Artificial Intelligence"
    elif department == "3":
        department_name = "Research and Development"
    elif department == "4":
        department_name = "Quality Assurance"
    elif department == "5":
        department_name = "IT Operations"
    elif department == "6":
        department_name = "Human Resources"
    else:
        print("Error: invalid department.")
        return

    # read the review_N.txt file
    status = "" # stays empty if no report exists yet
    meeting_date = ""
    meeting_note = ""
    try:
        with open(f"review_{department}.txt", "r") as review_file:
            status = review_file.readline().strip()
            review_file.readline()  # reviewer ID (not needed)
            review_file.readline()  # reviewer name (not needed)
            review_file.readline()  # review comment (not needed)
            meeting_date = review_file.readline().strip()
            meeting_note = review_file.readline().strip()
            review_file.close()
    except FileNotFoundError:
        print(f"No report found for {department_name}. A new report will be generated.")
        status = "" # expected before the first generation

    # report already exists and is not rejected
    if status == "Pending Approval" or status == "Approved":
        print(f"A report for {department_name} already exists . Status: {status}.")
        print("No changes were made.")
        return

    ### Everything below is for first generation or regeneration after a rejection.

    # check if the tasks file exists
    try:
        tasks_file = open(f"tasks_{department}.txt", "r")
        tasks_file.close()
    except FileNotFoundError:
        print("No tasks have been assigned yet. Please assign tasks first using option 2.")
        return

    # ask if user wants to regenerate the rejected report. if not, we stop here
    if status == "Rejected":
        answer = input("The report was rejected. Overwrite it with the saved tasks? (y/n): ").strip().lower()
        while answer != "y" and answer != "n":
            print("Invalid input: Please enter y or n.")
            answer = input("The report was rejected. Overwrite it with the saved tasks? (y/n): ").strip().lower()
        if answer == "n":
            print("Cancelled. No changes were made.")
            return


    employee_count = 0
    total_hours = 0
    employee_details = "" # the employee part of the report, built as one string

    # check the employees file for employees of this department. for each employee in this department, check the tasks file for their task and make sure everything is valid.
    try:
        with open("employees.txt", "r") as employees_file:
            # each employee record has 6 lines followed by one blank line
            employee_id = employees_file.readline().strip() # line 1
            while employee_id != "":
                name = employees_file.readline().strip() # line 2
                surname = employees_file.readline().strip() # line 3
                title = employees_file.readline().strip() # line 4
                employee_department = employees_file.readline().strip() # line 5
                employees_file.readline() # role (not needed) # line 6
                employees_file.readline() # blank line

                # only look at employees of the selected department
                if employee_department == department_name:

                    # search tasks file for this employee's task(s)
                    # there might be a more efficient way of doing this but this works so whatever
                    task_count = 0
                    task_description = ""
                    hours_text = ""
                    with open(f"tasks_{department}.txt", "r") as tasks_file:
                        task_id = tasks_file.readline().strip() # line 1 
                        while task_id != "":
                            current_description = tasks_file.readline().strip() # line 2
                            current_hours_text = tasks_file.readline().strip() # line 3
                            tasks_file.readline() # blank line
                            if task_id == employee_id:
                                task_count += 1
                                task_description = current_description
                                hours_text = current_hours_text
                            task_id = tasks_file.readline().strip() # set next task's line 1
                        tasks_file.close()

                    # the employee must have exactly one valid task
                    if task_count != 1:
                        print(f"Employee {employee_id} does not have exactly one task.")
                        print("The report cannot be generated.")
                        return
                    if task_description == "":
                        print(f"Employee {employee_id} has an empty task description.")
                        print("The report cannot be generated.")
                        return
                    try:
                        task_hours = int(hours_text)
                    except ValueError:
                        print(f"Employee {employee_id} has invalid hours.")
                        print("The report cannot be generated.")
                        return
                    if task_hours < 1 or task_hours > 40:
                        print(f"Employee {employee_id} has hours outside 1-40.")
                        print("The report cannot be generated.")
                        return

                    # task is valid so we add this employee to the report text
                    employee_details += f"Employee ID: {employee_id}\n"
                    employee_details += f"Name: {name} {surname}\n"
                    employee_details += f"Title: {title}\n"
                    employee_details += f"Task: {task_description}\n"
                    employee_details += f"Estimated Hours: {task_hours}\n\n"
                    employee_count += 1
                    total_hours += task_hours

                employee_id = employees_file.readline().strip() # set next employee's line 1
            employees_file.close()
    except FileNotFoundError:
        print("Error: employees.txt was not found.")
        return

    if employee_count == 0:
        print("No employees were found for this department.")
        return
    average_hours = total_hours / employee_count

    # get the meeting date and note on first generation. a rejected report keeps the old ones
    if status != "Rejected":
        meeting_date = input("Enter the meeting date (e.g. 2026-11-02): ").strip()
        while meeting_date == "":
            print("Invalid input: The meeting date cannot be empty.")
            meeting_date = input("Enter the meeting date (e.g. 2026-11-02): ").strip()

        meeting_note = input("Enter a one-line meeting note: ").strip()
        while meeting_note == "":
            print("Invalid input: The meeting note cannot be empty.")
            meeting_note = input("Enter a one-line meeting note: ").strip()

    # write new review_N.txt
    with open(f"review_{department}.txt", "w") as review_file:
        review_file.write("Pending Approval\n")
        review_file.write("-\n")  # reviewer ID
        review_file.write("-\n")  # reviewer name
        review_file.write("-\n")  # review comment
        review_file.write(meeting_date + "\n")
        review_file.write(meeting_note + "\n")
        review_file.close()

    # write meeting_report_N.txt
    with open(f"meeting_report_{department}.txt", "w") as report_file:
        report_file.write(f"Department: {department_name}\n")
        report_file.write(f"Meeting Date: {meeting_date}\n")
        report_file.write(f"Meeting Note: {meeting_note}\n")
        report_file.write("Status: Pending Approval\n")
        report_file.write("Reviewer ID: -\n")
        report_file.write("Reviewer Name: -\n")
        report_file.write("Review Comment: -\n\n")
        report_file.write(employee_details)
        report_file.write(f"Number of Employees: {employee_count}\n")
        report_file.write(f"Total Estimated Hours: {total_hours}\n")
        report_file.write(f"Average Estimated Hours: {average_hours:.2f}\n")
        report_file.close()

    print(f"Meeting report for {department_name} was generated (status: Pending Approval).")

def display_meeting_report(department): # çınar
    # Display the report, or explain that none exists.
    try:
        with open(f"meeting_report_{department}.txt", "r") as f:
            print()
            print(f.read()) #read file content if exists
            f.close()
    
    except FileNotFoundError:
        print("\nNo meeting report found.") #give an error message if file doesn't exists, continue the program
    
    else:
        print("Meeting report displayed successfully.")

def authenticate_manager(manager_id, password, department): # almina
    authenticated = False
    try:
        with open("manager_passwords.txt", "r") as pass_check:
            while True:
                id_line = pass_check.readline()
                if not id_line:  # End of file reached
                    break
                
                id_str = id_line.rstrip('\n')
                if not id_str:  # Skip blank lines
                    continue
                
                pass_str = pass_check.readline().rstrip('\n')
                
                if id_str == manager_id:
                    if pass_str == password:
                        authenticated = True
                    else:
                        print("Incorrect password.")
                        return False
                    break
    except FileNotFoundError:
        print("File not found.")
        return False

    if not authenticated:
        print("Manager ID not found.")
        return False

    manager_found = False

    if department == "1":
        department = "Software Development"
    elif department == "2":
        department = "Artificial Intelligence"
    elif department == "3":
        department = "Research and Development"
    elif department == "4":
        department = "Quality Assurance"
    elif department == "5":
        department = "IT Operations"
    elif department == "6":
        department = "Human Resources"

    try:
        with open("employees.txt", "r") as passdep_check:
            while True:
                emp_id_line = passdep_check.readline()
                if not emp_id_line:
                    break
                
                emp_id = emp_id_line.rstrip('\n')
                if not emp_id:  
                    continue
                
                emp_fname = passdep_check.readline().rstrip('\n')
                emp_lname = passdep_check.readline().rstrip('\n')
                emp_title = passdep_check.readline().rstrip('\n')
                emp_dept = passdep_check.readline().rstrip('\n')
                emp_role = passdep_check.readline().rstrip('\n')
                
                if emp_id == manager_id:
                    manager_found = True
                    
                    if emp_dept != department:
                        print(f"Manager does not belong to the selected department. (File has '{emp_dept}', passed '{department}')")
                        return False
                        
                    if emp_role != "Manager":
                        print("User is not a manager.")
                        return False
                    return True
    except FileNotFoundError:
        print("employees.txt not found.")
        return False

    if not manager_found:
        print("Manager ID not found in employee records.")
        return False

    return False

def review_meeting_report(department): # yunus
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
            rev_file.close()
            
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

    try:
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
            emp_file.close()
    except FileNotFoundError:
        print("Error: employees.txt file not found.")

    
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
        emp_file.close()
    print("\n--- MEETING REPORT ---")
    try:
        with open(f"meeting_report_{department}.txt", "r") as rep_file:
            while True:
                line = rep_file.readline()
                if not line:
                    break
                else:
                    line = line.rstrip("\n") # we do this so blank seperator lines don't become "" and cause the loop to break
                print(line)
            rep_file.close()
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
        rev_file.close()

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
            emp_file.close()
            task_file.close()
            report_file.close()
    except FileNotFoundError:
        print("Error: The tasks file is missing.")
        return

    print(f"\nThe report has been {new_status.lower()}.")
    
def display_task_summary(department): # eren
    # Calculate and display counts, total hours and average.

    if department == "1":
        department_name = "Software Development"
    elif department == "2":
        department_name = "Artificial Intelligence"
    elif department == "3":
        department_name = "Research and Development"
    elif department == "4":
        department_name = "Quality Assurance"
    elif department == "5":
        department_name = "IT Operations"
    elif department == "6":
        department_name = "Human Resources"
    else:
        print("Error: invalid department.")
        return

    # count department employees
    employee_count = 0
    try:
        with open("employees.txt", "r") as employees_file:
            # each employee record has 6 lines followed by one blank line
            employee_id = employees_file.readline().strip()
            while employee_id != "":
                employees_file.readline()  # name (not needed)
                employees_file.readline()  # surname (not needed)
                employees_file.readline()  # title (not needed)
                employee_department = employees_file.readline().strip()
                employees_file.readline()  # role (not needed)
                employees_file.readline()  # blank separator line

                if employee_department == department_name:
                    employee_count += 1

                employee_id = employees_file.readline().strip()
            employees_file.close()
    except FileNotFoundError:
        print("Error: employees.txt was not found.")
        return

    # count the tasks and total hours
    assigned_tasks = 0
    total_hours = 0
    try:
        with open(f"tasks_{department}.txt", "r") as tasks_file:
            task_id = tasks_file.readline().strip() # line 1
            while task_id != "":
                tasks_file.readline()  # line 2, task description (not needed)
                hours_text = tasks_file.readline().strip() # line 3
                tasks_file.readline()  # blank line

                try:
                    total_hours += int(hours_text)
                    assigned_tasks += 1
                except ValueError:
                    pass  # ignore a record with invalid hours

                task_id = tasks_file.readline().strip()
            tasks_file.close()
    except FileNotFoundError:
        pass  # no tasks file yet. not a problem, tasks and hours stay at 0

    
    if assigned_tasks == 0:
        average_text = "N/A"  # avoid dividing by zero
    else:
        average_text = f"{total_hours / assigned_tasks:.2f}"

    # display summary
    print(f"\nTask summary for {department_name}")
    print(f"Number of employees: {employee_count}")
    print(f"Number of assigned tasks: {assigned_tasks}")
    print(f"Total estimated hours: {total_hours}")
    print(f"Average hours per assigned task: {average_text}")

def main():
    while True:
        display_menu()

if __name__ == "__main__":
    main()
