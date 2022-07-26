# My Currency Converter Project

# Pika Related Stuff
import pika
import uuid

class Client(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        self.connection.process_data_events(time_limit=None)
        return float(self.response)

# Variables
currencyin = "N/A"
currencyout = "N/A"
theinput = 0
currency = ["U.S. Dollar (USD)", "European Euro (EUR)", "Japanese Yen (JPY)"]
currencyabb = ["USD", "EUR", "JPY"]


# Main Code
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
		message = Client()
		response = message.call(currencyin)
		response = message.call(currencyout)
		response = message.call(str(theinput))
		print("Your Converted Output is: %r" % response)
	else:
		print("Invalid Input")
