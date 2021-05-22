class ATM:
    def __init__(self, cardNo, pin):
        self.cardNo=cardNo
        self.pin=pin

    def checkBalance(self):
        print("You have a balance of 20,000")
    def withdraw(self,amount):
        amount2= 20000- amount
        print("you have withdrawn: "+str(amount))
        print("you have a balance of: "+str(amount2))

def ATM2():
    cardNo= input("Enter your card number: ")
    pin= input("Enter your pin: ")

    user= ATM(cardNo,pin)

    print("Do you want to: ")
    print("1. Check your balance")
    print("2. Withdraw Amount")
    choise=int(input("Choose 1 or 2- "))

    if(choise == 1):
        user.checkBalance()
    elif(choise== 2):
        amount=int(input("Enter the amount you would like to withdraw: "))
        user.withdraw(amount)

if __name__ == "__main__":
    ATM2()