import base64
import boto3
import imghdr
import json
import string
import os
import uuid


BUCKET = os.environ['BUCKET']

s3_client = boto3.client('s3')

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

def handler(event, context):
    
    uname = str(uuid.uuid4())
    
    if event['httpMethod'] == 'POST' :

        image = event['body']
        image_array = bytearray(image, 'ascii')
        image_format = base64.b64decode(image_array)
        image_extension = imghdr.what('', image_format);
        #print(image_extension)
        
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
    
