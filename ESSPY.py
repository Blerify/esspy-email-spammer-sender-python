import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromemail = "" #Input your Email Address
frompassword = "" #Input your Email Password
toemail = "" #Input the address you want to send to
numemail = 10 #How many emails do you want to send
n = 1

msg = MIMEMultipart()
msg['From'] = fromemail
msg['To'] = toemail 
msg['Subject'] = "test" #Input Email Subject
body = """
test
""" #Input your text 
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587) #Input which domain to use (gmail, yahoo, abv)
server.starttls()
server.login(fromemail, frompassword)
text = msg.as_string()
print(":Loading ESSPY:")
while n < numemail:
    server.sendmail(fromemail, toemail, text)
    print("sending", n)
    n += 1
    
print ("{} sent {} emails to {}".format(fromemail, numemail, toemail))
server.quit()
