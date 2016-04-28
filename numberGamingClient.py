import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8000')


# Print Writer
def clientOptions():
    return 'GMN - Start The Guessing Game \n' \
           'EXT - Exit the Program '

isGamingActive = False

# Client Code
while True:
    global isGamingActive
    if isGamingActive:
        print server.options()
        gamingChoice = raw_input(" \n" + "Please enter your choice: ")
        if str(gamingChoice) == "1":
            guessedNumber = raw_input(" \n" + "Please enter your guess: ")
            server.guess(guessedNumber)
        elif gamingChoice == "2":
            print server.exit()
            isGamingActive = False
        else:
            print("Invalid choice please try again!")

    else:
        global isGamingActive
        print clientOptions()
        clientChoice = raw_input("Please enter your choice: ")
        if clientChoice == 'EXT':
            print("Good Bye!")
            isGamingActive = False
            break;
        elif clientChoice == 'GMN':
            print server.startGame()
            isGamingActive = True
        else:
            print("Invalid choice please try again!")
