import time
import random
given_sentence = random.randint(0,3)
chosen_sentence = ["hello", "rahh", "bruh", "ahhh"]
sentence_to_type = chosen_sentence[given_sentence]

def funtypy():
    print("This is a typing test. please try to type the following sentence as quickly and as accurately as possible.")
    time.sleep(3)
    print("")
    print("the sentence is:")
    print("")
    time.sleep(2)
    print(sentence_to_type)
    print("")
    print("The timer starts in:")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")
    print(sentence_to_type)

user_type = input("retype that nerd: ")


if user_type == "Hello":
    print("yup")
else:
    print("no")


def main():
    funtypy()
    starttime = time.time()
    totaltime = round((time.time() - starttime), 2)
    print("Total Time: " + str(totaltime))

main()
