import json
import uuid
import boto3
import os

dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    table_name = os.environ['wishlistTable']
    print('request: {}'.format(json.dumps(event)))
    new_id = str(uuid.uuid4())
    print('Creating new wishlist with id = {}'.format(new_id))
    table = dynamodb.Table(table_name)
    table.put_item(Item={'id': new_id})

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': new_id
    }