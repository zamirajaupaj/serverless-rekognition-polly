### Lambda Layer Serverless Framework

[![Join the chat at https://gitter.im/Zamira-Jaupaj/serverless-rekognition-polly](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Zamira-Jaupaj/serverless-rekognition-polly)

[![Build Status](https://travis-ci.org/zamirajaupaj/serverless-rekognition-polly.svg?branch=master)](
https://travis-ci.org/zamirajaupaj/serverless-rekognition-polly)

### Requirements 
* Serverless framework 
* AWS Account 
* Mac, Windows, Linux

### Serverless Framework 
* Installing Node.js
**[check the link Node](https://nodejs.org/)**
You can install `nodejs`. Just run:

```
#  Ubuntu
$ curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
$ sudo apt-get install -y nodejs

#  Debian, as root
$ curl -sL https://deb.nodesource.com/setup_8.x | bash -
$ apt-get install -y nodejs
```
* Installing the Serverless Framework
**[check the link Serverless framework ](https://serverless.com/framework/docs/providers/aws/guide/installation/)**

```
$ npm install -g serverless
$ serverless --version

```
### AWS Account 
* if you don't have yet an account on aws, you need an account to deploy lambda function
**[check the link AWS Account ](https://aws.amazon.com/account/)**

### Quickstart 

```
$ git clone https://github.com/zamirajaupaj/serverless-rekognition-polly.git
$ cd serverless-rekognition-polly

```
* Change the variables in params.yml

```
$ sls deploy
$ deactive
$ sls remove 

```

### Lambda Function and Layer

![Architecture of Lambda layer](https://raw.githubusercontent.com/zamirajaupaj/serverless-rekognition-polly/master/architecture/architecture.png)


### Trigger Event
```JSON
{
  "Records": [
    {
      "eventVersion": "2.0",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "s3": {
        "configurationId": "testConfigRule",
        "object": {
          "eTag": "xxxxxxxxxxxxxxxxxx",
          "sequencer": "xxxxxxxxxxxxx",
          "key": "image.jpg",
          "size": 1024
        },
        "bucket": {
          "arn": bucketarn,
          "name": "sourcebucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          }
        },
        "s3SchemaVersion": "1.0"
      },
      "responseElements": {
        "x-amz-id-2": "xxxxxxxxxxxxxxxxxxx",
        "x-amz-request-id": "EXAMPLE123456789"
      },
      "awsRegion": "eu-west-1",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "eventSource": "aws:s3"
    }
  ]
}
```

### Polly 
- Amazon Polly is a service that turns text into lifelike speech
### Rekognition
-  Text in images

Specifically built to work with real world images, Rekognition can detect and recognize text from images, such as street names, captions, product names, and license plates.


### IAM Lambda Policy Permissions for s3
```JSON
{
  "Effect": "Allow",
  "Action": [
      "s3:GetBucketLocation",
      "s3:DeleteObject",
      "s3:GetObject",
      "s3:GetObjectVersion",
      "s3:ListBucket",
      "s3:PutObject"
  ],
  "Resource": [
      "arn:aws:s3:::bucketname",
      "arn:aws:s3:::bucketname/*"
  ]
}
```
### IAM Lambda Policy Permissions for dynamoDb, polly, recognition
```JSON
{
  "Effect": "Allow",
  "Action": [
      "dynamodb:PutItem",
      "polly:SynthesizeSpeech",
      "rekognition:DetectText"
  ],
  "Resource": [
      "*"
  ]
}
```


