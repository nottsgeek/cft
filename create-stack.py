#!/usr/bin/env python
import boto3
client = boto3.client('cloudformation')
response = client.create_stack(
    StackName='MyS3Bucket',
    TemplateURL='https://s3-us-west-2.amazonaws.com/templateash/s3-bucket.yml',
    DisableRollback=True,
    ClientRequestToken='string'
)
