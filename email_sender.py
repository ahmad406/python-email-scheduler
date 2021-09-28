import smtplib, ssl
import datetime as dt
import time

from apscheduler.schedulers.blocking import BlockingScheduler

sender_email = "xyz@gmail.com"

receiver_email = input("Reciver email address ")

password = "password" # genrate passord from gmail app password genrator

port = 587  

smtp_server = "smtp.gmail.com"


SUBJECT = input("Enter Subject of mail :")
TEXT = input("Enter Message body :")

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)






context = ssl.create_default_context()
def email_sender():
    with smtplib.SMTP(smtp_server, port) as email:
        email.starttls(context=context)
        email.login(sender_email, password)
                
        send_time = dt.datetime(2021,9,22,00,10,0) 

        print(send_time.timestamp())

        print(time.time())



        email.sendmail(sender_email, receiver_email, message)

        print('Email sent')

day = input("Enter date : ")
hr = input("Enter hour in 24hr format : ")
min = input("Enter  minute :  ")

scheduler = BlockingScheduler()
scheduler.add_job(email_sender, 'cron', day = day, hour=hr, minute=min)
scheduler.start()