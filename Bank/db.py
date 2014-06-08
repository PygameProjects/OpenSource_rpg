import account

class DB(object):
  """This keep all users"""
  total_money = 0
  users = []
  def __init__(self, bank_name, password):
    self.bank_name = bank_name
    self.password = password
    
  def addUser(self, user):
    #add user to DB
    self.users.append(user)
  
  def removeUser(self, user):
    #remove user from DB
    pass
  
  def changeAttribute(self, user, attribute, value):
    #access one attribute of a user and change his value
    pass
  
database = DB('test', 'test')
#test
mihai = account.Account("Mihai", "TEST", "jkOpenWV23", "allowed")
mihai.money = 1000
mihai.total_debt = 300 
mihai.pay_per_month = 30
mihai.months = 10
mihai.income = 200
mihai.taxes = 5.0/100.0 * 1000
mihai.proprieties = {
  "cash":1000,
  "house":10000
  }
