import json

try:
    with open("application.json", "r") as file:
        applications = json.load(file)
except FileNotFoundError:
    applications = []




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
        company_name = input("Company Name: ")
        position = input("Position: ")
        status = input("Status: ")

        intern_track_dict = {
            "company_name": company_name,
            "position": position,
            "status": status
            }
        print(f"""
        Application added!
            Company Name: {intern_track_dict["company_name"]} 
            Position: {intern_track_dict["position"]} 
            Status: {intern_track_dict["status"]}
            """
        )
        applications.append(intern_track_dict)
        with open("application.json", "w") as file:
            json.dump(applications, file, indent=4)
        # print(applications)
    
    elif choice == "2":
        if len(applications) == 0:
            print("No application found.")
        else:
            print("\n YOUR APPLICATIONS")

            for number, application in enumerate(applications, start=1):

                print(f"""
                {number}. Company Name: {application["company_name"]}
                          Position: {application["position"]}
                          Status: {application["status"]}
                """)
    elif choice == "3":
        if len(applications) == 0:
            print("No application found.")
        else:
            print("\n YOUR APPLICATIONS")
            for number, application in enumerate(applications, start=1):
                print(f"""
                {number}. Company Name: {application["company_name"]}
                          Position: {application["position"]}
                          Status: {application["status"]}
                """)
            try:
                update_application_number = int(input("Enter the application number you want to update: "))
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

                    with open("application.json", "w") as file:
                        json.dump(applications, file, indent=4)
                    print("Application updated successfully!")
                else:
                    print("Invalid application number.")
            except ValueError:
                print("Please enter a valid number.")
                continue
                    
    elif choice == "4":
        if len(applications) == 0:
            print("No application found.")
        else:
            print("\n YOUR APPLICATIONS")
            for number, application in enumerate(applications, start=1):
                print(f"""
                {number}. Company Name: {application["company_name"]}
                          Position: {application["position"]}
                          Status: {application["status"]}
                """)
            try:
                delete_application_number = int(input("Enter the application number you want to delete: "))
                index = delete_application_number - 1

                if 0 <= index < len(applications):
                    print(f"""Deleting application number {delete_application_number}...

                          Company Name: {applications[index]['company_name']}
                          Position: {applications[index]['position']}
                          Status: {applications[index]['status']}
                    """)

                    deleted_application = applications.pop(index)
                    with open("application.json", "w") as file:
                        json.dump(applications, file, indent=4)
                    print(f"Application for {deleted_application['company_name']} deleted successfully!")
                else:
                    print("Invalid application number.")
            except ValueError:
                print("Please enter a valid number.")
                continue

    elif choice == "5":
        print("Exit") 
        break   
    else: 
        print('Invalid choice, Please try again')
        

