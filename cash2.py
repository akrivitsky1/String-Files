### constants for prices list and total amount
print("Cash register")
### asks for user to input a file name
file = input("Enter file of prices:")
try:
    amount = 0
    length = 0
    ##opens the file as read only
    open_file = open(file,"r")
    ### prints every line found in file
    for line in open_file:
        try: ## strips each line of the dollar sign and space
            prices = line.strip("/n")
            prices = prices.strip("$")
            prices = float(prices) ### converts the values to a float
            amount += prices ###adds the sum of numbers to variable
            length += 1 ###adds the numbers of items to the variable
        except:
            pass 
    ## convers value to 2nd decimal place
    amount = "{:.2f}".format(amount)
    ##print out results
    print("File contained",length,"items totaling","$"+str(amount))
    ## if file cant be found prints error
except:
    print("No file found")
 
