from add import add
from subtract import subtract
from multiply import multiply
from divide import divide
import logging

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

formatter = logging.Formatter('Time: [%(asctime)s] - %(levelname)s: [%(message)s]')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

fileHandler = logging.FileHandler('./logs/output.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = f"{num1} + {num2} = {add(num1, num2)}"
            logger.debug(result)

        elif choice == '2':
            result = f"{num1} - {num2} = {subtract(num1, num2)}"
            logger.debug(result)

        elif choice == '3':
            result = f"{num1} * {num2} = {multiply(num1, num2)}"
            logger.debug(result)
            
        elif choice == '4':
            try:
                result = f"{num1} / {num2} = {divide(num1, num2)}"
                logger.debug(result)
            except:
                logger.error("Do Not Divide By Zero")

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
        

    else:
        logger.error("Invalid Input")
