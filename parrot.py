## continous loop until it is broken by a command word
while True:
    repeat_input = input(">") ##asks the user to input something
    repeat_input = repeat_input.lower()### makes the input all lowercase
    if "hush" in repeat_input: ## is now able to compare the input for the word hush
        break ## if the word hush is found regardless of capitlization loop is broken
    else:
        print(repeat_input.upper()) ## prints what the user inputed but with everythigng capitlized
