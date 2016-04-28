import xmlrpclib
import random

def createRandomVar():
    return random.randint(0, 100)
server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")

sum,product,random_number1,random_number2=0,0,0,0
while True:
    try:
     choiceVar = raw_input("Enter 1 : Select and print two random numbers"+
                    "\n"+"Enter 2 : Print the sum of these two numbers"+
                    "\n"+"Enter 3 : Print the product of these two numbers"+"\n"
                    +"Enter 4 : Exit"+"\n"
                    )
     if choiceVar == "1":
        global random_number1,random_number2
        random_number1= createRandomVar()
        #server.guess()
        random_number2= createRandomVar()
        print(str(random_number1)+" "+str(random_number2))
     elif choiceVar == "2":
        global sum,product,random_number1,random_number2
        sum,product=server.test.sumprod(random_number1, random_number2)
        print(sum)
     elif choiceVar == "3":
        global sum,product,random_number1,random_number2
        sum,product=server.test.sumprod(random_number1, random_number2)
        print(product)
     elif choiceVar == "4":
         break
     else:
        print("You must enter 1-4 for selecting an option")
    except ValueError :
     print("You must provide a numerical value ! \n")
