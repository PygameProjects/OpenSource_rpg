from Bank import *

def register():
  print "Register"
  print "Complete all boxes!\n"
  #request data from user
  user = raw_input("User: ")
  password = raw_input("Password: ")                    
  money = raw_input("How much do you want to deposit? ")
  income = raw_input("What is your income? ")
  cash = raw_input("How much cash do you have? ")
  
  if user and password and money and income and cash: #check if any box is empty
    if user not in database.users.keys(): #check if user exist already in database
      f = open('Account.py', 'a') #open file whre will be wrote  the data
      #write data
      f.write(user + '=Account("'+user+'","'+password+'","","waiting)"\n')
      f.write(user+'.money='+money+'\n')
      f.write(user+'.income='+income+'\n')
      f.write(user+'.proprieties["cash"]='+cash+'\n')
      f.close() #close file
      
      f = open('db.py', 'a') #write file where user will be regitered
      f.write('\n')
      f.write('database.addUser('+user+')') #register user
      f.close() #close file
    else: print "Username already exist!"
  else: print "There are empty boxes!"

def login():
  log = False #this variable say if user is logged in or not
  print "Log in!"
  #request data from user for log in
  user = raw_input("User: ")
  password = raw_input("Password: ")
  if user in database.users.keys(): #check if user exist
    if database.users[user].password == password: #check password
      print "You logged in!"
      log = True #log variable is true => user is logged in
    else: print "Wrong password!"
  else: print "Username doesn't exist!"
  return (log, user) #function return status and name of user
	
	
def main():
  print "Welcome to " + TheBank.name + " bank!"
  print "Type 'log in' to enter in your account, or 'sign up' to register."
  #user select log in panel or register panel
  c = raw_input("> ")
  if c == 'log in':
    log, user = login()
    if log == True: #if status is true
    	print '\n\n\n'
    	admin_acc(user) # function admin_acc() take user as argument
  elif c == 'sign up':
    register()
  else:
    print "This command doesn't exist!"
    
def admin_acc(user):
  while True: 
    #user select what he want to do
    c = raw_input(user+"> ")
    f = open("Bank.py", "a")

    #in progress	
    if c == "buy": #user buy
      item = raw_input("Item: ")
      value = int(raw_input("Value: "))
      if database.users[user].money >= value: #check if user has enough money
        database.users[user].buy(item, value) #user buy
        f.write("database.users['"+user+"'].buy('"+item+"',"+str(value)+")\n") #write action on bank file so it can
        f.close()                                                              #be read next time
      else: print "No enough money!"
      
    elif c == "sell": #user sell
      item = raw_input("Item: ")
      if item in database.users[user].proprieties.keys(): #check if user has the item
        database.users[user].sell(item) #user sell
        f.write("database.users['"+user+"'].buy('"+item+"'\n") #write action on bank file so it can
        f.close()                                              #be read next time
      else: print "You don't have this item!"
      
    elif c == "pay tax": #user pay his taxes
      database.users[user].pay_tax()
      f.write("database.users['"+user+"'].pay_tax()")
      f.close()
      
    elif c == "withdraw": #user withdraw money from bank
      amount = int(raw_input("How much money do you want to withdarw? "))
      if database.users[user].money >= amount: #check if user has in account enough money
        database.users[user].withdraw(amount) #user withdraw
        f.write("database.users['"+user+"'].withdraw("+str(amount)+")") #write action on bank file so it can
        f.close()                                                       #be read next time
      else: print "No enough money!"
      
    elif c == "deposit": #user deposit money in bank
      amount = int(raw_input("How much money do you want to deposit? "))
      break
      #in progress...
				
	
if __name__ == '__main__':
  while True:
    main()
    print "\n\n\n"
