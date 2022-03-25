import requests
import time
import smtplib
from email.message import EmailMessage

def send_email():
      
      msg = EmailMessage()

      msg['From'] = "your_gmail"
      msg['To'] = send_email_to
      msg['Subject'] = "💥 Ether Price Alert 💥, ACT FAST!"

      
      message = msg.set_content("Dear " + your_name + "," + "\nEther prices are now "
                                + str(eth_rate) + ". Better transact quickly🙂.\nRegards,\n")
      
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.login("your_gmail", "your_password")
      server.send_message(msg)
      server.quit()

      # prints to your console
      print("successfully sent email to %s:" % (msg['To']))
      print("Price of ether was at " + str(eth_rate))
      

your_name = input('Enter your name: ')

send_email_to = input('Enter email address to send to: ')
alert_amount = input('Alert if Ether price is above: ')

url = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"

while True: 
 
      response = requests.get(
      url,
      headers={"Accept": "application/json"},
      )
      data = response.json()
      USD = data['USD']
      eth_rate = float(USD)
      # print(eth_rate)
     
            
      if eth_rate > int(alert_amount):
            send_email()
            print('Will check again in 3 minutes. Ctrl + C to quit.')
            time.sleep(180)
      else:  
            time.sleep(300)
            print('Price is ' + str(eth_rate) + '. Will check again in 5 minutes. Ctrl + C to quit.')
