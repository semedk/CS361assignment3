#!/usr/bin/env python
import pika, sys, os
from currency_converter import CurrencyConverter

info = []
currencyin = "N/A"
currencyout = "N/A"
theinput = 0

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def on_request(ch, method, props, body):
    info.append(body.decode('utf-8'))
    conversion = 0
    
    if(len(info) == 3):
        currencyin = info[0]
        currencyout = info[1]
        theinput = int(info[2])
        # Do Currency Conversion Here
        c = CurrencyConverter()
        conversion = c.convert(theinput, currencyin, currencyout)
        # Restart Info Array
        for i in range(0, 3):
            info.pop()
        print("Value Calculated and Sent")

    # Send conversion back to client
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(conversion))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()