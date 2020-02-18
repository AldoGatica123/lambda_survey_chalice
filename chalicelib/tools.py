from datetime import datetime
from chalicelib.config import SMTP_USERNAME, SMTP_PASSWORD, ORIGIN_EMAIL, DESTINATION_EMAIL, EMAIL_SUBJECT
from chalicelib.utils import profile_map, slider_map, value_map


def format_slider_results(sliders):
    question_list = 'Resultados:\n'
    for question in sliders.keys():
        question = f'\t{slider_map[question]}: {value_map[sliders[question]]}'
        question_list = question_list + question + '\n'
    return question_list


def format_profile(profile):
    survey_date = datetime.strptime(profile['date'], '%Y-%m-%d').strftime('%d/%m/%Y')
    return f'''Encuesta recibida:
    Fecha de la encuesta: {survey_date}
    Lugar donde fue atendido: {profile['location']}
    Edad: {profile['age']}
    Género: {profile_map[profile['gender']]}
    Sexo: {profile_map[profile['sex']]}
    Orientación Sexual: {profile_map[profile['orientation']]}
    Indígena: {'Sí' if profile['indigenous'] else 'No'}
    Discapacitado: {'Sí' if profile['disabled'] else 'No'}\n\n'''


def send_email(server, email_message):
    server.connect('email-smtp.us-east-1.amazonaws.com', 587)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = f'From: {ORIGIN_EMAIL}\nTo: {DESTINATION_EMAIL}\nSubject: {EMAIL_SUBJECT}\n\n' \
              f'{email_message}'
    server.sendmail(ORIGIN_EMAIL, DESTINATION_EMAIL, message)
    return {'message': 'Email sent successfully'}
