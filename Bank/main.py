from Bank import *

def register():
  print "Register"
  print "Complete all boxes!\n"
  user = raw_input("User: ")
  password = raw_input("Password: ")
  money = raw_input("How much do you want to deposit? ")
  income = raw_input("What is your income? ")
  cash = raw_input("How much cash do you have? ")
  if user and password and money and income and cash: #check if any box is empty
    if user not in database.users.keys():
      f = open('Account.py', 'a')
      f.write(user + '=Account("'+user+'","'+password+'","","waiting)"\n')
      f.write(user+'.money='+money+'\n')
      f.write(user+'.income='+income+'\n')
      f.write(user+'.proprieties["cash"]='+cash+'\n')
      f.close()
      
      f = open('db.py', 'a')
      f.write('\n')
      f.write('database.addUser('+user+')')
      f.close()
    else: print "Username already exist!"
  else: print "There are empty boxes!"

def login():
  log = False
  print "Log in!"
  user = raw_input("User: ")
  password = raw_input("Password: ")
  if user in database.users.keys():
    if database.users[user].password == password:
      print "You logged in!"
      log = True
    else: print "Wrong password!"
  else: print "Username doesn't exist!"
  return (log, user)
	
	
def main():
  print "Welcome to " + TheBank.name + " bank!"
  print "Type 'log in' to enter in your account, or 'sign up' to register."
  c = raw_input("> ")
  if c == 'log in':
    log, user = login()
    if log == True:
    	print '\n\n\n'
    	admin_acc(user)
  elif c == 'sign up':
    register()
  else:
    print "This command doesn't exist!"
    
def admin_acc(user):
  while True:
    c = raw_input(user+"> ")
    f = open("Bank.py", "a")

    #in progress	
    if c == "buy":
      item = raw_input("Item: ")
      value = int(raw_input("Value: "))
      if database.users[user].money >= value:
        database.users[user].buy(item, value)
        f.write("database.users['"+user+"'].buy('"+item+"',"+str(value)+")\n")
        f.close()
      else: print "No enough money!"
      
    elif c == "sell":
      item = raw_input("Item: ")
      if item in database.users[user].proprieties.keys():
        database.users[user].sell(item)
        f.write("database.users['"+user+"'].buy('"+item+"'\n")
        f.close()
      else: print "You don't have this item!"
      
    elif c == "pay tax":
      database.users[user].pay_tax()
      f.write("database.users['"+user+"'].pay_tax()")
      f.close()
      
    elif c == "withdraw":
      amount = int(raw_input("How much money do you want to withdarw? "))
      if database.users[user].money >= amount:
        database.users[user].withdraw(amount)
        f.write("database.users['"+user+"'].withdraw("+str(amount)+")")
        f.close()
      else: print "No enough money!"
      
    elif c == "deposit":
      amount = int(raw_input("How much money do you want to deposit? "))
      break
      #in progress...
				
	
if __name__ == '__main__':
  while True:
    main()
    print "\n\n\n"
