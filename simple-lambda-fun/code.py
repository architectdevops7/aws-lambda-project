def lambda_handler(event, context):
    number = 5  # Replace with your input value
    result = number * number
    return {
        "statusCode": 200,
        "body": str(result),
    }

