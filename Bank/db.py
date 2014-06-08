from Account import *

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

