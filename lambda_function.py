import json
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = 'mytribal-ai-chatbot'
LESSONS = ['lesson1.pdf', 'lesson2.pdf', ...]

def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    if intent == 'GetLesson':
        day = int(event['currentIntent']['slots']['Day'])
        if 1 <= day <= 7:
            s3_response = s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': BUCKET_NAME, 'Key': f'micro-campaigns/lesson{day}.pdf'},
                ExpiresIn=3600
            )
            response = f"Here's Lesson {day}: {s3_response}"
        else:
            response = "Invalid day. Please enter 1-7."
    else:
        response = "How can I assist you today?"
    return {
        'sessionAttributes': {},
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {'contentType': 'PlainText', 'content': response}
        }
    }
