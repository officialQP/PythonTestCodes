on = True
while (on == True):
    #Tar input
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))


#Anvander input och skapar olika variabler som har
    division = number1 / number2
    addition = number1 + number2
    subtraktion = number1 - number2
    multiplikation = number1 * number2
    modulu = number1 % number2
    print('Summan ar: ', addition)
    print('Differansen ar: ', subtraktion)
    print('produkten ar: ', multiplikation)
    print('modulen ar: ', modulu)

    userInput = input('vill du fortsatta? Nej/Ja ')
    if userInput in ['n', 'N', 'nej', 'Nej', 'NEJ']:
         on = False
