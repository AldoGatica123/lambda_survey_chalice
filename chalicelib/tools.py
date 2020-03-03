from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from chalicelib.config import SMTP_USERNAME, SMTP_PASSWORD, ORIGIN_EMAIL, DESTINATION_EMAIL, EMAIL_SUBJECT
from chalicelib.utils import profile_map, slider_map, value_map, get_multibutton_values, get_biswitch_value, score_map


def format_slider_results(sliders):
    question_list = 'Resultados:\n'
    for question in sliders.keys():
        question = f'\t{slider_map[question]}: {value_map[sliders[question]]}'
        question_list = question_list + question + '\n\n'
    return question_list


def format_profile(profile):
    survey_date = datetime.strptime(profile['survey_date'], '%Y-%m-%d').strftime('%d/%m/%Y')
    return f'''Encuesta recibida:
    Fecha de la encuesta: {survey_date}
    Lugar donde fue atendido: {profile['location']}
    Edad: {profile['age']}
    Género: {profile_map[profile['gender']]}
    Sexo: {profile_map[profile['sex']]}
    Orientación Sexual: {profile_map[profile['orientation']]}
    Indígena: {'Sí' if profile['indigenous'] else 'No'}
    Discapacitado: {'Sí' if profile['disability'] else 'No'}\n\n'''


def format_feedback(feedback):
    return f'''Feedback:
    Servicios Prestados: {get_multibutton_values(feedback['services_given'])}
    Se dió respuesta a sus necesidades: {get_biswitch_value((feedback['needs_met']))}
    Feedback de las necesidades: {feedback['needs_feedback']}
    Fue referido por un socio: {get_biswitch_value(feedback['referred_to_partner'])}
    Calidad del servicio del socio: {value_map[feedback['partner_service']]}
    Encontró problemas: {get_biswitch_value(feedback['had_problems'])}
    Problemas encontrados: {feedback['problems_encountered']}
    Donde conoció de los espacios seguros: {get_multibutton_values(feedback['seen_on'])}
    Otros medios: {feedback['additional_channels']}
    Calificación global de los espacios seguros: {score_map[feedback['global_valuation']]}
    Sus datos fueron manejados de manera confidencial: {get_biswitch_value(feedback['is_confidential'])}
    Feedback sobre manejo confidencial de los datos: {feedback['confidential_feedback']}
    Sugerencias: {feedback['suggestions']}\n\n'''


def format_contact(contact):
    if contact['anonymity'] == "true":
        return 'Contacto: Confidencial'
    else:
        return f'''Contacto:
        Nombre: {contact['first_name']}
        Apellido: {contact['last_name']}
        Email: {contact['email']}
        Telefono: {contact['phone_number']}'''


def send_email(server, email_message):
    server.connect('email-smtp.us-east-1.amazonaws.com', 587)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)

    message = MIMEMultipart("alternative")
    message["Subject"] = EMAIL_SUBJECT
    message["From"] = ORIGIN_EMAIL
    message["To"] = DESTINATION_EMAIL

    part1 = MIMEText(email_message, "plain")
    message.attach(part1)

    # message = f'From: {ORIGIN_EMAIL}\nTo: {DESTINATION_EMAIL}\nSubject: {EMAIL_SUBJECT}\n\n' \
    #           f'{email_message}'
    server.sendmail(ORIGIN_EMAIL, DESTINATION_EMAIL, message.as_string())
    return {'message': 'Email sent successfully'}
