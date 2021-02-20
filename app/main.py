from flask import Flask
from flask import request
from twilio.rest import Client
import os
# import marketstack.py
from marketstack import get_stock_price

app = Flask(__name__)

# ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
# TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')

ACCOUNT_ID = "AC91478018baa0178d652562ff820ef775"
TWILIO_TOKEN = "ef3b23d187445d6b543e4a3dbc8c9cc9"

client = Client(ACCOUNT_ID,TWILIO_TOKEN)

# twilio sandbox number
TWILIO_NUMBER = 'whatsapp:+14155238886' 

def process_msg(msg):
    response = ""
    if(msg.upper() ==  "HI"):
        response = "Hello, welcome to stock market bot!"
        response += " Type 'sym:<symbol/ticker>' to get the latest price. 💸"
    elif ('sym' in msg):
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price['full_res']['last']
        last_price_str = str(last_price)
        response = "The last price of: " + stock_symbol+" is: $" + last_price_str
    else:
        response = "Please type 'Hi' to get started."
    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to=recipient
    )


@app.route('/')
def index():
  return "<h1>Welcome to Stocks bot</h1>"

@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return "OK", 200
 