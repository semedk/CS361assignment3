# My Currency Converter Project


currencyin = "N/A"
currencyout = "N/A"
theinput = 0
currency = ["U.S. Dollar (USD)", "European Euro (EUR)", "Japanese Yen (JPY)"]
currencyabb = ["USD", "EUR", "JPY"]


print("Welcome to the Currency Converter!")
print("")
print("Here you can convert the value of one currency into another")
print("In order to do so, all you need to do is")
print("establish your number, the currency type of your number,") 
print("and the currency type you want it converted to")
print("")
print("Pick a choice based on your needs")
print("")

while True:
	print("")
	print("1: Establish Currency Type of Input.....Currency Type: %s" % currencyin)
	print("2: Estalbish Input Amount......Input Amount: %d" % theinput)
	print("3: Establish Currency Type of Output....Currency Type: %s" % currencyout)
	print("")
	print("4: Clear All Choices")
	print("5: Quit Program")
	print("")
	print("6: See list of avialable currencies to print out")
	print("7: Submit Values")

	number = input("")

	if number.isnumeric() == False:
		print("Please type in a number")
		continue

	if int(number) == 1:
		while True:
			print("(Hit enter to go back if needed)")
			abbr = input("What currency type would you like for your input?	(Ex. 'USD')\n")

			if abbr == "":
				break
			
			if abbr in currencyabb:
				currencyin = abbr	
				break
			else:
				print("This program does not support '%s' " % abbr)	
	elif int(number) == 2:
		while True:
			print("(Hit enter to go back if needed)")
			numberx = input("What input amount would you like converted? (Ex. '20')\n")

			if numberx == "":
				break
			elif numberx.isnumeric() == True:
				theinput = int(numberx)
				break
			else:
				print("Invalid Input")
	elif int(number) == 3:	
		
		while True:
			print("(Hit enter to go back if needed)")
			abbrout = input("What currency type would you like for your output?	(Ex. 'USD')\n")

			if abbrout == "":
				break
			
			if abbrout in currencyabb:
				currencyout = abbrout	
				break
			else:
				print("This program does not support '%s' " % abbrout)	
	elif int(number) == 4:
		currencyin = "N/A"
		currencyout = "N/A"
		theinput = 0
	elif int(number) == 5:
		break
	elif int(number) == 6:
		print("Currencies Avaialble are listed below...")
		print(currency)
	elif int(number) == 7:
		break
	else:
		print("Invalid Input")
