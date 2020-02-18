from datetime import datetime
from chalicelib.config import SMTP_USERNAME, SMTP_PASSWORD, ORIGIN_EMAIL, DESTINATION_EMAIL, EMAIL_SUBJECT
from chalicelib.utils import map


def format_profile(sp):
    profile = sp['profile']
    survey_date = datetime.strptime(profile['date'], '%Y-%m-%d').strftime('%d/%m/%Y')
    profile_message = \
f'''Encuesta recibida:
    Fecha de la encuesta: {survey_date}
    Lugar donde fue atendido: {profile['location']}
    Edad: {profile['age']}
    Género: {map[profile['gender']]}
    Sexo: {map[profile['sex']]}
    Orientación Sexual: {map[profile['orientation']]}
    Indígena: {'Sí' if profile['indigenous'] else 'No'}
    Discapacitado: {'Sí' if profile['disabled'] else 'No'}
'''
    return profile_message


def send_email(server, email_message):
    server.connect('email-smtp.us-east-1.amazonaws.com', 587)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = f'From: {ORIGIN_EMAIL}\nTo: {DESTINATION_EMAIL}\nSubject: {EMAIL_SUBJECT}\n\n' \
              f'{email_message}'
    server.sendmail(ORIGIN_EMAIL, DESTINATION_EMAIL, message)
    return {'message': 'Email sent successfully'}
