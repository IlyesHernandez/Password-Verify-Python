# Creation of 'password' and 'password_verify' variables

password = input("Enter your password ")
password_verify = input("Enter your password again")

if password == password_verify:
    print("Your account has been successfully created !")
else:
    print("Please enter the same password twice")

# the program is finish !