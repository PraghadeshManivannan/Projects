from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):

    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticateAccount(self):
        return 0
    
    @abstractmethod
    def deposit(self):
        return 0
    
    @abstractmethod
    def withdraw(self):
        return 0
    
    @abstractmethod
    def displayBalance(self):
        return 0

    @abstractmethod
    def transactionHistory(self):
        return 0

class SavingsAccount(Account):
    def __init__(self):

        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        
        self.accountNumber = randint(10000,99999)
        self.balance = []
        self.name = name
        self.balance.append(initialDeposit)
        self.savingsAccount[self.accountNumber] = [self.name,self.balance]
        print(f'Acount created successfully and your account number is { self.accountNumber } \n')

    def authenticateAccount(self,accountNumber):
        
        if accountNumber in self.savingsAccount.keys():
            print('Authentication Successfull!! \n')
            self.accountNumber = accountNumber
            return True
        else:
            print('Authentication failed!! \n')
            return False
    
    def withdraw(self,amount):

        self.amount = amount

        if self.savingsAccount[self.accountNumber][1][-1] > self.amount:
            newBalance = self.savingsAccount[self.accountNumber][1][-1] - self.amount
            self.savingsAccount[self.accountNumber][1].append(newBalance)
            print(f'Amount { self.amount } withdrawn successfully\n')
            self.displayBalance()

        else:
            print(f'Insufficient balance!!! you can able to withdraw { self.savingsAccount[self.accountNumber][1][-1] }\n')

    def deposit(self,amount):

        self.amount = amount
        newBalance = self.savingsAccount[self.accountNumber][1][-1] + self.amount
        self.savingsAccount[self.accountNumber][1].append(newBalance)
        print(f'Amount { self.amount } deposited successfully \n')
        self.displayBalance()

    def displayBalance(self):
        print(f'Available balance is {self.savingsAccount[self.accountNumber][1][-1]}\n')

    def transactionHistory(self):
        print('---------Transaction History---------')
        for i in self.savingsAccount[self.accountNumber][1]:
            print(i)


savingsAccount  = SavingsAccount()

while True:
    print('1.Create Account 2.Existing Account 3.Exit')
    n = int(input('Enter your choice:'))

    if n == 1:
        name = input('Enter your name:')
        initialDeposit = int(input('Enter your initial deposit:'))
        savingsAccount.createAccount(name,initialDeposit)
    
    elif n == 2:
        accountNumber = int(input('Enter your account number:'))
        if savingsAccount.authenticateAccount(accountNumber):
            while True:
                print('1.Deposit 2.Withdraw 3.Transaction History 4.Balance 5.Exit')
                m = int(input('Enter your choice:'))

                if m == 1:
                    amount = int(input('Enter the amount to be deposited:'))
                    savingsAccount.deposit(amount)
                
                elif m == 2:
                    amount = int(input('Enter the amount to be withdrawn:'))
                    savingsAccount.withdraw(amount)
                
                elif m == 3:
                    savingsAccount.transactionHistory()

                elif m == 4:
                    savingsAccount.displayBalance()
                
                elif m == 5:
                    break

                else:
                    print('Enter correct choice')


    elif n == 3:
        break

    else:
        print('Enter correct choice')
    


