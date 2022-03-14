import random
data = open("words.txt")
lines = data.readlines()
data.close()

def play(word_len, guesses):
    filtered = list(map(lambda s: s.rstrip('\n'), lines))
    filtered = list(map(lambda s: s.lower(), filtered))
    filtered = list(filter(lambda x: len(x) == word_len and all(y.lower() in "abcdefghijklmnopqrstuvwxyz" for y in x), filtered))
    target = random.choice(filtered)
    cur_guesses = 0
    while cur_guesses < guesses:
        word = str(input("Guess a %d letter word\n" % word_len))
        if len(word) != word_len or not all (y in "abcdefghijklmnopqrstuvwxyz" for y in word):
            print("invalid guess")
        else:
            cur_guesses += 1
            if word == target:
                print("You got it!")
                return
            else:
                for i in range(len(word)):
                    print('Letter %d:' % (i+1))
                    if word[i] == target[i]:
                        print("Letter %s is in the word at this position" % word[i])
                    elif word[i] in target:
                        print("Letter %s is in the word but not in this position" % word[i])
                    else:
                        print("Letter %s is not in the word" % word[i])
                    print('\n')
    print("The answer was %s" % target)
    

