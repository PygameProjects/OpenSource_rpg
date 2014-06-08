import account, db

class Bank(object):
  """ This is a imaginary Bank server. """
  def __init__(self, name, money):
    self.name = name
    self.money = money
    
  def transfer_money(self, fromAccount, toAccount, moneyForTransfer):
    #this will send money from account x to account y
    pass
  
  def block_user(self, name):
    #stop user to make any transaction
    pass
  
  def allow_user(self, name):
    #stop the bann of one user
    pass
  
  def enforcement(self, name):
    #if one user can't pay his debt
    #bank take all his money from account
    #and their proprieties
    pass
  
  def take_money(self, name, amount):
    #take amount of money from one account
    pass
  
  def give_money(self, name, amount):
    #give to one account amount of money
    pass
  
  def tax_transaction(self, transaction, precent):
    #take x precents from a transaction
