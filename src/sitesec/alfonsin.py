#!/usr/local/env python
import sys
import os
from datetime import datetime
from opsgenie import OpsGenie
from opsgenie.alert.requests import ListAlertsRequest
from opsgenie.config import Configuration
from opsgenie.errors import OpsGenieError
from slackclient import SlackClient
sys.path.append(os.environ['GAUSSIAN_HOME'])
import src.config.config as config

OG_CONFIG = Configuration(apikey=config.value(['opsgenie', 'apikey']))
OG_CLIENT = OpsGenie(OG_CONFIG)
BOT_ID = config.value(['slack', 'alfonsin_bot_id'])
#CHANNEL = config.value(['slack', 'channel_alerts'])
CHANNEL = config.value(['slack', 'channel_sandbox'])
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
SLACK_CLIENT = SlackClient(config.value(['slack', 'token']))


def handle_command(command, channel):
    response = "no sure"
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    SLACK_CLIENT.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
       RTM API is an events firehose.
       this parsing function returns None unless a message is
       directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


'''
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if SLACK_CLIENT.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(SLACK_CLIENT.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
'''

create_after = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
created_before = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18, 30)
limit = 100
who_is_on_call = '@martin'
#who_is_on_call = '@icincotta'

if __name__ == "__main__":
    if SLACK_CLIENT.rtm_connect():
        print("StarterBot connected and running!")

        try:
            list_alerts_response = OG_CLIENT.alert. \
                list_alerts(ListAlertsRequest(created_after=create_after, created_before=created_before, limit=limit))

            if len(list_alerts_response.alerts) == 0:
                response = 'La casa esta en orden'
            else:
                response = 'La casa NO estuvo en orden. Todo va a estar bien.'

            response += '...And Now, The Watch has Ended. ' + who_is_on_call

            response = 'La noche se avecina, ahora empieza mi guardia (' + who_is_on_call + ')'
            SLACK_CLIENT.api_call("chat.postMessage", link_names=1, channel=CHANNEL, text=response, as_user=True)

        except OpsGenieError as err:
            print "[ERROR]", err.message
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
