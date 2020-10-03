number = input("Enter number: ")
try:
    numberInt = int(number)
    numberString = str(numberInt).replace('0','5')
    print(numberString)
except:
    print("Invalid number")