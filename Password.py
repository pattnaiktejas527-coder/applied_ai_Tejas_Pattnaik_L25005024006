#Password
create_password= int(input(" Enter a password : "))
confirm_password = int(input(" Enter confirm password : "))
if(create_password==confirm_password):
    print("Correct password")
else:
    print("Incorrect password")