import db

class Bank(object):
  """ This is a imaginary Bank server. """
  def __init__(self, name, money):
    self.name = name
    self.money = money
    
  def transfer_money(self, fromAccount, toAccount, moneyForTransfer):
    #this will send money from account x to account y
    moneyForTransfer = self.tax_transaction(moneyForTransfer, 2.0/100.0)
    db.database.users.fromAccount.money -= moneyForTransfer
    db.database.users.toAccount.money += moneyForTransfer
  
  def block_user(self, name):
    #stop user to make any transaction
    db.database.users.name.status = 'banned'
  
  def allow_user(self, name):
    #stop the bann of one user
    db.database.users.name.status = 'allowed'
  
  def enforcement(self, name):
    #if one user can't pay his debt
    #bank take all his money from account
    #and their proprieties
    self.money += db.database.users.name.money
    db.database.users.name.money = 0
    db.database.users.name.total_debt = 0
    db.database.users.name.months = 0
    db.database.users.name.pay_per_month = 0
    
    for i in db.database.users.name.proprieties.keys():
      self.money += db.database.users.name.proprieties[i]
      db.database.users.name.proprieties[i] = 0 
  
  def take_money(self, name, amount):
    #take amount of money from one account
    db.database.users.name.money -= amount
    self.money += amount
  
  def give_money(self, name, amount):
    #give to one account amount of money
    db.database.users.name.money += amount
    self.money -= amount
  
  def tax_transaction(self, transaction, precent):
    #take x precents from a transaction
    #and return rest of money
    self.money += precent*transaction
    return transaction - transaction * precent 
