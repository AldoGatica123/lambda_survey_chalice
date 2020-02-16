import smtplib
import json
from chalice import Chalice, CORSConfig
from chalicelib.config import SMTP_USERNAME, SMTP_PASSWORD

app = Chalice(app_name='lambda_survey')
s = smtplib.SMTP()
cors_config = CORSConfig(
        allow_origin="*",
        allow_headers=["X-Special-Header", "X-Requested-With"],
        max_age=600,
        expose_headers=["X-Special-Header"],
        allow_credentials=True
    )

# tony@tecnometro.net
# aldo.gatica.gt@gmail.com


@app.route('/survey', cors=cors_config, methods=['GET'])
def index():
    s.connect('email-smtp.us-east-1.amazonaws.com', 587)
    s.starttls()
    s.login(SMTP_USERNAME, SMTP_PASSWORD)
    message = 'From: aldogatica123@gmail.com\nTo: tony@tecnometro.net\nSubject: Lambda Survey\n\n' \
              'Esta es una prueba'
    s.sendmail('aldogatica123@gmail.com', 'tony@tecnometro.net', message)
    return {'message': 'Correo enviado'}


# @app.route('/survey', cors=cors_config, methods=['POST'])
# def post_survey():
#     body = app.current_request.json_body
#     s.connect('email-smtp.us-east-1.amazonaws.com', 587)
#     s.starttls()
#     s.login(SMTP_USERNAME, SMTP_PASSWORD)
#     message = 'From: aldogatica123@gmail.com\nTo: aldo.gatica.gt@gmail.com\nSubject: Resultados de la Encuesta\n\n' \
#               'Contenido de la encuenta: ' + json.dumps(body)
#     s.sendmail('aldogatica123@gmail.com', 'aldo.gatica.gt@gmail.com', message)
#     return {'message': 'Correo enviado'}


@app.route('/survey', cors=cors_config, methods=['POST'])
def post_survey():
    body = app.current_request.json_body
    print(body)
    return {'message': json.dumps(body)}
