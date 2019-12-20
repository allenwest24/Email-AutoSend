# You just have to change the inputs to be your email and password.

# Library used to send emails every certain amount of time of the log
import smtplib

# Sample Message:
test_msg = "Congrats you made something that works.."

# Sends us the email of the log on the given interval
def send_email(email, password, message):
    # Initialize server for gmail
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    # Start server
    email_server.starttls()
    # Login for me
    email_server.login(email, password)
    # Send the log to yourself
    email_server.sendmail(email, email, message)
    # Quit
    email_server.quit()
    
# Call the email send.
send_email("youremail@gmail.com", "yourpassword", test_msg)    
