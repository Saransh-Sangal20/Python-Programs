def gmail_verify(email):
    if ("@" in email):
        if ("gmail" in email):
            if (" " not in email):
                print("Valid gmail address")
            else:
                print("Invalid gmail address")
        else:
            print("Invalid gmail address")
    else:
        print("Invalid gmail address")
email = input("Enter your email: ")
gmail_verify(email)