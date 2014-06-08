class Account(object):
  """ Allow to user to have a personal account 
  and keep their money here, to buy , sell and borrow
  proprieties -> dictionary with name of propriety and its value"""
  money = 0
  total_debt = 0
  pay_per_month = 0
  months = 0
  proprieties = {
    "cash":0
    }
  income = 0
  taxes = 0
  
  def __init__(self, username, password, credit_card):
    self.username = username
    self.password = password
    self.credit_card = credit_card
    
  def buy(self, thing, value):
    #add a thing to proprieties and pay for it
    pass
  
  def sell(self, thing, value):
    #sell a thing from proprieties
    pass
  
  def pay_tax(self):
    #pay monthly taxes
    pass
  
  def withdraw_money(self, amount):
    #withdraw an amount of money from account
    pass
  
  def deposit_money(self, amount):
    #deposit an amount of money in bank
    
