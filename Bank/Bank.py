import db
reload(db)
from db import *

class Bank(object):
  """ This is a imaginary Bank server. """
  def __init__(self, name, money):
    self.name = name
    self.money = money
    
  def transfer_money(self, fromAccount, toAccount, moneyForTransfer):
    #this will send money from account x to account y
    fromAccount.money -= moneyForTransfer
    moneyForTransfer = self.tax_transaction(moneyForTransfer, 20.0/100.0)
    toAccount.money += moneyForTransfer
  
  def block_user(self, name):
    #stop user to make any transaction
    name.status = 'banned'
  
  def allow_user(self, name):
    #stop the ban of one user
    name.status = 'allowed'
  
  def enforcement(self, name):
    #if one user can't pay his debt
    #bank take all his money from account
    #and their proprieties
    self.money += name.money
    name.money = 0
    name.total_debt = 0
    name.months = 0
    name.pay_per_month = 0
    
    for i in name.proprieties.keys():
      self.money += name.proprieties[i]
      name.proprieties[i] = 0 
  
  def take_money(self, name, amount):
    #take amount of money from one account
    name.money -= amount
    self.money += amount
  
  def give_money(self, name, amount):
    #give to one account amount of money
    name.money += amount
    self.money -= amount
  
  def tax_transaction(self, transaction, precent):
    #take x precents from a transaction
    #and return rest of money
    self.money += precent*transaction
    return transaction - transaction * precent


#here bank is created
TheBank = Bank("Python-Dev", 1000000)
