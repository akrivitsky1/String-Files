# validate_phone.py
# Validate a phone is specified in the form ###-###-#### 
phone = input("Enter number as  ###-###-####:")        
valid = len(phone) == 12 ## compared input to total amount of characters
pos = 0 
while valid and pos < 12: ### loops through each digit breaks out when it reaches character 12
    ## checks for requirments to be valid
    if pos == 3: 
        valid = phone[pos] == "-"
    elif pos == 7:
        valid = phone[pos] == "-"
    else:
        valid = phone[pos].isdigit()
    pos = pos + 1

if valid:
    print("Valid")
else:
    print("Invalid")
