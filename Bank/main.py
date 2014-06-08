from Bank import *

# Initialize a DB object
db = DB()


def new_acc():
	new_username = raw_input("\nNew Username: ")
	new_password = raw_input("\nNew Password: ")
	
	db.users.append(new_username)
	print "\nWelcome, " + new_username + "! \n"

def login():
	username = raw_input("Username: ")
	password = raw_input("\nPassword: ")
	print "Login successful! \n"
	
def main():
	print "\nWelcome To The Bank\n\n"
	new = raw_input("Are you new to our bank? [y/n]: ")
	
	if new == 'y':
		create_acc = raw_input("\nWould you like to create an account? [y/n]: ")
		
		if create_acc == 'y':
			new_acc()
		elif create_acc == 'n':
			print "Have a good day then. \n"
		else:
			print "Invalid input. Enter y for yes or n for no."
				
	elif new == 'n':
		print "Welcome back then! \n"
		login()
	
if __name__ == '__main__': main()