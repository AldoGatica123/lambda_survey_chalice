import os

SMTP_USERNAME = os.environ.get('SMTP_USERNAME')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
ORIGIN_EMAIL = os.environ.get('ORIGIN_EMAIL')
DESTINATION_EMAIL = os.environ.get('DESTINATION_EMAIL')
EMAIL_SUBJECT = 'Lambda Survey Results'
