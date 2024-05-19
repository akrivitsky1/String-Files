while True:
    ### asks for user to input a file name
    file = input("Enter a file name to open:")
    ## trys to open the file as read only
    try:
        open_file = open(file,"r")
        break
    ## if file cant be found,asks user to re-enter filename
    except:
        print("Could not open",file)
        continue
    ### prints every line found in file
for line in open_file:
    print(line,end="")
