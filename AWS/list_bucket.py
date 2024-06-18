import boto3

s3=boto3.client('s3')

objL=s3.list_objects_v2(Bucket='my-s3-bucket5')

for e in objL['Contents']:
    print(e['Key'])
