from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import random

actualNumber = 0
gameIsActive = False
def guess(guessedNumber):
    if not checkIsNumber(guessedNumber):
        resultText= 'You must input an integer'
        resultBoolean=False
    elif guessedNumber > actualNumber:
        resultText=  'Smaller than this'
        resultBoolean=False
    elif guessedNumber < actualNumber:
        resultText= 'Bigger than this'
        resultBoolean=False
    else:
        resultText= 'You win' +exit()
        resultBoolean=False
    return {'resultText':resultText, 'resultBoolean':resultBoolean}


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
    return '1 - Guess  \n' \
           '2 - Exit'
def startGame():
    global actualNumber,gameIsActive
    if not (gameIsActive):
     gameIsActive = True
     actualNumber = random.randint(0, 100)
     return 'Game has been started'+'\n'+options()+"\n"
    else:
      return 'Someone has been already playing this game. Please try later ! '
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

server.register_function(startGame)
server.register_function(exit, 'EXT')
server.register_function(options, 'OPT')
server.register_function(guess, 'GSS')
server.serve_forever()