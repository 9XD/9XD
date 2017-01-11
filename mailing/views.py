import requests

SPARK_POST_URL = 'https://api.sparkpost.com/api/v1/transmissions'


def send_email(mail_data):
    data = create_mail_parameter(mail_data)
    r = requests.post(SPARK_POST_URL, data=data)


def create_mail_parameter(mail_data):
    recipients = []
    for recipient in mail_data['recipients']:
        recipients.append({'address': {'email': recipient}})

    return {
        "options": {
            "open_tracking": True,
            "click_tracking": True
        },
        "metadata": {
            "some_useful_metadata": "mail of 9xd"
        },
        "substitution_data": {
            "signature": "Hyeon-Mook Jerry Choi"
        },
        "recipients": recipients,
        "content": {
            "from": {
                "name": "9XD",
                "email": "9xd.official@gmail.com"
            },
            "subject": mail_data['subject'],
            "text": mail_data['text'],
            "html": mail_data['html']
        }
    }
