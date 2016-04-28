import xmlrpclib

server = xmlrpclib.ServerProxy('http://localhost:8000')


# Print Writer
def clientOptions():
    return 'GMN - Start The Guessing Game \n' \
           'EXT - Exit the Program '

isGamingActive = False

# Client Code
while True:
 try:
    global isGamingActive
    if isGamingActive:
        print server.options()
        gamingChoice = raw_input("Please enter your choice: \n")
        if str(gamingChoice) == "1":
            guessedNumber = raw_input("Please enter your guess: \n")
            result=server.guess(guessedNumber)
            resultBoolean=result["resultBoolean"]
            resultText=result["resultText"]
            if resultBoolean == True :
               isGamingActive=False
            print  str(resultText)

        elif gamingChoice == "2":
            print server.exit()
            isGamingActive = False
        else:
            print("Invalid choice please try again!")

    else:
        global isGamingActive
        print clientOptions()
        clientChoice = raw_input("Please enter your choice: \n")
        if clientChoice == 'EXT':
            print("Good Bye!")
            isGamingActive = False
            break;
        elif clientChoice == 'GMN':
            result= server.startGame()
            if result["resultBoolean"]==True:
             isGamingActive = True
            print result["resultText"]
        else:
            print("Invalid choice please try again!")
 except xmlrpclib.Fault as err:
    print "A fault occurred"
    print "Fault code: %d" % err.faultCode
    print "Fault string: %s" % err.faultString
