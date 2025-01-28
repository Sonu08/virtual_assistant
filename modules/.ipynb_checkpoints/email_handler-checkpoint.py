import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from modules.utils import get_env_variable

def send_email():
    try:
        email = get_env_variable("EMAIL")
        password = get_env_variable("EMAIL_PASSWORD")

        recipient = input("Enter recipient email: ")
        subject = input("Enter the subject: ")
        body = input("Enter the body of the email: ")

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, recipient, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        logging.error("Error sending email", exc_info=True)
        print("Sorry, I couldn't send the email. Please check your setup and try again.")
