from slack_sdk import WebClient

import os

def post_slack(image):
    token = os.environ['SLACK_TOKEN']
    client = WebClient(token)

    try:
        client.files_upload_v2(file=image, channel=os.getenv('SLACK_CH'))
    except Exception as e:
        print(e)

