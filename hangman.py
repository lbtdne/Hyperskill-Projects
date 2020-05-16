import random  # We need choice()
import string  # We need ascii_lowercase()


def valid_guess(x):  # x is any string of any length
    global has_tried
    if not len(x) == 1:
        print("You should print a single letter")
        return True
    elif x not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        return True
    elif x in has_tried:
        print("You already typed this letter")
        return True
    else:
        return False


def list_letters():
    global answer_
    letters_ = set()
    for i in answer_:
        letters_.update(i)
    return letters_


def show_hyphens(x=""):
    global answer_
    global state_
    for i in range(len(state_)):
        if state_[i] == "-" and answer_[i] == x:
            state_[i] = x


def string_it(x):
    string_ = str()
    for i in range(len(x)):
        string_ = string_ + x[i]
    return string_


def guess_letter():
    global state_
    global answer_
    global game_end
    global has_tried
    n_guess = 0
    while n_guess < 8 and not game_end:
        if check_win():
            print("You guessed the word!")
            game_end = True
        else:
            guess_ = str(input("Input a letter:"))
            if valid_guess(guess_):
                pass
            elif guess_ in list_letters():
                show_hyphens(x=guess_)
                has_tried.update(guess_)
            else:
                print("No such letter in the word")
                n_guess += 1
                has_tried.update(guess_)
            if n_guess < 8:
                if not game_end:
                    print("\n" + string_it(state_))
    game_end = True


def check_win():
    global answer_
    global state_
    if string_it(state_) == answer_:
        return True
    else:
        return False


wordbank_ = "python", "java", "kotlin", "javascript"
answer_ = random.choice(wordbank_)
state_ = []
has_tried = set()
game_end = False


def reset():
    global answer_
    global state_
    global game_end
    answer_ = random.choice(wordbank_)
    state_ = []
    game_end = False
    has_tried.clear()


def hangman():
    global state_
    global wordbank_
    global answer_
    global game_end
    global has_tried
    print("H A N G M A N")
    quit_ = False
    while not quit_:
        go_ = str(input('Type "play" to play the game, "exit" to quit:'))
        if go_ == "exit":
            quit_ = True
        elif go_ == "play":
            reset()
            for every in range(len(answer_)):
                state_.append("-")
            print("\n" + string_it(state_))
            while not game_end:
                guess_letter()
            if check_win():
                print("You survived!")
            else:
                print("You are hanged!")
            print()
    exit()

hangman()
