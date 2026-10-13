email = input("Enter email: ")
password = input("Enter password: ")

correct_email = "abc@gmail.com"
correct_password = "abc"

if email == correct_email and password == correct_password:
    print("User is logged in")
elif email == correct_email and password != correct_password:
    print("Password is not correct")
elif email != correct_email and password == correct_password:
    print("Enter the correct email")
else:
    print("Email and password are both incorrect")
