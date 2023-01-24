import csv
import time
import smtplib, ssl
from email.message import EmailMessage
smtp_server='email-smtp.us-east-2.amazonaws.com'
smtp_port=465
smtp_username=''
emailPassword = {}
#def validEmail(x):
    #pass
def mubbs(key):
    return key
         
with open("./posapplicant.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        
        """while validEmail(row[2]):
            emailPassword[row[2]]   = row[3]"""
        emailPassword[row[1]]   = row[3]
#emailPassword.pop('email')
#print(emailPassword)

    for key, value in emailPassword.items():
        try:
            #print(key)
            if len(value)==10:
                value='0'+value
            elif(len(value)==13):
                value ='+'+value 
            elif(len(value)<10):
                value='0'+value
            else:
                value=value  
            email_sender='noreply@fics.ng'
            email_password='BJ/X1W0qBuyFvN3eUhRuN7RpAqsJ8SiKy5/64x+Vu+Lk'
            email_receiver = "%s" %(key)
            subject='FIC eNaira Agent Onboarding'
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
            <b>Dear Applicant,</b>
            <br><br>
                    
            Compliment of the season, we bring you good tidings from the <b>Central Bank of Nigeria (CBN).</b><br> 
            The central bank of Nigeria introduced digital currency (eNaira) to encourage cashless policy.<br>
            As an applicant in the pending POS loan, <b>you should benefit from this excercise before others get onboard. We have enrolled you as an eNaira Agent at no cost to you.
            As an eNaira FIC Specialist, you can open eNaira account for your community and get paid for your service.</b>
            Find your login details below and log-in to <a href="https://www.fics.ng"><b>FICS Portal here</b></a> or click <b style="color: blue;">https://www.fics.ng</b>, confirm your information is correct, make correction if necessary and change your pasword.<br><br>
            Username:<b> %s</b> <br>
            Password:<b> %s </b><br><br>
            
            If you qualify as a certificed Financial Inclusion Expert these are other services you can offer:<br>
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
    """ %(mubbs(key), value)
        
            
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
                print('Message delivered to',key)
            with open("./sent.csv", 'a') as file:
                file.writelines('Message delivered to '+key+'\n')
                file.close()   
        except:
            pass
            print(key) 
                #print(Exception)
            with open("./failed.csv", 'a') as file:
                file.writelines('Unable to deliver message to '+key+'\n')
                file.close()      
                #run as python3 packfile.py