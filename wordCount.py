import sys        # command line arguments

# set input and output files
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

f = open(inputFile, "r")

# Read the file and replace all punctuation, split the words into an array and sort
words = f.read().lower().replace("-", " ").replace("_", " ").replace(".", " ").replace(",", " ").replace("/", " ")\
    .replace("!", " ").replace("?", " ").replace("'", " ").replace(":", " ").replace(";", " ").replace("(", " ")\
    .replace(")", " ").replace('"', " ").split()
words.sort()

# Keeps track of current element we are in and amount of times a word appeared
current = 0
amount = 0

# Stores the word and how many times it appeared
key = []

# Count the number of times each word appears
for i in range(0, len(words)):
    if words[current] != words[i]:
        key.append(words[current] + " " + str(amount))
        current = i
        amount = 0
    amount += 1
key.append(words[len(words)-1] + " " + str(words.count(words[len(words)-1])))
f.close()

# Create a new output file and store the output from above code
f = open(outputFile, "w")
for x in key:
    f.write(x + "\n")
f.close()
