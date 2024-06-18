import boto3

s3 = boto3.client('s3')

bucket_name = "shanky-first-bucket"

file_key = "dummy.txt"

s3.download_file(bucket_name, file_key, "my_file.txt")

with open("my_file.txt", "r") as fp:
    data = fp.read()
    print(data)

