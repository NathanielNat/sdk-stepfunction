import json

def handler(event, context):
    response = {}
    response["Payload"] = event["Payload"]
    return response
