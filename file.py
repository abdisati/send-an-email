import smtplib
sender = "sender@gmail.com"
receiver = "receicer@gmail.com"
password ="password123"
subject = "Python email test"
body = "I wrote an email! :D"


#header
message = f"""From: Snoop Dogg{sender}
To: Nicholas Cage{receiver}
Subject: {subject}\n 
{body} """

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()