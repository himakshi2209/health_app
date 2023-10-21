from datetime import date
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def sending(name, toaddr,filename):
    fromaddr = "rejuwel4u@gmail.com"
                # MIMEMultipart 
    msg = MIMEMultipart() 
                # senders email address 
    msg['From'] = fromaddr 

                # receivers email address 
    msg['To'] = toaddr 

                # the subject of mail
    msg['Subject'] = 'Your Rejuwel Health Report - '+str(date.today())
                # open the file to be sent
                # rb is a flag for readonly 
    attachment=open(filename, "r")
                
                # the body of the mail 

    body = 'Dear '+name+','+'\n'+'\n'+'Greetings from Rejuwel !  We hope to find you rejuvenated and well both in body and mind.'+'\n'+'Please find below your daily health report, the same is attached for your perusal.'+'\n'+attachment.read()+'Wishing you always the best of health!'+'\n'+'\n'+'Your Health App,'+'\n'+'Rejuwel'
    
                # attaching the body with the msg 
    msg.attach(MIMEText(body, 'plain'))
    attachment.close()
    attachment=open(filename, "r")
                # MIMEBase
    attc= MIMEBase('application', 'octet-stream') 

                # To change the payload into encoded form 
    attc.set_payload((attachment).read()) 

                # encode into base64 
    encoders.encode_base64(attc) 

    attc.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                

                # attach the instance 'p' to instance 'msg' 
    msg.attach(attc) 

                # creates SMTP session 
    email = smtplib.SMTP('smtp.gmail.com', 587) 

                # TLS for security 
    email.starttls() 

                # authentication 
    email.login(fromaddr, "rejuwel3022") 

                # Converts the Multipart msg into a string 
    message = msg.as_string() 
                # sending the mail 
    email.sendmail(fromaddr, toaddr, message)
