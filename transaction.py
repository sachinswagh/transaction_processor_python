from datetime import datetime

class Transaction:
    def __init__(self, id, txn_date, txn_type, account_id, amount, customer):
        self.id = id
        self.txn_date = datetime.strptime(txn_date, '%d/%m/%Y')
        self.txn_type = txn_type
        self.account_id = account_id
        self.amount = amount
        self.customer = customer
        self.closing_balance = 0

    def operate(self, amount):
      return "Operate Not Implemented"

    def signed_amount(self):
      if(self.txn_type == 'D'):
        return(f"-{self.amount}")
      else:
        return(f"+{self.amount}")

    # def print_line(self, customer):
    #   if self.txn_type == 'D':
    #     amount = f"-{self.amount}"
    #   else:
    #     amount = f"+{self.amount}"
    #   line = (customer.id, self.txn_date.date(), self.txn_type, amount, self.clos_balance)
    #   # print(f"customer: {customer.id}")
    #   #print(f"txn_date: {self.txn_date}")
    #   #print(f"txn_type: {self.txn_type}")
    #   #print(f"amount: {self.amount}")
    #   #print(f"running_balance: {self.customer.running_balance}")
    #   # print("\n table: ", table)
    #   # print(' '.join(map(str, line)))
