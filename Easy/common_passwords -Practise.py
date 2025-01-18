common_passwords = [
    "123456",
    "password",
    "12345678",
    "qwerty",
    "12345",
    "123456789",
    "Football",
    "1234567",
    "princess",
    "1234"
]



#for i in range(len(common_passwords)):
 #   common_passwords[i]= common_passwords[i].lower()
    
common_passwords = [password.lower() for password in common_passwords]

def check_password(common_passwords, password):
    if password.lower() in common_passwords:
        return "password rejected"
    else:
        return "password accepted"

   
print(check_password(common_passwords,"football"))

