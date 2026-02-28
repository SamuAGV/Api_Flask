import boto3
import json
from botocore.exceptions import ClientError

class AwsSecretManager:

    def __init__(self):
        print("inicio")
        self.client = boto3.client('secretsmanager')
        self.nombre = "Ricardo"

    def get_secret(self, secret_name):
        try:
            response = self.client.get_secret_value(
                SecretId=secret_name
            )
            secret_string = response.get('SecretString')
            return json.loads(secret_string)
        except ClientError as e:
            raise Exception(f"Error: {str(e)}")