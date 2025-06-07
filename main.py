import file_utils as util
import patient as p

AVAILABLE_DOMAIN = ['gmail.com','hotmail.com']

def login():
    while(True):
        print("------------------------------\n"
        "Clinic Management System\n"
        "------------------------------\n")

        #input email
        user_email = input("Please enter your email (leave blank to exit): ")

        #exit case
        if user_email == '':
            print("------------------------------\n"
                  "Exiting program\n"
                  "------------------------------\n")
            break

        #validate user email
        email_parts = user_email.strip().split('@')
        #check has only 1 @ and both sides are not empty
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1] :
            print("Invalid email format!")
            continue
        else:
            user_name, user_domain = email_parts
        #check if domain is a supported domain
        if user_domain not in AVAILABLE_DOMAIN:
            print("domain is not supported!")
            continue

        #find user email in file and assign line as the found line
        line = util.search_in_file("user.txt", email = user_email)[0]
        if line is None:
            print("No email found")
            continue

        #assign line into variables for more readible code
        email, raw_password, user_id, user_role = line

        #gives user 3 attempts to enter password
        attempt = 3

        while attempt > 0:
            #input password
            input_password = input("Please enter your password ")

            #check password
            if input_password == raw_password:
                match user_role:
                    case 'patient':
                        p.menu(user_id)
                    case _:
                        print(f'menu for {user_role} has\'nt been implemented')
                break
            else:
                print("WRONG PASSWORD")
                attempt -= 1
        else:
            print("Too many fails, please log in again.")

login()



