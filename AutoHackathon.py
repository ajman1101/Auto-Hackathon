def startScrn():
	print("Welcome to Auto-Hackathon!")
	print("1.Default (Name, Email, Occupation, How They Heard of Event)")
	print("2.Configure (Make Your Own)")
	print("3.Exit")
	choice = raw_input("Please input 1-3: ")
	if int(choice) == 1:
		defaultSignIn()
	elif int(choice) == 2:
		customSignIn()
	elif int(choice) == 3:
		exit()

def defaultSignIn():
	name = raw_input("What is your name? ")
	email = raw_input("What is your email? ")
	occ = raw_input("What is your job? ")
	connection = raw_input("How did you hear of the Hackathon? ")
	import csv
	with open('data.csv','wb') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter=",")
		csvwriter.writerow(['Name','Email','Occ','Connection'])
		csvwriter.writerow([name,email,occ,connection])
	choice = raw_input("Thanks for signing in! Enjoy the Hackathon \n Use 3 to exit, 1 to continue \n")
	if int(choice) == 1:
		defaultSignIn()
	elif int(choice) == 3:
		exit()

def customSignIn():
	print("Custom Sign In Test")


def exit():
	print("Exiting")
	quit()



startScrn()