## boolean variable for checking the requirments of the passowrd
low_Case = False
up_Case = False
digit = False
special_C = False
## asks user for pasword
password = input("Enter password:")
##checks for the requirments through a for loop
for check in password:
    if check.islower():
        low_Case = True
    if check.isupper():
        up_Case = True
    if check.isdigit():
        digit = True
    if check in "@#$*!":
        special_C = True
## prints whatever check passed and occured in the password    
print("Length:",len(password)) ### prints length of input
if low_Case == True:
    print("Has lower case") 
if up_Case == True:
    print("Has upper case")
if digit == True:
    print("Has digit")
if special_C == True:
    print("Has special")
