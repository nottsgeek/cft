#!/usr/bin/env python
import boto3
client = boto3.client('cloudformation')
response = client.create_stack(
    StackName='MyS3Bucket',
    TemplateURL='<<template url>>',
    DisableRollback=True,
    ClientRequestToken='string'
)
