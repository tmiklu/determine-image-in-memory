import base64
import boto3
import imghdr
import json
import string
import os
import io
import uuid


BUCKET = os.environ['BUCKET']

s3_client = boto3.client('s3')


def handler(event, context):
    
    uname = str(uuid.uuid4())
    
    if event['httpMethod'] == 'POST':

        image = event['body']
        image_decode = base64.b64decode(bytearray(image, 'ascii'))
        image_extension = imghdr.what('', image_decode);
        
    
        s3_client.put_object(Bucket=BUCKET, Key=uname + '.' + image_extension, Body=image_decode)
    
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(event)
        }
        
    elif event['httpMethod'] == 'GET' :
        return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/html"
                },
                "body": generate_html()
                
            }

def generate_html():
    content = '''
        <html>
            <body>
                <h1 align="center">Nahraj uctenku</h1></br>
                <form align="center" class="form" id="myForm">
                    <input type="file" name="myHiddenField">
                    <button type="submit">Nahraj</button>
                    <script>
    
                    </script>
            </body>
        </html>
    '''
    return content
