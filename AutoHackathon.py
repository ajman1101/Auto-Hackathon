def startScrn():
	bool firstRun = true;
	bool entryCorrect = false;
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
	checkEntries(true)
		import csv
		with open('data.csv','wb') as csvfile:
			csvwriter = csv.writer(csvfile, delimiter=",")
			if(firstRun):
				csvwriter.writerow(['Name','Email','Occ','Connection'])
			csvwriter.writerow([name,email,occ,connection])
			choice = raw_input("Thanks for signing in! Enjoy the Hackathon! \n Press 1 to Continue (3 to quit) \n")
			if int(choice) == 1:
				firstRun = false
				defaultSignIn()
			elif int(choice) == 3:
				exit()

def customSignIn():
	bool enteringQ =true
	Q1 = raw_input("Enter your Fisrt Question: ")
	Q2 = raw_input("Enter your Second Question: ")
	while(enteringQ):
		questions = [Q1,Q2]
		choice = raw_input("1. Enter Another Question \n 2. Done Adding Questions")
		if int(choice) ==1:
			questions.append(raw_input("Enter Next Question: "))
			num = 1
			for Q in questions:
				print("Q" + num + ": " + Q + "\n")
				num++
		elif int(choice) ==2:
			enteringQ = false

	for Q in questions:
		answers.append(raw_input(Q + ": "))
		
	num =1	
	for Q in questions:
		num++
		for A in answers:
			print(num". "+ Q + ": " + A +"/n")

	choice = raw_input("Is this correct? Enter "+ num+1 +"if correct")	


def checkEntries(bool isDefault):
	if(isDefault = true):
		choice = raw_input("1. Name: "+name + /n +"2. Email: "+ email + /n + "3. Occupation: "+ occ /n +"4. Connection: " + connection + /n +"Is this correct? Enter 5 if correct (Enter the number for the incorrect entry)") 
		if int(choice) == 1:
			name = raw_input("What is your name? ")
		elif int(choice) == 2:
			email = raw_input("What is your email? ")
		elif int(choice) == 3:
			occ = raw_input("What is your job? ")
		elif int(choice) ==4:
			connection = raw_input("How did you hear of the Hackathon? ")
		elif int(choice) ==5:
	else
		print("Custom Check")

def exit():
	print("Exiting")
	quit()



startScrn()