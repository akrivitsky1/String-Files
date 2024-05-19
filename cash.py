### constants for prices list and total amount
amount = 0
prices = []

print("Cash register")
### asks for user to input a file name
file = input("Enter file of prices:")
##opens the file as read only
open_file = open(file,"r")
### prints every line found in file
for line in open_file:
    prices.append(float(line)) ### adds the numbers found in the text to the prices list
    amount = amount + float(line) ###adds the numbers in the list together

open_file.close() ###closes file
### takes length of list 
length = len(prices)
## convers value to 2nd decimal place
amount = "{:.2f}".format(amount)
##print out results
print("File contained",length,"items totaling","$"+str(amount))

 
