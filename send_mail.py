import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add='202101455@daiict.ac.in'
    to_add='rachit.office2020@gmail.com'
    subject = "Mail from Python Script"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

    body = "<b>Today's Fianance Report Attached.</b>"
    msg.attach(MIMEText(body, 'html'))

    my_file = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, 'djvaizyzpogihqsd')

    server.sendmail(from_add, to_add, message)

    server.quit()
