import smtplib
import os
from email.message import EmailMessage

#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_ADDRESS = "komal.bansal.2297@gmail.com"
EMAIL_PASSWORD = "Komal@1997"
SENDER = EMAIL_ADDRESS
RECEIVER = "komal.bansal@gen-xt.com"

smtp = smtplib.SMTP_SSL('smtp.gmail.com') 

#METHOD 1

#identifies ourselves with the mail server
#smtp.ehlo()
#encrypting the traffic using tls
#smtp.starttls
#again identifies ourselves with the mail server as encryted connection
#smtp.ehlo()

#login through our mail server
#smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#subject = "Grab dinner this weenend?"
#body = "How about dinner at 6pm this Saturday?"
#msg = f"Subject: {subject} \n\n{body}"
#smtp.sendmail(SENDER, RECEIVER, msg)

#METHOD 2

msg = EmailMessage()
msg['Subject'] = "Grab dinner this weenend?"
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECEIVER
msg.set_content('How about dinner at 6pm this Saturday?')

#adding attachment
#resume_path = os.getcwd() + "/Resume/Komal_bansal.pdf"
directory = os.getcwd() + '/Resume/'
for filename in os.listdir(directory):
    resume_path = os.path.join(directory, filename)
    if not os.path.isfile(resume_path):
        continue
    
    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)
    f = open(resume_path, 'rb')
    file_data = f.read()
    file_name = f.name
    msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)

#Login and send email
smtp = smtplib.SMTP_SSL('smtp.gmail.com') 
smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
smtp.send_message(msg)