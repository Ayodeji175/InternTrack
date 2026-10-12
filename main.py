applications = []



while True:
    print( """
======================================
                INTERNTRACK
======================================
        1. Add Application
        2. View Application
        3. Exit
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
        print("View Application")
    elif choice == "3":
        print("Exit") 
        break   
    else: 
        print('Invalid choice, Please try again')
        

