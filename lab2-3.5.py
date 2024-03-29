import random
history = []

qualifiers = ['Why do you say that ', 'You seem to think that ', 'Did I just hear you say that ',
              'Why did you believe that ']

replacement = {'i': 'you', 'me': 'you', 'my': 'your', 'we': 'you', 'us': 'you', 'am': 'are',
               'you': 'i', 'you': 'I'}

hedges = ['Go on. ', 'I would like to hear more about that. ', 'And what do you think about this? ', 'Please Continue ']

def reply(sentence):
    """Implements three different reply strategies."""
    probability = random.randint(1,5)
    if probability in (1,2):
        #Just hedge
        answer = random.choice(hedges)
    elif probability == 3 and len(history) > 3:
        #Go back to an early topic
        answer = "Earlier you said that " + \
            changePerson(random.choice(history))
    else:
        #Transform the current input
        answer = random.choice(qualifiers) + changePerson(sentence)
    #Always add the currnt sentence to the history list
    history.append(sentence)
    return answer

def changePerson(sentence):
    """Replaces first person pronounce with second person pronounce."""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacement.get(word, word))
    return "".join(replyWords)

def main():
    """Handles the interaction between patient and doctor. """
    print("Goodmorning, I hope you are well today. ")
    print("What can I do for you? ")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day! ")
            break
        print(reply(sentence))

# The Entry point for program execution
if __name__ == "__main__":
    main()