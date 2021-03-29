from ex_atm import ATM

class MockBankSystem():
    def __init__(self):
        self.account_dict = {
            # If any of the Keys are not used in your function. Please delete them.
            "1" : {
                "pin" : 1111,
                "check_balance" : 100,
                "saving_balance" : 1000,
                "withdraw_limit" : 200,
                "deposit_limit" : 1000,
                "transfer_limit" : 1000
            },
            "2" : {
                "pin" : 2222,
                "check_balance" : 200,
                "saving_balance" : 2000,
                "withdraw_limit" : 300,
                "deposit_limit" : 2000,
                "transfer_limit" : 1000
            }
        }
   
    def CheckPin(self, account, pin):
        if account not in self.account_dict.keys():
            return False
        else:
            if pin == self.account_dict[account]["pin"]:
                return True
            else:
                return False

    def GetCheckBalance(self, account):
        if account not in self.account_dict.keys():
            return None
        else:
            return self.account_dict[account]["check_balance"]
        
    def GetSavingBalance(self, account):
        if account not in self.account_dict.keys():
            return None
        else:
            return self.account_dict[account]["saving_balance"]

    def DepositToCheck(self, account, amount):
        if account not in self.account_dict.keys():
            return False
        else:
            if amount <= self.account_dict[account]["deposit_limit"]:
                self.account_dict[account]["check_balance"] += amount
                return True
            else:
                return False

    def DepositToSaving(self, account, amount):
        if account not in self.account_dict.keys():
            return False
        else:
            if amount <= self.account_dict[account]["deposit_limit"]:
                self.account_dict[account]["saving_balance"] += amount
                return True
            else:
                return False

    def WithdrawalFromCheck(self, account, amount):
        if account not in self.account_dict.keys():
            return False
        else:
            if amount <= self.account_dict[account]["withdraw_limit"] and amount <= self.account_dict[account]["check_balance"]:
                self.account_dict[account]["check_balance"] -= amount
                return True
            else:
                return False

    def WithdrawalFromSaving(self, account, amount):
        if account not in self.account_dict.keys():
            return False
        else:
            if amount <= self.account_dict[account]["deposit_limit"] and amount <= self.account_dict[account]["saving_balance"]:
                self.account_dict[account]["saving_balance"] -= amount
                return True
            else:
                return False
            
    def TransferToAnotherAccount(self, account, amount, recipientAccount):
        if account not in self.account_dict.keys():
            return False
        else:
            if amount <= self.account_dict[account]["transfer_limit"] and amount <= self.account_dict[account]["check_balance"]:
                self.account_dict[account]["check_balance"] -= amount
                self.account_dict[recipientAccount]["check_balance"] += amount
                return True
            else:
                return False
#Test Authentication            
def TEST_AtmShouldCheckIfPinIsValid():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")

    pinIsValid = atm.AuthenticateAccountAndPin(2222)      # Invalid PIN
    assert pinIsValid == False

    pinIsValid = atm.AuthenticateAccountAndPin(1111)      # Valid PIN
    assert pinIsValid == True


def TEST_AtmShouldNotAllowAccessIfNotAuthenticated():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("2")

    assert atm.GetCheckBalance() == False

#Test Balance            
def TEST_AtmShouldBeAbleToGetCheckBalance():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)

    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 200
    
def TEST_AtmShouldBeAbleToGetSavingBalance():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)
    
    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)
    
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 2000
#Test Deposit            
def TEST_AtmShouldBeAbleToDepositToCheck():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.DepositToCheck(400)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 500

def TEST_AtmShouldBeAbleToDepositToSaving():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.DepositToSaving(800)
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 1800

#Test Deposit limit            
def TEST_AtmShouldNotAllowDepositToCheckOverDepositLimit():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.DepositToCheck(1100)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 100
    
def TEST_AtmShouldNotAllowDepositToSavingOverDepositLimit():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)

    atm.DepositToSaving(3000)
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 2000
#Test Withdraw    
def TEST_AtmShouldBeAbleToWithdrawalFromCheck():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.WithdrawalFromCheck(60)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 40

def TEST_AtmShouldBeAbleToWithdrawalFromSaving():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.WithdrawalFromSaving(150)
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 850


def TEST_AtmShouldNotAllowWithdrawalFromCheckOverDepositLimit():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.WithdrawalFromCheck(1000)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 100
    
def TEST_AtmShouldNotAllowWithdrawalFromSavingOverDepositLimit():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.WithdrawalFromSaving(1500)
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 1000

def TEST_AtmShouldNotAllowWithdrawalFromSavingOverSavingBalance():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)

    atm.WithdrawalFromSaving(3000)
    atm.GetSavingBalance()
    assert atm.currentSavingBalance == 2000

def TEST_AtmShouldAllowTransferAnotherAccount():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.TransferToAnotherAccount(60, "2")
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 40
    
    atm.EraseCurrentAccountInformation()
    #See Check balance("2")
    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 260
    
def TEST_AtmShouldNotAllowTransferAnotherAccountOverTransferLimit():
    atm = ATM()
    bankSystem = MockBankSystem()
    atm.ConnectToBankSystem(bankSystem)

    atm.CardInserted("1")
    atm.AuthenticateAccountAndPin(1111)

    atm.TransferToAnotherAccount(6000, "2")
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 100
    
    atm.EraseCurrentAccountInformation()
    #See Check balance("2")
    atm.CardInserted("2")
    atm.AuthenticateAccountAndPin(2222)
    atm.GetCheckBalance()
    assert atm.currentCheckBalance == 200
        
def main():
    TEST_AtmShouldCheckIfPinIsValid()
    TEST_AtmShouldNotAllowAccessIfNotAuthenticated()
    TEST_AtmShouldBeAbleToGetCheckBalance()
    TEST_AtmShouldBeAbleToGetSavingBalance()
    TEST_AtmShouldBeAbleToDepositToCheck()
    TEST_AtmShouldBeAbleToDepositToSaving()
    TEST_AtmShouldNotAllowDepositToCheckOverDepositLimit()
    TEST_AtmShouldNotAllowDepositToSavingOverDepositLimit()
    TEST_AtmShouldBeAbleToWithdrawalFromCheck()
    TEST_AtmShouldBeAbleToWithdrawalFromSaving()
    TEST_AtmShouldNotAllowWithdrawalFromCheckOverDepositLimit()
    TEST_AtmShouldNotAllowWithdrawalFromSavingOverDepositLimit()
    TEST_AtmShouldNotAllowWithdrawalFromSavingOverSavingBalance()
    TEST_AtmShouldAllowTransferAnotherAccount()
    TEST_AtmShouldNotAllowTransferAnotherAccountOverTransferLimit()
if __name__ == "__main__":
    main()
