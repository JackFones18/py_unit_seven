# Jack Fones, Lars Leonard-Cook
# 12-14-2023
# This code mimics popular online typing games, such as https://play.typeracer.com/. It asks the user to type a given sentence and times them, telling them their accuracy and words per minute.
import time
import random

given_sentence = random.randint(0, 3)                                        # Chooses a random integer from 0-3, which is used to determine which sentence to give the user.
chosen_sentence = ["The quick brown fox jumps over the lazy dog.",
                   "Many people like many things, what do you like?",
                   "Formula one racing has grown in popularity over the years.",
                   "Over the years, many moons will shine."]                       # This is a database of the potential sentences a user will be asked to type.
sentence_to_type = chosen_sentence[given_sentence]                                 # This randomly chooses one of the 4 sentences.


def funtypy():
    """
    this entire function essentially just explains the code to the user, amd gives them a countdown to start.
    :return: none
    """
    print("This is a typing test. Please try to type the following sentence as quickly and as accurately as possible.")
    time.sleep(3)                           # idea to sleep came from https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
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


def start_timer():
    """
    This is a short funtion that just starts the timer.
    :return: none
    """
    global start_time                               # idea came from https://www.programiz.com/python-programming/global-keyword
    start_time = time.time()                        # starts the timer to record the duration it takes for the user to retype the sentence. All code relating to time came from https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html


def end_timer():
    """
    Stops the sentence timer and rounds the value to the nearst hundreds place.
    :return: none
    """
    global totaltime
    totaltime = round((time.time() - start_time), 2)        # This line finds the total time that has elapsed since the timer started, and rounds it to the nearest hundreds place.
    print("Time: " + str(totaltime), "seconds.")            # Prints the time elapsed since the start of the timer.


def find_accuracy():
    """
    Finds the accuracy of the sentence typed by the user in comparison
    to the sentence given by the computer.
    :return: Returns the sentence that the user typed.
    """
    global sentence_to_type
    user_type = input("Retype the sentence: ")                         # This is where the user will type the sentence.
    accuracy = 0                                                       # Sets the amount of errors to 0.
    for user_char, target_char in zip(user_type, sentence_to_type):    # This line came from ChatGPT
        if user_char == target_char:                                   # This line came from ChatGPT. It tests each character from both the generated sentence and the user's sentence to see if they match.
            accuracy += 1                                              # This line came from ChatGPT. It adds one error to a tally every the user's sentence doesn't match the target sentence.
    accuracy_percentage = (accuracy / len(sentence_to_type)) * 100     # This line calculates the accuracy of what the user typed relative to the given sentence,
    print("Accuracy:", round(accuracy_percentage, 2), "%")             # by dividing the amount of errors by the length of the sentence they typed.
    return user_type                                                   # The idea to return user_type came from ChatGPT


def wpm(totaltime, user_type):
    """
    Finds the words per minute of the sentences typed by the user.
    :param totaltime:
    :param user_type:
    :return: none
    """
    thing = len(user_type) / 5                                         # This line divides the total characters typed by the user by 5, representing the average length of a word.
    minutes = 60 / totaltime                                           # This line divides the total time it took the user by 1 minute, so that later we are able to calculate WPM.
    words_per_minute = round(thing * minutes, 2)                       # Calculates the words per minute based on the time taken by the user to type the sentence.
    print("Your WPM is:", words_per_minute)


def main():
    funtypy()
    start_timer()
    user_type = find_accuracy()
    end_timer()
    wpm(totaltime, user_type)


main()
