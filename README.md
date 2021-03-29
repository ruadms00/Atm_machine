# atm_machine

## Table of contents
* [General Info](#general-info)
* [Instructions](#instruction)

## General Info
This project contatins a simple ATM controller.
### atm.py
atm.py contains all atm functions. <br />

- **ConnectToBankSystem** <br />
This function is used to check if the ATM is connected to a bank system. <br />
- **CardInserted** <br />
This function set the account number if the card is inserted. <br />
- **AuthenticateAccountAndPin** <br />
This function checks if the entered PIN matches to account's PIN <br />
- **GetCheckBalance** <br />
This function returns current balance in Check account. <br />
- **GetSavingBalance** <br />
This function returns current balance in Saving account. <br />
- **DepositToCheck** <br />
This function puts deposit to Check account. <br />
- **DepositToSaving** <br />
This function puts deposit to Saving account. <br />
- **WithdrawalFromCheck** <br />
This function withdraws the certain amount of money from Check account. <br />
- **WithdrawalFromSaving** <br />
This function withdraws the certain amount of money from Saving account. <br />
- **EraseCurrentAccountInformation** <br />
This function is used to remove the information of Account in ATM. <br />
### mock_bank_system.py <br />
This file contains mock bank system which has two accounts and simple functions <br />
- **CheckPin** - return TRUE if given Pin Matches account PIN, else return FALSE <br />
- **GetCheckBalance** - return Check account balance <br />
- **GetSavingBalance** - return Saving account balance <br />
- **DepositToCheck** - add deposit the Check account <br />
- **DepositToSaving** - add deposit the Saving account <br />
- **WithdrawalFromCheck** - withdraw from Check balance <br />
- **WithdrawalFromSaving** - withdraw from Saving balance <br />
- **TransferToAnotherAccount** - Transfer money to another's Check account <br />

And each atm.py's function is tested in the main(). <br />
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
