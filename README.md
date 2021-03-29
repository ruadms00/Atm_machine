# atm_machine

## Table of contents
* [General Info](#general-info)
* [Instructions](#instruction)

## General Info
This project contatins a simple ATM controller.
### atm.py
atm.py contains all atm functions.

**ConnectToBankSystem**
This function is used to check if the ATM is connected to a bank system.
**CardInserted**
This function set the account number if the card is inserted.
**AuthenticateAccountAndPin**
This function checks if the entered PIN matches to account's PIN
**GetCheckBalance**
This function returns current balance in Check account.
**GetSavingBalance**
This function returns current balance in Saving account.
**DepositToCheck**
This function puts deposit to Check account.
**DepositToSaving**
This function puts deposit to Saving account.
**WithdrawalFromCheck**
This function withdraws the certain amount of money from Check account.
**WithdrawalFromSaving**
This function withdraws the certain amount of money from Saving account.
**EraseCurrentAccountInformation**
This function is used to remove the information of Account in ATM.
### mock_bank_system.py
This file contains mock bank system which has two accounts and simple functions
**CheckPin** - return TRUE if given Pin Matches account PIN, else return FALSE
**GetCheckBalance** - return Check account balance
**GetSavingBalance** - return Saving account balance
**DepositToCheck** - add deposit the Check account
**DepositToSaving** - add deposit the Saving account
**WithdrawalFromCheck** - withdraw from Check balance
**WithdrawalFromSaving** - withdraw from Saving balance
**TransferToAnotherAccount** - Transfer money to another's Check account

And each atm.py's function is tested in the main().
Tests include:
- TEST_AtmShouldCheckIfPinIsValid <br />
- TEST_AtmShouldNotAllowAccessIfNotAuthenticated <br />
- TEST_AtmShouldBeAbleToGetCheckBalance <br />
- TEST_AtmShouldBeAbleToGetSavingBalance <br />
- TEST_AtmShouldBeAbleToDepositToCheck <br />
- TEST_AtmShouldBeAbleToDepositToSaving <br />
- TEST_AtmShouldNotAllowDepositToCheckOverDepositLimit <br />
- TEST_AtmShouldNotAllowDepositToSavingOverDepositLimit <br />
- TEST_AtmShouldBeAbleToWithdrawalFromCheck <br />
- TEST_AtmShouldBeAbleToWithdrawalFromSaving <br />
- TEST_AtmShouldNotAllowWithdrawalFromCheckOverDepositLimit <br />
- TEST_AtmShouldNotAllowWithdrawalFromSavingOverDepositLimit <br />
- TEST_AtmShouldNotAllowWithdrawalFromSavingOverSavingBalance <br />
- TEST_AtmShouldAllowTransferAnotherAccount <br />
- TEST_AtmShouldNotAllowTransferAnotherAccountOverTransferLimit <br />

## Setup
To run this program, the code has to be downloaded to the designated directory.
1. Clone the project.
```
git clone https://github.com/ruadms00/atm-machine.git
```
2. Run 'mock_bank_system.py'.
```
python atm-machine/mock_bank_system.py 
```
