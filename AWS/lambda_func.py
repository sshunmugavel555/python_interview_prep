import boto3
import os

def lambda_handler(event:any, context:any):

    user=event['user']
    visitCount:int=0

    #Create a dynamoDB client
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)

    # Get the current visit count from the table
    response = table.get_item(Key={"user":user})

    if "Item" in response:
        visitCount = response["Item"]["count"]
    
    # Increment the number of visits
    visitCount += 1

    # Writing the visit count back to the table
    table.put_item(Item={"user":user, "count":visitCount})

    return {
        'message' : f"Hello {user} - You have visited this page {visitCount} times!! "    
    }

if __name__ == "__main__":
    os.environ['TABLE_NAME'] = 'vist-count-tbl'
    event = {"user":"myAdmin"}
    print(lambda_handler(event,None))