import os
import json
import time
import boto3
import requests
from datetime import datetime


def get_messages_in_queue():
    try:
        sqs = boto3.resource('sqs')
        sqs_queue = sqs.get_queue_by_name(QueueName=os.environ['QUEUE_NAME'])
        count = sqs_queue.attributes["ApproximateNumberOfMessages"]
        return int(count)
    except Exception as e:
        print(e)


def invoke_webhook(payload):
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url=os.environ['WEBHOOK_URL'], headers=headers, data=json.dumps(payload))
        if r.status_code == 200:
            print(f"Success: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print(f"Failed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        message_count = get_messages_in_queue()
        payload = {
            "message_count": message_count,
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        invoke_webhook(payload)

        time.sleep(int(os.environ['PUMP_INTERVAL'])*60)

