import boto3

s3=boto3.client('s3')

s3.delete_object(Bucket='shanky-first-bucket',Key='dummy.txt')
