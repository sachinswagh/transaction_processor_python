from transaction import Transaction

class Credit(Transaction):
  def operate(self, customer):
    customer.running_balance += self.amount
    self.closing_balance = customer.running_balance
    # self.print_passbook(customer)