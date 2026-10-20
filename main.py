import json

def load_applications():
    try:
        with open("application.json", "r") as file:
            applications = json.load(file)
    except FileNotFoundError:
        applications = []

    return applications

def save_applications(applications):
    with open("application.json", "w") as file:
        json.dump(applications, file, indent=4)

def add_application(applications):
    company_name = input("Company Name: ")
    position = input("Position: ")
    status = input("Status: ")

    intern_track_dict = {
        "company_name": company_name,
        "position": position,
        "status": status

    }

    applications.append(intern_track_dict)
    save_applications(applications)

    print(f"""
    Application added!
        Company Name: {intern_track_dict["company_name"]} 
        Position: {intern_track_dict["position"]} 
        Status: {intern_track_dict["status"]}
    """
    )

def view_applications(applications):
    if len(applications) == 0:
        print("No application found.")
    else:
        print("\nYOUR APPLICATIONS")

        for number, application in enumerate(applications, start=1):
            print(f"""
            {number}. Company Name: {application["company_name"]}
                      Position: {application["position"]}
                      Status: {application["status"]}
            """)    

def update_application(applications):
    if len(applications) == 0:
        print("No application found.")
        return

    view_applications(applications)

    try:
        update_application_number = int(
            input("Enter the application number you want to update: ")
        )

        index = update_application_number - 1

        if 0 <= index < len(applications):
            print(f"""Updating for application number {update_application_number}...

                        Company Name: {applications[index]["company_name"]}
                        Position: {applications[index]["position"]}
                        Status: {applications[index]["status"]}

                    """)

            new_company_name = input("Enter new Company Name: ")
            new_position = input("Enter new Position: ")
            new_status = input("Enter new Status: ")

            applications[index]["company_name"] = new_company_name
            applications[index]["position"] = new_position
            applications[index]["status"] = new_status

            save_applications(applications)
            print("Application updated successfully!")
        else:
            print("Invalid application number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_application(applications):
    if len(applications) == 0:
        print("No application found.")
        return

    view_applications(applications)

    try:
        delete_application_number = int(
            input("Enter the application number you want to delete: ")
        )

        index = delete_application_number - 1

        if 0 <= index < len(applications):
            print(f"""Deleting application number {delete_application_number}...

Company Name: {applications[index]["company_name"]}
Position: {applications[index]["position"]}
Status: {applications[index]["status"]}
""")

            deleted_application = applications.pop(index)

            save_applications(applications)

            print(
                f'Application for {deleted_application["company_name"]} '
                "deleted successfully!"
            )

        else:
            print("Invalid application number.")

    except ValueError:
        print("Please enter a valid number.")

applications = load_applications()

while True:
    print( """
======================================
                INTERNTRACK
======================================
        1. Add Application
        2. View Application
        3. Update Application
        4. Delete Application
        5. Exit
    """)

    choice = input("Enter your choice:  ")

    if choice == "1":
        add_application(applications)
    
    elif choice == "2": 
        view_applications(applications)

    elif choice == "3":
        update_application(applications)
                    
    elif choice == "4":
        delete_application(applications)

    elif choice == "5":
        print("Exit") 
        break   
    else: 
        print('Invalid choice, Please try again')
        

