import time
import random
given_sentence = random.randint(0,3)
chosen_sentence = ["The quick brown fox jumps over the lazy dog.",
                   "Many people like many things, what do you like?",
                   "Formula one racing has grown in popularity over the years.",
                   "Over the years, many moons will shine."]
sentence_to_type = chosen_sentence[given_sentence]

def funtypy():
    print("This is a typing test. Please try to type the following sentence as quickly and as accurately as possible.")
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

def find_accuracy():
    global user_type
    user_type = input("Retype the sentence: ")
    accuracy = 0
    for user_char, target_char in zip(user_type, sentence_to_type):
        if user_char == target_char:
            accuracy += 1
    accuracy_percentage = (accuracy / len(sentence_to_type)) * 100
    print("Accuracy:", round(accuracy_percentage,2), "%")


def wpm():
    thing = len(user_type)/5
    print ("Your WPM is:", thing)

def main():
    funtypy()
    starttime = time.time()

    find_accuracy()
    wpm()
    global totaltime
    totaltime = round((time.time() - starttime), 2)
    print("Time: " + str(totaltime), "seconds.")
main()
