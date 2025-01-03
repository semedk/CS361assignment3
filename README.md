This project involves using a communication channel between a Server and a Client through the use
of RabbitMQ in order to create a currency converter.

Before running my code, you will need to install certain applications...
1. Do pip3 install pika
2. Do pip install --user currencyconverter

This is a currency converter. 
The goal is to input a specific amount, a type of currency that describes the input and a type of currency that describes the output you want. 

Before you do anything, run output.py and then after run input.py. output.py will be used to make the currency conversion, we'll make use of it later. Stay on the input.py terminal.

In order to use my currency converter, you'll need to input all of the needed values.
In order to do so, you need to hit 1, 2, and 3 accordingly (based on what the initial prompt gives) and input each of those values.
You'll know if you've gotten through all of them by seeing what values are displayed when looking at the prompt (The default is N/A and 0, so you need to 
replace this with actual currencie abbrevations and a number)

Once you're finished, enter in 7 to submit those values.
![image](https://user-images.githubusercontent.com/108033475/180931400-b1d80777-54e5-48d5-b2da-cbdcf724d194.png)

Hitting 7 will effectively be you 'requesting' for the currency conversion amount.
In order to 'recieve' all you would need to do is wait until the currency conversion is done and the message is sent.
You can look at output.py and see a confirmation message to also verify that the message is being sent after waiting.

UML Sequence Diagram:
![image](https://user-images.githubusercontent.com/108033475/180929808-16c9d30c-d62f-4ebc-8677-3edd3005dcae.png)


