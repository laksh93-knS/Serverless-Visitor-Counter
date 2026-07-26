import json
import boto3
from decimal import Decimal

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')


def lambda_handler(event, context):
    """
    AWS Lambda function to increment and return
    the website visitor count.
    """

    response = table.update_item(
        Key={
            'id': 'visitor-count'
        },
        UpdateExpression='ADD visits :inc',
        ExpressionAttributeValues={
            ':inc': Decimal(1)
        },
        ReturnValues='UPDATED_NEW'
    )

    visitor_count = int(response['Attributes']['visits'])

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'visitorCount': visitor_count
        })
    }
