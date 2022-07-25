#!/usr/bin/env python
import pika, sys, os
from currency_converter import CurrencyConverter

info = []
currencyin = "N/A"
currencyout = "N/A"
theinput = 0

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        #print(" [x] Received %r" % body)
        info.append(body)
        
        if(len(info) == 3):
            currencyin = info[0]
            currencyout = info[1]
            theinput = int(info[2])
        # Do Currency Conversion Here
            c = CurrencyConverter()
            conversion = c.convert(theinput, currencyin, currencyout)
        # Send Back Output of Proper Conversion
    	    channel.basic_publish(exchange='', routing_key='hello', body=str(conversion))
    
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)