#
#Python 3.6.4
#
#author: James Hannafin
#
#Purpose: Have fun
#
#



def start (nice = 0, mean = 0, name = ""):
    #Get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is nt a new game, thanl the player
        for playing the again and continue with the game,
    """
    #meaning, if we do not already have this user's game,
    #then they are a new player and we need to get their name
    if name != "":
        print("\nThankyou for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nConversation. Will you be nice \nor mean? (N/M) \n>>>: ")
        if pick == "n":
            print("\nThe stranger was happy to meet you...")
            nice = (nice + 1)
            stop = False
        elif pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off..")
            mean = (mean + 1)
            stop = False
        else:
            print ("\Please type 'y' or 'n'")
            nice_mean(nice,mean,name)
            
        score(nice,mean,name) #pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}\n, Mean)".format(name,nice,mean))
                    

def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variavles
    if nice > 2: #if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call los function passing in the variables so it can use them
        lose(nice,mean,name)
    else:
        #else,call nice_mean function passing in the vars
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nAhh too bad, game over! \nYou live in a dirty beat-up  \nvan by the river, wretched and alone!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( y ) for 'YES', ( N ) for 'NO':\n>>> ")  
    
def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice, I do not reset the name variable as that same user has slectecd to play again
    start(nice,mean,name)

if __name__ == "__main__":
    start()
