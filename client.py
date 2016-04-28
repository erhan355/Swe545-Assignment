import xmlrpclib
import random
server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")

sum,product,random_number1,random_number2=0,0,0,0
while True:
    try:
     choiceVar = raw_input("Enter 1 for Select and print two random numbers"+
                    "\n"+"Enter 2 for Print the sum of these two numbers"+
                    "\n"+"Enter 3 for Print the product of these two numbers"+"\n"
                    )
     if choiceVar == "1":
        global random_number1,random_number2
        random_number1= random.randint(0, 100)
        random_number2= random.randint(0, 100)
        print(str(random_number1)+" "+str(random_number2))
     elif choiceVar == "2":
        global sum,product,random_number1,random_number2
        sum,product=server.test.sumprod(random_number1, random_number2)
        print(sum)
     elif choiceVar == "3":
        global sum,product,random_number1,random_number2
        sum,product=server.test.sumprod(random_number1, random_number2)
        print(product)
     else:
        print("You must enter 1-3 for selecting an option")
    except ValueError :
     print("An error occured please try again ! \n")
