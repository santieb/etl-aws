import json
import boto3
# import requests
BUCKET_ARN = 'arn:aws:s3:::sam-app-datalake'

def lambda_handler(event, context):
    s3 = boto3.resource("s3")
    key = 'diagnosticos.csv'

    obj = s3.get_object(Bucket=BUCKET_ARN, Key=key)
    j = json.loads(obj['Body'].read())
    print(j)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
