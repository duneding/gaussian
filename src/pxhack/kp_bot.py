#!/usr/bin/env python
#import src.config.config as config
#from slackclient import SlackClient
import slack

#client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])
slack_token = 'xoxb-2160271414-595069688483-lzF3wSYNjEIxTsiaSp3acmex'
client = slack.WebClient(token=slack_token)

@slack.RTMClient.run_on(event='message')
def say_hello(**payload):
    data = payload['data']
    web_client = payload['web_client']
    rtm_client = payload['rtm_client']
    if 'Hello' in data['text']:
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hi <@{user}>!",
            thread_ts=thread_ts
        )


rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
