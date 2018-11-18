#!/usr/bin/python
import boto3
import sys
s3_client = boto3.client('s3')

# Upload the file to S3
bucket_url="<<s3 bucket url>>"
cft_file=sys.argv[1]
cft_url=bucket_url + cft_file
stack=sys.arv[2]
print cft_file
print cft_url
s3_client.upload_file(cft_file, 'template', cft_file)
cft_client = boto3.client('cloudformation')
response = cft_client.create_stack(
    StackName=stack,
    TemplateURL=cft_url,
    DisableRollback=True,
    ClientRequestToken='string'
)
print response
