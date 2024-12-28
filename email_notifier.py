import smtplib

def send_mail(sender_email, receiver_email, subject, body, password):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender_email, password)

        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver_email, msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred while sending email: {e}")

if __name__ == "__main__":
    sender_email = 'email'
    receiver_email = 'email'
    subject = "price change information"
    body = "product link and information"
    password = 'xxxxxxxxxxxxxx'

    send_mail(sender_email, receiver_email, subject, body, password)
