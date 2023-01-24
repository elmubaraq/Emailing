import smtplib, ssl
from email.message import EmailMessage
from PIL import Image
img = Image.open('enaira.png')

my_dict={'recievers':[{'Username':'Mubaraq','mail':'peace.elmubaraq@gmail.com'},{'Username':'Mubbs','mail':'musa.almubaraq@gmail.com'}]}
email_sender='peace.elmubaraq@gmail.com'
email_password=''
email_receiver = 'musa.almubaraq@gmail.com'
subject='Testing'
body="""Hello Almubaraq,

Did you get this?%s
"""(img)
em=EmailMessage()
em['From']= email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

#let add ssl for security

context=ssl.create_default_context()

#login and send the mail
# we specify host smtp.gmail.com, connect through port 465, 
# and use the context defined above

with smtplib.SMTP_SSL('smtp.gmail.com',465, context= context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
#run as python3 gmail.py