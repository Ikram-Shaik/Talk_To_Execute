import smtplib
from email.message import EmailMessage

def send_email(receiver_email, subject, body):
    try:
        email = EmailMessage()
        email['From'] = "ikramshaik.cse.ai@gmail.com"
        email['To'] = receiver_email
        email['Subject'] = subject
        email.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("ikramshaik.cse.ai@gmail.com", "qimb mobd kixt hjve")  # Replace with your app password
            smtp.send_message(email)

            print("✅ Email sent successfully!")
            return True
    except:
        print("Error Occured")