import smtplib
from chalice import Chalice, CORSConfig
from chalicelib.tools import send_email, format_profile, format_slider_results
from chalicelib.utils import TEST_MESSAGE

app = Chalice(app_name='lambda_survey')
smtp_server = smtplib.SMTP()
cors_config = CORSConfig(
        allow_origin="*",
        allow_headers=["X-Special-Header", "X-Requested-With"],
        max_age=600,
        expose_headers=["X-Special-Header"],
        allow_credentials=True
    )


@app.route('/', cors=cors_config, methods=['GET'])
def index():
    return {'message': 'Survey notification service online'}


@app.route('/notify', cors=cors_config, methods=['POST'])
def post_survey():
    body = app.current_request.json_body
    print(body)
    # return send_email(smtp_client, format_message(body))
    message = format_profile(body['profile']) + format_slider_results(body['sliders'])
    return message


@app.route('/test', cors=cors_config, methods=['POST'])
def test_email():
    body = app.current_request.json_body
    print(body)
    if body['payload'] == 'Test payload':
        return send_email(smtp_server, TEST_MESSAGE)
    else:
        return {'message': 'Incorrect test payload'}
