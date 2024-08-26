import smtplib

# Email details
sender = "sender@gmail.com"
receiver = "receiver@gmail.com"
password = "your_app_password_here"  # Use the App Password, not your actual Gmail password
subject = "Python email test"
body = "I wrote an email! :D"

# Header
message = f"""From: Snoop Dogg <{sender}>
To: Nicholas Cage <{receiver}>
Subject: {subject}\n
{body}"""

try:
    # Set up the SMTP server connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    
    # Establish connection to the server
    server.ehlo()  # Send the extended hello to the server
    server.starttls()  # Start TLS encryption
    server.ehlo()  # Send another hello to re-identify the connection as secure
    
    # Log in to the server
    server.login(sender, password)
    print("Logged in ...")
    
    # Send the email
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
    
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in: Authentication failed.")
except smtplib.SMTPServerDisconnected:
    print("Unable to send email: Server disconnected.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()  # Ensure the connection is closed properly
