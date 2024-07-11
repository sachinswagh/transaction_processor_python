from transaction import Transaction

class Debit(Transaction):
    def operate(self, customer):
      customer.running_balance -= self.amount
      self.closing_balance = customer.running_balance
      # self.print_passbook(customer)