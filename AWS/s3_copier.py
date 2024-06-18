import boto3

s3 = boto3.resource('s3')

source = {
    'Bucket' : 'my-s3-bucket5',
    'Key' : 'details.json'
}

bucket = s3.Bucket('shanky-first-bucket')

bucket.copy(source,'details_copied_over.json')