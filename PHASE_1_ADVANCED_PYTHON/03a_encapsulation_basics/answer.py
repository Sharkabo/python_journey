# Complete your task here (refer to task.md)

# Goal 1: Create a BankAccount Class
class BankAccount:
    def __init__(self, balance, account_number, holder) -> None:
        self.__balance = balance
        self.__account_number = account_number
        self.holder = holder
# Goal 2: Implement Account Operations
    def get_balance(self) -> float:
        return self.__balance

    def get_account_info(self) -> str:
        return f"Account holder: {self.holder}\nAccount number: {self.__account_number}"
    
    def deposit(self, deposit_amount: float) -> None:
        if not isinstance(deposit_amount, (int, float)):
            raise ValueError ('Please verify the input is number and number only')
        
        if deposit_amount <= 0:
            raise ValueError ('Please make sure the deposit number is correct')
        
        self.__balance += deposit_amount
    
    def withdraw(self, withdraw_amount: float) -> None:
        if not isinstance(withdraw_amount, (int, float)):
            raise ValueError ('Please verify the input is number and number only')
        
        if withdraw_amount <= 0:
            raise ValueError ('Please make sure the deposit number is correct')
        
        if withdraw_amount > self.__balance:
            raise ValueError ('Please double check the amount you try to withdraw')
        
        self.__balance -= withdraw_amount