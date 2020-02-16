from chalicelib.config import SMTP_USERNAME, SMTP_PASSWORD, ORIGIN_EMAIL, DESTINATION_EMAIL, EMAIL_SUBJECT

TEST_MESSAGE = 'Test email. \nwoop woop!'

def send_email(smtp_client, email_message):
    smtp_client.connect('email-smtp.us-east-1.amazonaws.com', 587)
    smtp_client.starttls()
    smtp_client.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = f'From: {ORIGIN_EMAIL}\nTo: {DESTINATION_EMAIL}\nSubject: {EMAIL_SUBJECT}\n\n' \
              f'{email_message}'
    smtp_client.sendmail(ORIGIN_EMAIL, DESTINATION_EMAIL, message)
    return {'message': 'Email sent successfully'}
