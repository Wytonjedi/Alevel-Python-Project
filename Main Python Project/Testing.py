import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "mypythonprojects101@gmail.com"
password = "Python123"
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, "15elliottj@stpetershuntingdon.org", "This is a test")
except Exception as e:
    print(e)
finally:
    server.quit()