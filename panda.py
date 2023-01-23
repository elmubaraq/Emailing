import csv
import time
import smtplib, ssl
from email.message import EmailMessage
smtp_server='email-smtp.us-east-2.amazonaws.com'
smtp_port=465
smtp_username='AKIAWZMDTF2HKNAS3GO3'
import csv 
aggregators_dict={} 
with open("./agrregator login.csv", 'r') as file:
    csvreader = csv.reader(file)
    for Row in csvreader:
        #print(Row)
        if '@' in Row[-2]:
            #print(Row[-1])
            aggregators_dict[Row[-2]]=[Row[0],Row[-2],Row[-1]]

keys=['plightlogicalservices@gmail.com']
new_dict= {}

for key in keys:
    try:
        new_dict[key]=aggregators_dict.get(key)
    except:
        pass
for key,value in new_dict.items():
    #print(key,value)
    try:
        email_sender='noreply@fics.ng'
        email_password='BJ/X1W0qBuyFvN3eUhRuN7RpAqsJ8SiKy5/64x+Vu+Lk'
        email_receiver = "%s" %(key)
        subject='FIC eNaira Aggregator Onboarding'
        body="""
            <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body style="color: black; background-color: white;">
        <div style="border:2px green solid;
        padding: 4px 4px;
        margin: 4px 4px;
        background-color: white;
        color: black;
        font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;">
            <b>Dear %s,</b>
            <br><br>
                    
            Compliment of the season, Whilst we work on the Aggregator portal, that will enable Aggregators view registered agents and progress. 
            Below is your login details as an Aggregator, register and update your information.<br><br>
            <b>NOTE:You will be informed when the Aggregator Portal is ready.<br>
            Please ignore if you have already logged in.</b> 
            <br><br>
            Username:<b> %s</b> <br>
            Pasword:<b> %s </b><br><br>
            
            Those who qualify as a Certificed Financial Inclusion Expert, can offer the services listed below:<br>
            <b>Agent Banking</b>: i) Account opening <br>
                        ii) ATM Card issuance<br><br>
            <b>Digital Identity</b>: i) CheckIn <br>
                ii) BVN/NIN enrolement <br>
                iii) Sim card registration. <br><br>
            <b>E-commerce</b>:  i) Jumia Agent(Jforce) <br>
                        ii) Exportation on Alibaba <br><br>
            <b>Credit Guarantee Scheme</b>: i) Credit Bureau <br>
                Community Finance: <br><br>
            
            <b>For further enquiries please call 09134449444, enquiries via whatsapp message 08061992760</b><br>
            Email:  support@ficexchnageplc.ng or  visit our website: https://ficexchangeplc.ng</div>
    </body>
    </html>
    """ %(value[0].strip(), value[1],value[-1])
    
        msg=EmailMessage()
        msg['From']= email_sender
        msg['To']=email_receiver
        msg['Subject']=subject
        msg.set_content(body,subtype='html')
        
        #let add ssl for security

        context=ssl.create_default_context()

            #login and send the mail
            #we specify host smtp.gmail.com, connect through port 465, 
            #and use the context defined above

        with smtplib.SMTP_SSL(smtp_server,smtp_port, context= context) as smtp:
            smtp.login(smtp_username, email_password)
            smtp.sendmail(email_sender, email_receiver, msg.as_string())
            time.sleep(1.2)
            print("Aggregator's details delivered to ",key)
        with open("./sent.csv", 'a') as file:
            file.writelines("Aggregator's login details delivered to "+key+'\n')
            file.close()
    except:
        with open("./failed.csv", 'a') as file:
            print("Unable to deliver aggregator's login details to ")
            file.writelines("Unable to deliver aggregator's details to "+key+'\n')
            file.close()  

    


#AggregatorName,Code,Username,Password 
