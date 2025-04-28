import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_FULL_NAME = "firstName lastName" # Needed to correctly display 'From' username - need to be the same as real gmail name
EMAIL_ADDRESS = "email@gmail.com"  
EMAIL_PASSWORD = "aaaa bbbb cccc dddd" # App password for Chrome
EMAIL_SUBJECT = "Insert subject"

# File paths
RECIPIENTS_FILE = "recipients.txt" # One recipient per line
EMAIL_BODY_FILE = "email_body.txt"
EMAIL_ATTACHMENT_FILE = ""

def send_emails():
    # Read recipients from file
    with open(RECIPIENTS_FILE, 'r') as file:
        recipients = [line.strip() for line in file if line.strip()]

    # Read email body from file
    with open(EMAIL_BODY_FILE, 'r') as file:
        email_body = file.read()     
            
    # Create email
    for recipient in recipients:
        msg = MIMEMultipart()
        msg['From'] = f"{EMAIL_FULL_NAME}{EMAIL_ADDRESS}" # Display correct 'From' user
        msg['To'] = recipient
        msg['Subject'] = EMAIL_SUBJECT
        msg.attach(MIMEText(email_body, 'plain'))
        if EMAIL_ATTACHMENT_FILE != "":
            with open(EMAIL_ATTACHMENT_FILE, 'rb') as file:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', 'attachment', filename=EMAIL_ATTACHMENT_FILE.split('/')[-1])
                msg.attach(attachment)

        try:
            # Connect to SMTP server and send email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
                print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")
if __name__ == "__main__":
    send_emails()
