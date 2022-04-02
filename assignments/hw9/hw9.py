from random import randint
from graphics import *
def get_words(file_name):
    infile=open(file_name,"r")
    read_file=infile.readlines()
    return read_file


def get_random_word(words):
    r=randint(0,len(words)-1)
    return words[r]


def letter_in_secret_word(letter, secret_word):
    for i in range(0,len(secret_word)):
        if(secret_word[i]==letter):
            return True
        return False


def already_guessed(letter, guesses):
    for i in range(0,len(guesses)):
        if (guesses[i]== letter):
            return True
        return False


def make_hidden_secret(secret_word, guesses):
    secret=""
    for i in range(0,len(secret_word)-1):
        secret=secret+"_"
        for j in range(0,len(guesses)):
            for k in range (0,len(secret_word)):
                if (secret_word[k] == guesses[j]):
                    secret=secret[:k*2]+ secret_word[k]+ secret[k*2+1:]
    return secret


def won(guessed):
    if "_" in guessed:
        return False
    else:
        return True


def play_graphics(secret_word):
    win=GraphWin("Hangman", 600,700)
    win.setBackground("white")
    l1=Line(Point(300,125),Point(300,400))
    l2=Line(Point(300,125), Point(150,125))
    l3=Line(Point(150,125),Point(150,200))
    l4=Line(Point(150,400),Point(300,400))
    l1.draw(win),l2.draw(win),l3.draw(win),l4.draw(win)

    figure=[]
    head=Circle(Point(130,200),25)
    body=Line(Point(150,240), Point(150,440))
    armL=Line(Point(150,250), Point(100,220))
    armR=Line(Point(150,250),Point(200,220))
    legL=Line(Point(150,440),Point(100,520))
    legR=Line(Point(150,440),Point(200,520))
    figure.append(head),figure.append(body), figure.append(armL),figure.append(armR),figure.append(legL),
    figure.append(legR)

    inputBox=Entry(Point(300,600),6)
    inputBox.draw(win)
    instructions= Text(Point(215,600),"Guess a letter:")
    instructions.draw(win)

    numofGuesses=6
    guesses=[]
    while numofGuesses !=0 and won(make_hidden_secret(secret_word, guesses))== False:
        bound=Text(Point(450,90), "Already guessed: {}".format(guesses))
        restr=Text(Point(140,500),"Guesses Remaining:{}".format(numofGuesses))
        output=make_hidden_secret(secret_word, guesses)
        res= Text(Point(300,475),output)
        bound.draw(win),restr.draw(win), res.draw(win)

        newLetter=win.getKey()
        if already_guessed(newLetter,guesses)==False:
            guesses.append(newLetter)
        else:
            r=Text(Point(300,500), "Letter already guessed, enter another letter")
            r.draw(win)
            inputBox.setText("")
            newLetter=win.getKey()
            r.undraw()
            guesses.append(newLetter)
        if letter_in_secret_word(newLetter,secret_word)==False:
            figure[0].draw(win)
            figure.pop(0)
            numofGuesses=-1
            inputBox.setText("")
        else:
            inputBox.setText("")
        bound.undraw(),restr.undraw(),res.undraw()
    final= Text(Point(300,450),"")
    sec=Text(Point(325,465),"")
    if won(make_hidden_secret(secret_word, guesses))==True:
        final.setText("Winner!")
        sec.setText(secret_word)
    elif won(make_hidden_secret(secret_word, guesses))==False or numofGuesses== False:
        final.setText("Sorry.You did not get the word correctly")
        sec.setText("The secret word is '{}'".format(secret_word))
    inputBox.undraw()
    instructions.undraw()
    final.draw(win)
    sec.draw(win)

    win.getMouse()
    win.close()

def play_command_line(secret_word):
    numofGuesses=6
    guesses=[]
    while numofGuesses !=0 and won(make_hidden_secret(secret_word, guesses)) == False:
        print("Already guessed:{}".format(guesses))
        print("Guesses remaining:{}".format(numofGuesses))
        print(make_hidden_secret(secret_word, guesses))
        newLetter=input("Guess a letter:")

        if already_guessed(newLetter,guesses)==False:
            guesses.append(newLetter)
        else:
            newLetter=input("Letter already guessed, enter another letter.")
            guesses.append(newLetter)
        if letter_in_secret_word(newLetter,secret_word)==False:
            numofGuesses -= 1
            print()
        else:
            print()
            continue
    if won(make_hidden_secret(secret_word, guesses)) == True:
        print("winner!")
        print(secret_word)
    else:
        print("You did not guess the secret word correctly.")
        print("The secret word is '{}'".format(secret_word))

if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
