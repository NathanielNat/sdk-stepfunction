import json
from urllib import response

def handler(event, context):

    # Pass just the field named "guid" into the Lambda, put the
        # Lambda's result in a field called "status" in the response
        # input_path="$.guid",
        # output_path="$.Payload"
    response = {}
    response["status"] = event["guid"]
    return response