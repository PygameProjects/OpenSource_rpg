from Account import *
from random import random
class DB(object):
  """This keeps all users"""
  total_money = 0
  users = {
    } # 'name_of_account':variable_of_account
  def __init__(self):
  # As far as I can tell it doesn't require any information 
  # to be provided during the initialization. Not yet anyway.
  #We need an account number in this system
  #to secure the system
    #self.account_number = random.random() * (10 ** 16)
    #for more crytography os.urandom() can be used
    pass
    
  def addUser(self, user):
    #add user to DB
    self.users[user.username] = user
  
  def removeUser(self, user):
    #remove user from DB
    del self.users[user.username]
  
  def changeAttribute(self, user, attribute, value):
    #access one attribute of a user and change his value
    pass

#here database is initialized and users are registred
database = DB()


database.addUser(Mihai)

database.addUser(TestUser)