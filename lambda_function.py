import json

def lambda_handler(event, context):
    intent = event['currentIntent']['name']
    slots = event['currentIntent']['slots']
    
    if intent == 'OrderStatus':
        order_id = slots.get('OrderID')
        response = f"Checking status for order {order_id}..."
        # Add DynamoDB query for order status
    elif intent == 'ProductRecommendation':
        product = slots.get('ProductType')
        response = f"Recommending {product} based on trends..."
        # Add logic for recommendations
    elif intent == 'ConsultingInquiry':
        response = "Thanks for your interest! Visit mytribal.ai to book a consultation."
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
