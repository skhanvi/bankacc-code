"""
This is sample program to demonstrate the functionality of bank account
"""
Please mention pylint score here e.g. 9.00 etc
# pylint: disable=superfluous-parens
# pylint: disable=too-few-public-methods
# pylint: disable=literal-comparison


class Bill(object):
    """This class represents bills"""
    def __init__(self, bill_name, bill_amount):
        """This is initialization of Bill"""
        self.bill_name = bill_name
        self.bill_amount = bill_amount

    def print_bill(self):
        """This functions prints bill name and amount"""
        print('Your current', self.bill_name, 'bill for this month is:', self.bill_amount)


class Account(object):
    """This is Account class"""
    def __init__(self, account_title, account_number, account_balance):
        """This is initialization of Account"""
        assert all three parameters types e.g. account title/number should -be of basestring, balance should be of int or float type and save it as float
        self.account_title = account_title
        self.account_number = account_number
        save balance as floating point number
        self.account_balance = account_balance

    def check_balance(self):
        """This checks the balance of the account"""
        print('Your Current balance is: ', self.account_balance)

    def withdraw_money(self):
        """This withdraws money from account_balance"""
        please use proper string formatting all around the prints by following this, new style, https://realpython.com/python-string-formatting/
        print('Available Balance: ', self.account_balance)
        No input validation and exception handling
        amount_to_draw = float(input('Enter the amount to withdraw: '))
        Should it take indefinite tries here
        while amount_to_draw > self.account_balance:
            No input validation and exception handling
            amount_to_draw = float(input('Enter the correct amount again: '))

        self.account_balance = self.account_balance - amount_to_draw
        print('Remaining Balance: ', self.account_balance)

    def transfer_money(self, amount_to_transfer, account_to_deposit):
        """This functions transfers money from one account to another"""
        while self.account_balance <= amount_to_transfer:
            self.check_balance()
            ditto
            amount_to_transfer = float(input('You do not have enough balance\n'
                                             'Enter the correct amount again: '))
        self.account_balance -= amount_to_transfer
        account_to_deposit.account_balance += amount_to_transfer
        self.check_balance()

    def deposit_bills(self, bill_to_deposit):
        """This function deposits bills"""
        if self.account_balance <= bill_to_deposit.bill_amount:
            print('You do not have enough balance in account\n'
                  'Please use cash to deposit bill!')
        else:
            self.account_balance -= bill_to_deposit.bill_amount
            self.check_balance()

    def __lt__(self, account_to_compare):
        """This Function checks if self(account) is less
        then the given account_to_compare(account)"""
        return self.account_balance < account_to_compare.account_balance

    def __gt__(self, account_to_compare):
        """This Function checks if self(account) is greater
            then the given account_to_compare(account)"""
        return self.account_balance > account_to_compare.account_balance

    def __eq__(self, account_to_compare):
        """This Function checks if self(account) is greater
            then the given account_to_compare(account)"""
        return self.account_balance == account_to_compare.account_balance


class Savings(Account):
    """This is Saving class"""
    def __init__(self, account_type, account_title, account_number, account_balance):
        """This is initialization of Savings(Account)"""
        self.account_type = account_type
        super(Savings, self).__init__(account_title, account_number, account_balance)

    def print_type(self):
        """This prints account type"""
        print('Your Account Type is: ', self.account_type)


class Current(Account):
    """This is Current class"""
    def __init__(self, account_type, account_title, account_number, account_balance):
        """This is initialization of Current(Account)"""
        self.account_type = account_type
        super(Current, self).__init__(account_title, account_number, account_balance)

    def print_type(self):
        """This prints account type"""
        print('Your Account Type is: ', self.account_type)


def main():
    """This is the main function"""
    curr1 = Current("Savings", "Account1", 1, 500.0)
    sav1 = Current("Current", "Account2", 2, 100.0)
    curr3 = Current("Current", "Account2", 3, 1000.0)
    # bill1 = Bill("phone", 200)

    accounts = [curr1, sav1, curr3]

    login = int(input("Enter you account number: "))

    print("Here is the menu for your bank account")
    print("1.Check Account Type\n2.Check Balance"
          "\n3.Draw Money\n4.Transfer money"
          "\n5.Pay bill\n6.Compare account"
          "\n7.Quit")

    menu_input = int(input("Enter the number from menu: "))

    while menu_input is not 7:
        if menu_input is 1:
            accounts[login - 1].print_type()
        elif menu_input is 2:
            accounts[login - 1].check_balance()
        elif menu_input is 3:
            accounts[login - 1].withdraw_money()
        elif menu_input is 4:
            money = int(input("Enter the amount to transfer: "))
            account = int(input("Enter the account number to transfer money: "))
            while account > len(accounts):
                account = int(input("Wrong input enter again: "))
            accounts[login - 1].transfer_money(money, accounts[account - 1])
        elif menu_input is 5:
            b_name = input("Enter the bill name: ")
            money = int(input("Enter the amount: "))
            bill = Bill(b_name, money)
            accounts[login - 1].deposit_bills(bill)
        elif menu_input is 6:
            account = int(input("Enter the account to compare with: "))
            while account > len(accounts):
                account = int(input("Wrong input enter again: "))
            if accounts[login - 1] < accounts[account - 1]:
                print("Your account has less balance")
            elif accounts[login - 1] > accounts[account - 1]:
                print("Your account has more balance")
            else:
                print("Your account has equal balance")
        menu_input = int(input("Enter again: "))


if __name__ == "__main__":
    main()
