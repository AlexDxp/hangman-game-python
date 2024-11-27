import random

fp = open("Words","r")
listofwords = fp.read().split()
randomchoice = random.choice(listofwords)
while True:
    players = input("Would you like to pick a word for your friend to pick?").lower()
    if players == "yes":
        randomchoice = input("What word")
        print("""
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x
        x""")
        length = len(randomchoice)
        word = list(randomchoice)
        leng = ("_" * length)
        listleng = list(leng)
        lives = 10
        break
    elif players == "no":
            while True:
                try:
                    wordlength = int(input("How long would you like your word to be? (3 - 21) or (0 for a random)"))
                except ValueError:
                    print("Please enter a number.")
                else:
                    if 3 <= wordlength < 22:
                        break
                    else:
                        print("Invalid range")

            while True:
                length = len(randomchoice)
                word = list(randomchoice)
                leng = ("_" * length)
                listleng = list(leng)
                lives = 10
                if wordlength == length:
                    break
                elif wordlength == 0:
                    break
                elif wordlength != length:
                    for i in range(100):
                        if i == wordlength and i != length:
                            randomchoice = random.choice(listofwords)

            break
    else:
        print("Invalid input (yes or no)")
step1 = """

|
|
|
|
|
| """

step2 = """
 ___________
|
|
|
|
|
| """

step3 = """
 ___________
|          |
|          |
|
|
|
| """

step4 = """
 ___________
|          |
|          |
|          O
|
|
| """

step5 = """  
 __________
|          |
|          |
|          O
|          |
|
| """

step6 = """ 
 __________
|          |
|          |
|          O
|          |
|         |
| """

step7 = """ 
 __________
|          |
|          |
|          O
|          |
|         | |
| """

step8 = """
 __________
|          |
|          |
|          O
|         -|
|         | |
| """

step9 = """ 
 __________
|          |
|          |
|          O
|         -|-
|         | |
| """

step10 = """ 
 __________
|          |
|          |
|          0
|         -|-
|         | |
| """
steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9, step10]
step = -1
wrong = []
while True:
    print("Your incorrect guesses are:",' '.join(wrong))
    print(' '.join(listleng))
    letter = input("Guess a letter: ")
    if letter in randomchoice:
        for i in range(length):
            if word[i] == letter:
                listleng[i] = letter
    elif letter not in randomchoice:
        lives -= 1
        step += 1
        wrong.append(letter)
        print(steps[step])
        if lives == 0:
            print("You lose!")
            print("The word was", randomchoice)
            break
    if listleng == word:
        print(randomchoice)
        print("You win!")
        print("You had",lives,"lives remaining")
        break