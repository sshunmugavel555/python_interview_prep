import boto3

s3_client = boto3.client('s3')

# response = s3_client.upload_file('C:/Users/SShunmugavel/Downloads/dummy.txt','my-s3-bucket5','dummy.txt')

# print(response)

for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])