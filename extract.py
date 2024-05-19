# asks user for a phoen number
lists = []
numbers = [1,2,3,4,5,6,7,8,9]
## Asks for input of a phone number
phone = input("Enter phone number: ")
### runs through users input and appends any intiger to the lists variable
for char in phone:
    if char.isdigit():
        lists.append(char)
## we take the index of each number in the list and assign it to the phoneNum variable as a string
phoneNum = lists[0] + lists[1] + lists[2] + lists[3] + lists[4] + lists[5] + lists[6]+ lists[7] + lists[8] + lists[9]
###prints only the numbers that were inputed by user
print("Numbers:", phoneNum)



