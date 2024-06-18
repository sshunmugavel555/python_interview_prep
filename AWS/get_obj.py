import boto3
import json

s3 = boto3.client('s3')

response = s3.get_object(Bucket='my-s3-bucket5',Key='details.json')

data = response['Body'].read()

print(data)



