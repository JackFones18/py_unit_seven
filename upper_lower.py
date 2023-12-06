word = ("jack")

half = int(round((len(word) / 2), 0))

length = int(len(word))
firsthalf = word[0:half]

secondhalf = str(word[half:length])

print(secondhalf + firsthalf)
