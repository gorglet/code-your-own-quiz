#easy level
blanks = ["___1___", "___2___", "___3___", "___4___", "___5___", "___6___"]

para_easy = '''There are lots of Python symbols you need to remember before you start learning
Python.
Use + and - for addition and subtraction, as you would expect. For multiplication,
use ___1___. Use ___2___ for division. However, "=" doesn't work as you might expect.
Instead, = ___3___ a value to a variable.
Another use of the = sign is ___4___, which you can use to check if something is equal
to something else. You can also check if numbers or variables are greater than others,
by using ___5___, or less than others, by using ___6___.'''

answer_list_easy = ['*', '/', 'assigns', '==', '>', '<']


para_medium = '''When using the terminal to navigate through your files and directories, there
are some shortcuts you need to know. ___1___ changes the working directory. To create
a new file, type ___2___ and the filename you want to save it as. Don't forget the file
___3___! To make a new directory inside the current directory, type ___4___. And to remove
a file, type ___5___ and the filename. Again, make sure you use the ___3___!
If you forget which directory you're in, you can type ___6___ to print the working
directory.'''

answer_list_medium = ['cd', 'touch', 'extension', 'mkdir', 'rm', 'pwd']


para_hard = '''In the terminal, you can run scripts that you have written in a text editor. To do
this, you need to first locate to the parent directory. Then, type ___1___ and the filename.
You will then see anything that your script prints and can enter raw input if it prompts you to.

There are several things you can do with files inside the terminal. You need to enter the Python
interpreter by typing 'python' and hitting enter. To do anything with a file here, you first have to
open it. To do this, type ___2___ = open('filename'). Now you can do things with it!
To read the first line, type file.___3___(). This will return the first line of the file
in the terminal. To close the file, which you should always do when you're finished with it,
type file.___4___().

You can also ___5___ to the file. This overwrites what is already in the file.
However, you then have to open the file differently. Open it by typing: file = .open('filename', 'w'). This opens it in write mode, rather
than the default read mode (which you can go back to by opening with 'r' after filename!).
After opening in write mode, type file.write('your text here').
Another thing you can do in 'w' mode is empty the file. You need to type
file.___6___().'''

answer_list_hard = ['Python', 'file', 'readline', 'close', 'write', 'truncate']



print "This is a fill in the blanks game. Which level would you like to play? easy/medium/hard"
user_input = raw_input("> ")

def level_choice(user_input):
    #takes user input as input and returns the relevant level choice when typed correctly
    while user_input != None:
        if user_input == 'easy':
            play_game(para_easy, blanks, answer_list_easy)
        elif user_input == 'medium':
            play_game(para_medium, blanks, answer_list_medium)
        elif user_input == 'hard':
            play_game(para_hard, blanks, answer_list_hard)
        else:
            print "Sorry - I didn't get that. Try again. easy/medium/hard"
            user_input = raw_input("> ")

def word_in_blanks(word, blanks):
    #takes as input list of blanks and a word, checks the word to see if it matches
    #anything in the list of blanks, returns the blank.
    for blank in blanks:
        if blank in word:
            return blank


def play_game(blanks_para, blanks_list, answer_list):
    #takes as input a paragraph with blanks and the list of blanks
    #returns as output the paragraph with blanks or with user input
    #allows user 3 tries and then returns correct answer
    print blanks_para
    replaced = []
    blanks_para = blanks_para.split()

    for word in blanks_para:
        index = 0
        replacement = word_in_blanks(word, blanks_list)
        if replacement != None:
            correct_answer(blanks_para, answer_list)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print replaced
    return replaced


def correct_answer(blanks_para, answer_list):
    #takes the paragraph and the answer list as inputs, prompts user for response
    #for each blank, outputs 'correct' if it's right, prompts to try again if not
    blank = 0
    tries = 1
    max_tries = 3
    while blank < len(answer_list):
        user_input = raw_input("Type your answer for ___" + str(blank) + "___")
        if user_input == answer_list[blank]:
            print "Correct! Well done!"
            blank += 1
        elif tries < max_tries:
            tries += 1
            print "Nope. Try again"
        else:
            print "Out of tries! The correct answer is: " + answer_list[blank]
    return blanks_para





level_choice(user_input)
