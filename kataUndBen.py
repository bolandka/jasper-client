#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.MIMEText import MIMEText

def run(input="", mic=None):

    fromaddr = "dummy.dummy@gmail.com"
    toaddrs  = ["dummy.dummy@dummy.org"]
    subject = "Der kleine Wilko möchte zum Trinken abgeholt werden!"
    text = input
    
    msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n%s"
           % (fromaddr, ", ".join(toaddrs), subject, text))

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    #server.set_debuglevel(1)
    server.login(fromaddr, "passwd")
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    
    notification = "Sent mail to Ben and Kata. Subject: '%s', text: '%s'." %(subject, text)
    if mic:
        mic.say(notification)
    print notification

if __name__=="__main__":
    run()
