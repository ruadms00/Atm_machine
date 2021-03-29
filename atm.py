class ATM():
    def __init__(self):
        ''' Currently Selected Account's information '''
        self.currentAccount = ''
        self.currentAccountAuthenticated = False
        self.currentCheckBalance = 0
        self.currentSavingBalance = 0

        # Bank System Related Member Variables
        self.connectedToBankSystem = False
        self.bankSystem = ''


    def ConnectToBankSystem(self, bankSystem):
        self.connectedToBankSystem = True
        self.bankSystem = bankSystem

    def CardInserted(self, accountNumber):
        self.currentAccount = accountNumber

    def AuthenticateAccountAndPin(self, pin):
        if self.connectedToBankSystem:
            self.currentAccountAuthenticated = True
            return self.bankSystem.CheckPin(self.currentAccount, pin)
        else:
            print("ATM is not connected to BankSystem\n")
            return False

    def GetCheckBalance(self):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentCheckBalance = self.bankSystem.GetCheckBalance(self.currentAccount)
            if self.currentCheckBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")

        else:
            print("ATM is not connected to BankSystem or Account is not Authenticated\n")
            return False
        
    def GetSavingBalance(self):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentSavingBalance = self.bankSystem.GetSavingBalance(self.currentAccount)
            if self.currentSavingBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")

        else:
            print("ATM is not connected to BankSystem or Account is not Authenticated\n")
            return False
        
    def DepositToCheck(self, amount):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentCheckBalance = self.bankSystem.GetCheckBalance(self.currentAccount)
            if self.currentCheckBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")
            else:
                depositSucceeded = self.bankSystem.DepositToCheck(self.currentAccount, amount)
                if not depositSucceeded:
                    print("Potentially, your deposit amount exceeded deposit limit")
                    print("Please try smaller amount and if still doesn't work, please contact bank\n")
        else:
            raise RuntimeError("ATM is not connected to BankSystem or Account is not Authenticated\n")

    def DepositToSaving(self, amount):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentSavingBalance = self.bankSystem.GetSavingBalance(self.currentAccount)
            if self.currentSavingBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")
            else:
                depositSucceeded = self.bankSystem.DepositToSaving(self.currentAccount, amount)
                if not depositSucceeded:
                    print("Potentially, your deposit amount exceeded deposit limit")
                    print("Please try smaller amount and if still doesn't work, please contact bank\n")
        else:
            raise RuntimeError("ATM is not connected to BankSystem or Account is not Authenticated\n")
     
    def WithdrawalFromCheck(self, amount):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentCheckBalance = self.bankSystem.GetCheckBalance(self.currentAccount)
            if self.currentCheckBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")
            else:
                depositSucceeded = self.bankSystem.WithdrawalFromCheck(self.currentAccount, amount)
                if not depositSucceeded:
                    print("Potentially, your withdrawal amount exceeded withdrawal limit")
                    print("Please try smaller amount and if still doesn't work, please contact bank\n")
        else:
            raise RuntimeError("ATM is not connected to BankSystem or Account is not Authenticated\n")

    def WithdrawalFromSaving(self, amount):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentSavingBalance = self.bankSystem.GetSavingBalance(self.currentAccount)
            if self.currentSavingBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")
            else:
                withdrawalSucceeded = self.bankSystem.WithdrawalFromSaving(self.currentAccount, amount)
                if not withdrawalSucceeded:
                    print("Potentially, your withdraw amount exceeded withdrawal limit")
                    print("Please try smaller amount and if still doesn't work, please contact bank\n")
        else:
            raise RuntimeError("ATM is not connected to BankSystem or Account is not Authenticated\n")
    
    def TransferToAnotherAccount(self, amount, recipientAccount):
        if self.connectedToBankSystem and self.currentAccountAuthenticated:
            self.currentCheckBalance = self.bankSystem.GetCheckBalance(self.currentAccount)
            if self.currentCheckBalance == None:
                print("Critical Failure while getting account balance information : Please contact Bank\n")
            else:
                transferSucceeded = self.bankSystem.TransferToAnotherAccount(self.currentAccount, amount, recipientAccount)
                if not transferSucceeded:
                    print("Potentially, your transfer amount exceeded transfer limit")
                    print("Please try smaller amount and if still doesn't work, please contact bank\n")
        else:
            raise RuntimeError("ATM is not connected to BankSystem or Account is not Authenticated\n")
              
    def EraseCurrentAccountInformation(self):
        self.currentAccount = ''
        self.currentAccountAuthenticated = False
        self.currentCheckBalance = 0
        self.currentSavingBalance = 0
