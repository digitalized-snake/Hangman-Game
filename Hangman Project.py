import random

wordbank = ['bikes','skate','spurious','thankful','division','better','waste','fairies','apple','indulge','parched','education','lean','cannon','discussion','waste','dynamic','familiar','tail','needle','deer','polish','design','pale','grouchy','imaginary','mine','word','station','possessive','collect','cherries','airport','secret','invite','curb','jail','shape','narrow','calm','complete','install','argument','damp','size','develop','trouble','sophisticated','chin','snatch','hard','thoughtless','feather','idealize','shaggy','scrawny','awesome','vigorous','thrill','parched','potato','unable','jump','immolate','teeth','prepare','convict','hook','oatmeal','wren','suggestion','dogs','pointless','hellish','sore','glitter','stitch','purify','rebel','ring','']
# get user input and check that input is valid.

def getInput():
    d = input("Enter your guess: ")
    if d.isalpha() == False or len(d) > 1:
        print("Enter a letter dummy!")
        d = input("Enter your guess: ")
    return d


def update_word(letter, output_word):
    for j in range(0, len(random_word)):
        if letter == random_word[j]:
            output_word[j] = letter


def print_word(output_word):
    for i in range(0, len(output_word)):
        print(output_word[i], end = ' ')
    print()
            
        

guessman1 = "__________\n|         |\n|         |\n|          \n|          \n|          \n|\n|\n|\n|\n|\n|\n|\n|___________"
guessman2 = """
__________
|         |
|       __|__
|       |   |
|       |___|
|
|
|
|
|
|
|
|
|________

"""
guessman3 = """
__________
|         |
|       __|__
|       |   |
|       |___|
|         |
|         |
|         |
|         |
|         |
|
|
|
|________

"""
guessman4 = """
__________
|         |
|       __|__
|       |   |
|       |___|
|         |  
|        /|\\
|       / | \\
|         |
|         |
|
|
|
|________

"""
guessman5 = """
__________
|         |
|       __|__
|       |   |
|       |___|
|         |  
|        /|\\
|       / | \\
|         |
|        / \\
|       /   \\
|
|
|________

"""

guessmans = [guessman1, guessman2, guessman3, guessman4, guessman5]
# Pick a random word
r = random.randint(0,len(wordbank))
for i in range(0,len(wordbank)):
    random_word = wordbank[r]

output_word = []
guess_wrong = 0

for k in range(0, len(random_word)):
    output_word.append("_")   

while guess_wrong < 4 and "_" in output_word: #Repeat till hangman built or word guessed completely.
    print(guessmans[guess_wrong])
    # print guessed word
        
    # get letter input
    letter = getInput()

    # If right update word
    if letter in random_word:
        update_word(letter, output_word)
    else:
        guess_wrong += 1
        
    print_word(output_word)
            
        # Hangman = altered hangman

if "_" not in output_word: 
    print("You Won!")
else: 
    print(guessman5, "\nYou Lost!\n","The word was:",random_word)
