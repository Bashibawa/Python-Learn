name = input ("What is your user name?\n")
allowed_users = ['Seyi', 'Mike', 'Love']
allowed_password = "passwordSeyi"

if name in allowed_users:
    password = input ("Your password? \n")
    

    if password == allowed_password:
        print("Welcome %s" % name)
        print("These are the available options:")
        print('1. Withdrwal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selected_option = int(input("Please select an option:"))

        if selected_option == 1:
            print('You selected %s' % selected_option)
            pass
        elif selected_option == 2:
            print('You selected %s' % selected_option)
            pass
        elif selected_option == 3:
            print('You selected %s' % selected_option)
            pass
        else:
            print("Invalid option selected, please try again")
    else:
        print("Password incorrect, please try again")

else:
    print("Name not found please try again!")