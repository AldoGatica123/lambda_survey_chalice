import smtplib
import json
from chalice import Chalice, CORSConfig
from chalicelib.utils import send_email, TEST_MESSAGE

app = Chalice(app_name='lambda_survey')
smtp_client = smtplib.SMTP()
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


@app.route('/test', cors=cors_config, methods=['POST'])
def test_email():
    body = app.current_request.json_body
    print(body)
    if body['payload'] == 'Test payload':
        return send_email(smtp_client, TEST_MESSAGE)
    else:
        return {'message': 'Incorrect test payload'}


@app.route('/notify', cors=cors_config, methods=['POST'])
def post_survey():
    body = app.current_request.json_body
    print(body)
    return {'message': json.dumps(body)}
