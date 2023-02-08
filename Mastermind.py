"""
CISC 204 Modelling Project 
Group 6: Shauna Tunistra, Fiona LeClair-Robertson, Aniket Mukherjee, 
The following program models a game of mastermind, and determines the number of solutions possible given a 
game configuration and a guess. 
"""

#importing necesarry libraries
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
import random

#setting up appropriate game environmnet
NUM_GUESSES = 2
NUM_PEGS = 4
NUM_COLOURS = 4

#Setting default state of solved code to false. 
solved = False

#Creating storage for appropriate game variablles
code = []
bauhaus_code = []
guesses = []
guesses_input = []
good_pegs = []
correct_guesses = []
purple_pegs = []
purple_matches = []
white_pegs = []
white_peg_colours = []

#setting the options for colour choice to either red, green, blue, or yellow. 
colchoice = ["R", "G", "B", "Y"]


# Encoding that will stores all of our model constraints.
E = Encoding()


class Guess:
    """
    The following class creates/defines the proposition for a player's guess in the game. 
    """

    def __init__(self, guess_num=0):
        self.guess_num = guess_num
        self.pegs = []
        self.peg_matches = []
        


@proposition(E)
class GuessRedPeg:
    """
    The following class creates/defines the proposition for a red peg guess in our model. Keeps 
    track of guess number and position.
    """

    def __init__(self, guess_num, pos):
        self.guess_num = guess_num
        self.pos = pos

    def __repr__(self):
        return f"G{self.guess_num}R{self.pos}"


@proposition(E)
class GuessBluePeg:
    """
    The following class creates/defines the proposition for a blue peg guess in our model. Keeps 
    track of guess number and position.
    """

    def __init__(self, guess_num, pos):
        self.guess_num = guess_num
        self.pos = pos

    def __repr__(self):
        return f"G{self.guess_num}B{self.pos}"


@proposition(E)
class GuessYellowPeg:
    """
    The following class creates/defines the proposition for a yellow peg guess in our model. Keeps 
    track of guess number and position.
    """

    def __init__(self, guess_num, pos):
        self.guess_num = guess_num
        self.pos = pos

    def __repr__(self):
        return f"G{self.guess_num}Y{self.pos}"


@proposition(E)
class GuessGreenPeg:
    """
    The following class creates/defines the proposition for a green peg guess in our model. Keeps 
    track of guess number and position.
    """

    def __init__(self, guess_num, pos):
        self.guess_num = guess_num
        self.pos = pos

    def __repr__(self):
        return f"G{self.guess_num}G{self.pos}"


@proposition(E)
class CodeRedPeg:
    """
    The following class creates/defines the proposition for a red peg located in the secret 
    code for our model. Only keeps track of position in code. 
    """

    def __init__(self, pos):
        self.pos = pos

    def __repr__(self):
        return f"CR{self.pos}"


@proposition(E)
class CodeBluePeg:
    """
    The following class creates/defines the proposition for a blue peg located in the secret 
    code for our model. Only keeps track of position in code. 
    """

    def __init__(self, pos):
        self.pos = pos

    def __repr__(self):
        return f"CB{self.pos}"


@proposition(E)
class CodeYellowPeg:
    """
    The following class creates/defines the proposition for a yellow peg located in the secret 
    code for our model. Only keeps track of position in code. 
    """

    def __init__(self, pos):
        self.pos = pos

    def __repr__(self):
        return f"CY{self.pos}"


@proposition(E)
class CodeGreenPeg:
    """
    The following class creates/defines the proposition for a green peg located in the secret 
    code for our model. Only keeps track of position in code. 
    """

    def __init__(self, pos):
        self.pos = pos

    def __repr__(self):
        return f"CG{self.pos}"


@proposition(E)
class CorrectGuess:
    """
    The following class creates/defines the proposition for a correct guess corresponding to a peg in
    our secret code for our model. Keeps track of guess number (which guess was correct)
    """
    
    def __init__(self, guess_num):
        self.guess_num = guess_num

    def __repr__(self):
        return f"CG{self.guess_num}"


@proposition(E)
class PurplePeg:
    """
    The following class creates/defines the proposition for a purple peg which implies a peg is both the correct
    colour and in the correct position of the corresponding secret code. Keeps track of guess number and 
    appropriate peg number in code. 
    """

    def __init__(self, guess_num, peg_num):
        self.guess_num = guess_num
        self.peg = peg_num

    def __repr__(self):
        return f"G{self.guess_num}P{self.peg}"


@proposition(E)
class WhitePeg:
    """
    The following class creates/defines the proposition for a purple peg which implies a peg satisfies either the correct
    spot or correct colour in the secret code for our model. Keeps track of guess number and appropriate position.
    """

    def __init__(self, pos, guess_num):
        self.pos = pos
        self.guess_num = guess_num

    def __repr__(self):
        return f"G{self.guess_num}W{self.pos}"


def ask_for_guess():
    """
    The following function prompts the user for their guess input
    """

    # Will be used to store user guess
    guess = []
    
    i = 0
    #For length of pegs in code
    while i < NUM_PEGS:
        #Prompts user for input. 
        peg_colour = input("Enter peg colour: ")
        
        #Checks for valid input.
        if peg_colour.upper() in colchoice:
            guess.append(peg_colour.upper())
            i += 1
        #Prompts for valid input. 
        else:
            print("Not a colour option, try again")
    #Saves user guess. 
    guesses_input.append(guess)


def create_guess_bauhaus(i):
    """
    The following function will create a guess using peg constraints.
    """

    guess = guesses_input[i]
    bauhaus_guess = Guess()

    for j in range(NUM_PEGS):
        peg_vals = [GuessRedPeg(i, j), GuessBluePeg(i, j), GuessGreenPeg(i, j), GuessYellowPeg(i, j)]
        
        #If red is selected for a spot, no other colour can occupy that same spot. 
        if guess[j] == 'R':
            E.add_constraint(peg_vals[0])
            E.add_constraint(~peg_vals[1])
            E.add_constraint(~peg_vals[2])
            E.add_constraint(~peg_vals[3])

        #If blue is selected for a spot, no other colour can occupy that same spot. 
        elif guess[j] == 'B':
            E.add_constraint(peg_vals[1])
            E.add_constraint(~peg_vals[0])
            E.add_constraint(~peg_vals[2])
            E.add_constraint(~peg_vals[3])
        
        #If green is selected for a spot, no other colour can occupy that same spot. 
        elif guess[j] == 'G':
            E.add_constraint(peg_vals[2])
            E.add_constraint(~peg_vals[0])
            E.add_constraint(~peg_vals[1])
            E.add_constraint(~peg_vals[3])

        #If yellow is selected for a spot, no other colour can occupy that same spot. 
        elif guess[j] == 'Y':
            E.add_constraint(peg_vals[3])
            E.add_constraint(~peg_vals[0])
            E.add_constraint(~peg_vals[1])
            E.add_constraint(~peg_vals[2])

        #Storing created guesses. 
        bauhaus_guess.pegs.append(peg_vals)
        
    guesses.append(bauhaus_guess) 


def give_purple_pegs(i):
    """
    The following function determines whether a purple peg (correct spot, correct colour)
    should be given for a peg in the guess. 
    """

    exclude_from_white_pegs = []

    guess = guesses[i]
    input_guess = guesses_input[i]

    for j in range(NUM_PEGS):
        purple_peg = PurplePeg(i, j)
        #If the guess matches the code
        if input_guess[j] == code[j]:
            r = guess.pegs[j][0]
            b = guess.pegs[j][1]
            g = guess.pegs[j][2]
            y = guess.pegs[j][3]
            c_r = bauhaus_code[j][0]
            c_b = bauhaus_code[j][1]
            c_g = bauhaus_code[j][2]
            c_y = bauhaus_code[j][3]

            #Give a purple peg
            E.add_constraint(purple_peg)
            #Which implies that code at red and guess red match, or code at blue and guess blue match, or code at green and guess green match or code at yellow and 
            #guess yellow match
            #No other colour than the one pairing per or statement can be true. 
            E.add_constraint(purple_peg >> ((c_r & r & ~b & ~g & ~y) | (c_b & b & ~r & ~g & ~y) | (c_g & g & ~b & ~r & ~y) | (c_y & y & ~b & ~g & ~r)))
            
            # Adding 1 when printing for ease of reading, so that the output is not zero-based like the arrays
            print(f"Guess {i + 1} Peg {j + 1} is the correct colour and in the correct position!")
            exclude_from_white_pegs.append(j)

        #Determined that no purple peg should be given 
        else:
            E.add_constraint(~purple_peg)
    return exclude_from_white_pegs


def give_white_pegs(guess_num, exclude):
    """
    The following function determines whether a white peg (either right colour or right position)
    should be given for a peg in the guess. 
    """
    # Only one white peg per colour
    guess = guesses_input[guess_num]

    for i in range(NUM_PEGS):
        peg = guess[i]
        white_peg = WhitePeg(i, guess_num)
        
        for j in range(NUM_PEGS):
            if peg == code[j]:
                if (i != j) and (i not in exclude):
                    print(f"Guess {guess_num + 1} peg {i + 1} is the correct colour but in the wrong position!")
                    E.add_constraint(white_peg)
                    idx = get_colour_idx(peg)
                    E.add_constraint(~bauhaus_code[i][idx])
                    other_pegs = []
                    for k in range(NUM_PEGS):
                        if k != i:
                            other_pegs.append(bauhaus_code[k][idx])
                    constraint.add_at_least_one(E, *(other_pegs))
                    return


def get_colour_idx(colour):
    """
    The following function will return the colour of peg.
    """
    col_idx = 0
    if colour == 'R':
        col_idx = 0
    elif colour == 'B':
        col_idx = 1
    elif colour == 'G':
        col_idx = 2
    elif colour == 'Y':
        col_idx = 3
    return col_idx


def guess_matches(guess_num):
    """
    The following function determines if a peg in guess matches a corresponding peg in code. 
    """
    guess = guesses[guess_num]
    for peg in range(NUM_PEGS):
        for colour in range(NUM_COLOURS):
            E.add_constraint(guess.pegs[peg][colour] >> bauhaus_code[peg][colour])


def peg_incorrect(guess_num, peg_num):
    """
    The following function determines if a peg does not match corresponding peg in code. 
    """
    colour = guesses_input[guess_num][peg_num]

    if colour == 'R':
        E.add_constraint(~bauhaus_code[peg_num][0])
    elif colour == 'B':
        E.add_constraint(~bauhaus_code[peg_num][1])
    elif colour == 'G':
        E.add_constraint(~bauhaus_code[peg_num][2])
    else:
        E.add_constraint(~bauhaus_code[peg_num][3])


def check_if_solved(i):
    """
    The following function determines whether the secret code has been cracked!
    """
    guess = guesses_input[i]
    #Default state is true
    flag = True
    for j in range(NUM_PEGS):
        #If a discrepancy is found between peg in code and peg in guess
        if code[j] != guess[j]:
            #state is then set to false
            flag = False
    return flag


def generate_code():
    """
    The following function creates a random code corresponding to 
    game configurations set at beginning (ie colour choices, code length).
    """
    for i in range(NUM_PEGS):
        colour = random.randint(0, NUM_COLOURS - 1)
        code.append(colchoice[colour])


def example_theory():
   

    # peg definition order: [RED VALUE, BLUE VALUE, GREEN VALUE, YELLOW VALUE]

    generate_code()
    print(code)

    for j in range(NUM_PEGS):
        bauhaus_code.append([CodeRedPeg(j), CodeBluePeg(j), CodeGreenPeg(j), CodeYellowPeg(j)])
        constraint.add_exactly_one(E, *(bauhaus_code[j]))

    i = 0
    while i < NUM_GUESSES:
    #For the length of the code
        print(F"GUESS {i + 1}")
        #Gather guess information
        ask_for_guess()
        #Compile guess information
        create_guess_bauhaus(i)
        #If user has cracked code return true
        if check_if_solved(i):
            print("That's the code!!")
            solved = True
            guess_matches(i)
            break
        exclude = give_purple_pegs(i)
        give_white_pegs(i, exclude)
        print()
        i += 1

    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    #E.introspect()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    sol = T.solve()
    # print("   Solution: %s" % sol)

    print()
    #If there exists a solution print corresponding colours
    if count_solutions(T) != 0:
        print("GUESS COLOURS")
        for guess in range(len(guesses)):
            print()
            print(f"GUESS {guess}")
            for peg in range(len(guesses[0].pegs)):
                if sol[guesses[guess].pegs[peg][0]]:
                    print(f"Peg {peg + 1} is RED")
                elif sol[guesses[guess].pegs[peg][1]]:
                    print(f"Peg {peg + 1} is BLUE")
                elif sol[guesses[guess].pegs[peg][2]]:
                    print(f"Peg {peg + 1} is GREEN")
                else:
                    print(f"Peg {peg + 1} is YELLOW")
        print()
        print("CODE COLOURS")

        for peg in range(len(code)):
            print(f"PEG {peg + 1} Colour Likelihoods")
            print(" %s: %.2f" % ("RED", likelihood(T, bauhaus_code[peg][0])))
            print(" %s: %.2f" % ("BLUE", likelihood(T, bauhaus_code[peg][1])))
            print(" %s: %.2f" % ("GREEN", likelihood(T, bauhaus_code[peg][2])))
            print(" %s: %.2f" % ("YELLOW", likelihood(T, bauhaus_code[peg][3])))

    print()
    print(f"ACTUAL GENERATED CODE: {code}")
    print()
    if not solved:
        #If there is only one solution, our player can guess the solution logically in the next guess
        if count_solutions(T) == 1:
            print("The code can be determined in the next guess.")
        #Should there be more than one solution, it is not possible for our player to logically guess the correct solution
        #without the factor of luck, as it is not 100% definitive they would guess the correct answer. 
        elif count_solutions(T) > 1:
            print("This guess will most likely require more than one additional guess to determine.")