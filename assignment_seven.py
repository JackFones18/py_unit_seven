import time


given_sentence = "Hello"
print(given_sentence)
print("")
starttime = time.time()

character_split = list(given_sentence.split())
print(len(character_split))
user_type = input("retype that nerd: ")


if user_type == "Hello":
    print("yup")
else:
    print("no")

'''
# Timer starts
def is_duplicates(user_type):

    for x in range(len(user_type)):                             # This line creates the outer loop. "x" will take on each variable in the list every time it goes through the loop.
        for y in range(x + 1,len(given_sentence)):                   # This line creates the nested loop. the variable "y" will take on each variable except for the one that is assigned to x, so that the numbers are not compared to themselves.
            if user_type[x] == given_sentence[y]:                    # Tests to see if the two variables, which each have a birthday assigned to them, are equal.
                return True
    return False
duplicate_count = 0
for z in range(1):                                                   # This creates another loop that will run the amount of times the user entered. this loop is where all the code is called basically                                                    # Assigns the list to the variable birthdays.
    if is_duplicates(user_type):                                                    # If is_duplicates returned true, the code will add one to the tally of duplicates.
        duplicate_count += 1
print(duplicate_count)
'''
totaltime = round((time.time() - starttime), 2)

print("Total Time: " + str(totaltime))
