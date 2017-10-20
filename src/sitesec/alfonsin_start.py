#!/usr/bin/env python
import os
import sys

from opsgenie import OpsGenie
from opsgenie.config import Configuration
from slackclient import SlackClient
sys.path.append(os.environ['GAUSSIAN_HOME'])
import src.config.config as config

OG_CONFIG = Configuration(apikey=config.value(['opsgenie', 'apikey']))
OG_CLIENT = OpsGenie(OG_CONFIG)
BOT_ID = config.value(['slack', 'alfonsin_bot_id'])
# CHANNEL = config.value(['slack', 'channel_alerts'])
CHANNEL = config.value(['slack', 'channel_sandbox'])
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
SLACK_CLIENT = SlackClient(config.value(['slack', 'token']))

who_is_on_call = '@martin'

if __name__ == "__main__":
    if SLACK_CLIENT.rtm_connect():
        print("StarterBot connected and running!")

        response = 'La noche se avecina, ahora empieza mi guardia (' + who_is_on_call + ')'
        SLACK_CLIENT.api_call("chat.postMessage", link_names=1, channel=CHANNEL, text=response, as_user=True)

    else:
        print("Connection failed. Invalid Slack token or bot ID?")
