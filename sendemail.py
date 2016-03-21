import smtplib

fromname = 'Quewayne'
toname = 'Cooze'
subject = 'Test'
msg = 'Hello Cooze'
fromaddr = 'qgrant96@gmail.com'
toaddr  = 'quewayne.grant@yahoo.com'
message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
""" 
messagetosend = message.format(
                             fromname,
                             fromaddr,
                             toname,
                             toaddr,
                             subject,
                             msg)

# Credentials (if needed)
username = 'qgrant96@gmail.com'
password = 'coozeman11'
#password = '{youremailapppassword}''
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
#server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()
