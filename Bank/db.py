from Account import *

class DB(object):
  """This keeps all users"""
  total_money = 0
  users = {
    } # 'name_of_account':variable_of_account
  
  def __init__(self):
  # As far as I can tell it doesn't require any information 
  # to be provided during the initialization. Not yet anyway.
    pass
    
  def addUser(self, user):
    #add user to DB
    self.users.append(user)
  
  def removeUser(self, user):
    #remove user from DB
    self.users.remove(user)
  
  def changeAttribute(self, user, attribute, value):
    #access one attribute of a user and change his value
    pass

#here database is initialized and users are registred
database = DB()
