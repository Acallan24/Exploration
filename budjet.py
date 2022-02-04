class Budjet:
    def __init__(self, amount):
        self.amount = float(amount)
        self.history = []
    def addmoney(self, amount):
        self.amount += float(amount)
        self.history.append(+amount)
    def subtractmoney(self, amount):
        self.amount -= float(amount)
        self.history.append(-amount)
    def getamountAndHistory(self):
        print( 'Balance History: ', self.history)
        print( 'Current Balance: ', self.amount)

amount = float(input("How much money do you want to start with? "))
b = Budjet(amount)
while True: 
    print(
        '''
        [1] Add money
        [2] Subtract money
        [3] Get amount and history
        [4] Exit
        '''
    )
    option = input("Enter Option:")
    if option == '1':
        amountadd = float(input("How much money do you want to add? "))
        b.addmoney(amountadd)
        b.getamountAndHistory()
    elif option == '2':
        amountsub = float(input("How much money do you want to subtract? "))
        b.subtractmoney(amountsub)
        b.getamountAndHistory()
    elif option == '3':
        b.getamountAndHistory()
    elif option == '4':
        break
    else:
        print("Invalid input, Try again")
        
    








