print("---Welcome to BasicKanban---")
print("1) Register")
print("2) Login")
print("3) Exit")
print ("")

exit_option = '3'

print ("---Register---")
name = input("Enter your first name: ")
if name == exit_option:
    exit()

surname = input("Enter your last name: ")
if surname == exit_option:
    exit()


while True:
    username = input("Enter a username which contains an underscore ('_') and which doesn't exceed 5 characters: ")
    if username == exit_option:
        exit()
    if len(username) <= 5 and "_" in username:
        break
    else:
        print("Invalid username! Please try again.")


special_characters = "!@#$%^&*()_-+={}[]|\\';:<>,.?/"
capital_letters = "QWERTYUIOPLKJHGFDSAMNBVCXZ"
numbers = "1234567890"

while True:
    password = input("Enter a password (min 8 chars, 1 capital, 1 number, 1 special char): ")
    if password == exit_option:
        exit()
    if (len(password) >= 8 and 
        any(char in capital_letters for char in password) and 
        any(char in numbers for char in password) and 
        any(char in special_characters for char in password)):
        break
    else:
        print("Invalid password! Please try again.")
        

print ("")
print ("---Login---")
while True:
    login_username = input("Enter your username: ")
    if login_username == exit_option:
        exit()
    login_password = input("Enter your password: ")
    if login_password == exit_option:
        exit()

    if login_username == username and login_password == password:
        print ("Welcome",name,surname + "!")
        print ("")
        print("\nWelcome to BasicKanban\n")
        break
    else:
        print("Username or password incorrect. Please try again.\n")


while True:
    print("Main Menu:")
    print("1) Add Tasks")
    print("2) Show Report")
    print("3) Quit")
    
    option_selection = input("Choose an option: ")

    if option_selection == '1':
        task_number = int(input("Enter the number of tasks: "))
        task_number1 = 0
        task_list = []
        task_duray = 0

        while task_number1 < task_number:
            print("\n--- Enter details for Task " + str(task_number1) + " ---")

            task_name = input("Enter a short name for the task: ")

            while True:
                task_description = input("Enter the task description (max 50 characters): ")
                if len(task_description) <= 50:
                    print("Task successfully captured")
                    break
                else:
                    print("Please enter a task description of less than 50 characters")

            dev_deets = input("Enter the first and last name of the assigned developer: ")
            dev_lastname = dev_deets.strip().split()[-1]
            task_duration = float(input("Enter task duration in hours: "))
            task_duray += task_duration

            first_two = task_name[:2].upper()
            last_three = dev_lastname[-3:].upper()
            task_ID = first_two + ":" + str(task_number1) + ":" + last_three

            while True:
                print("Choose task status:")
                print("1. To Do")
                print("2. Doing")
                print("3. Done")
                task_sta = input("Enter 1, 2, or 3: ")
                if task_sta == '1':
                    task_status = "To Do"
                    break
                elif task_sta == '2':
                    task_status = "Doing"
                    break
                elif task_sta == '3':
                    task_status = "Done"
                    break
                else:
                    print("Invalid input. Please choose 1, 2, or 3.")

            print("\nTask Status:", task_status)
            print("Developer Details:", dev_deets)
            print("Task Number:", task_number1)
            print("Task Name:", task_name)
            print("Task Description:", task_description)
            print("Task ID:", task_ID)
            print("Task Duration:", task_duration, "hrs\n")

            task_number1 += 1

        print("Total Estimated Duration:", task_duray, "hrs\n")

    elif option_selection == '2':
        print("\nComing Soon\n")

    elif option_selection == '3':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid option. Please try again!\n")
