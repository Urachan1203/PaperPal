from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os

SLACK_CHANNEL = "#fun-daily-thesis"

def send_msg(msg : str) -> bool:
    try:
        client = WebClient(token=os.environ.get('SLACK_API_KEY'))
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=msg
        )
        return True
    except SlackApiError as e:
        print(e)
        return False