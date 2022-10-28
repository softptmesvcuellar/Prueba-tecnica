import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_db(filename, bucket):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(filename, bucket, filename)
    except ClientError as e:
        logging.error(e)
        return False
    os.remove(filename)
    return True
