import boto3
import json

s3 = boto3.client('s3')

data={
    'name' : 'Shankar',
    'age' : 42,
    'sex' : 'm',
    'nationality' : 'indian'
}

data = json.dumps(data).encode('UTF-8')

response = s3.put_object(Body=data,Bucket='my-s3-bucket5',Key='details.json')

print(response)



