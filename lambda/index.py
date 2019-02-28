import boto3
import os
import uuid
import urllib
from contextlib import closing

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
polly = boto3.client('polly')
dynamodb = boto3.resource('dynamodb')

# Generate Id for each photo
photoId = str(uuid.uuid4())

# Detext the text from the image 
def detect_text(bucket, key, version):
    response = rekognition.detect_text(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key,
                'Version': version
            }
        }
    )
    line = []
    for i in response['TextDetections']:
        if i['Type'] == 'LINE':
            print(i['DetectedText']) 
            line.append(i['DetectedText'])
    text = ' '.join(line)
    return text

# Convert the text to audio
def convert_text_to_audio(text):
    response = polly.synthesize_speech(
        OutputFormat='mp3',
        Text = text,
        VoiceId = 'Matthew'
    )
    if "AudioStream" in response:
            with closing(response["AudioStream"]) as stream:
                output = os.path.join("/tmp/", photoId)
                with open(output, "a") as file:
                    file.write(stream.read())   
    return True

# Put the audio in bucket s3
def put_audio_s3(Bucket):
    s3.upload_file(
        '/tmp/' + photoId, 
        Bucket, 
        photoId + ".mp3"
    )
    s3.put_object_acl(
        ACL='private', 
        Bucket=Bucket, 
        Key=photoId + ".mp3")
    return True

# Put in DynamoDb three information: PhotoId, VoiceId and text 
def put_info_dynamo(text, photoId):
    table = dynamodb.Table(os.environ['tableName'])
    response = table.put_item(
        Item={
            'id' : photoId,
            'text' : text,
            'voice' : 'Matthew'
        }
    )
    return response

# main function
def lambda_handler(event, context):
    print(event)
    photoId = str(uuid.uuid4())
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(
                event['Records'][0]['s3']['object']['key'].encode('utf8'))
    version = event['Records'][0]['s3']['object']['versionId']
    text = detect_text(bucket, key, version)
    if convert_text_to_audio(text) == True:
        if put_audio_s3(bucket) == True:
            put_info_dynamo(text, photoId)
            
