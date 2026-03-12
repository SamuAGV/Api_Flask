import boto3
import os

client = boto3.client(
    "cognito-idp",
    region_name=os_environ.get("AWS_REGION")
)

USER_POOL_ID = os.environ.get("USER_POOL_ID")


def create_cognito_user(email: str, password: str):
    response = client.admin_create_user(
        UserPoolId=USER_POOL_ID,
        Username=email,
        UserAttributes=[
            {"Name": "email","Value": email},
            {"Name": "email_verified","Value": "true"}
        ],
        MessageAction="SUPPRESS"
    )

    client.admin_set_user_password(
        UserPoolId=USER_POOL_ID,
        Username=email,
        Password=password,
        Permanent=True
    )

    attributes = response["User"]["Attributes"]

    sub = next(
        attr["Value"] for attr in attributes if attr["Name"] == "sub"
    )

    return sub