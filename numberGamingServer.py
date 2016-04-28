from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

actualNumber = 0
gameIsActive = False
def guess(guessedNumber):
    if not checkIsNumber(guessedNumber):
        return 'You must input an integer'
    elif guessedNumber > actualNumber:
        return 'Smaller than this'
    elif guessedNumber < actualNumber:
        return 'Bigger than this'
    else:
        exit()
        return 'You win'
    return


def exit():
    global actualNumber,gameIsActive
    actualNumber = 0
    gameIsActive=False
    return 'Good Bye'

def createRandomVar():
    return random.randint(0, 100)

def checkIsNumber(x):
    if type(x) is not int :
        return False
    else:
        return True

def options():
    return 'STR - Start  The Guessing Game \n' \
           'EXT - Exit'
def startGame():
    global actualNumber,gameIsActive
    if not (gameIsActive):
     gameIsActive = True
     actualNumber = random.randint(0, 100)
     return 'Game has been started'
    else:
      return 'Someone has been already playing this game. Please try later ! '
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(startGame, 'STR')
server.register_function(exit, 'EXT')
server.register_function(options, 'OPT')
server.register_function(guess, 'GSS')



# Run the server's main loop
server.serve_forever()