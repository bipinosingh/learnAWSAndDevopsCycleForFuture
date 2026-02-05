import boto3
from botocore.config import Config

# Create session
session = boto3.Session()

# Where is boto3 looking?
print("=" * 50)
print("CREDENTIAL LOCATION CHECK")
print("=" * 50)

# 1. Check profile being used
print(f"Current profile: {session.profile_name}")

# 2. Get credentials
credentials = session.get_credentials()
if credentials:
    access_key = credentials.access_key
    # Hide most of the key for security
    masked_key = access_key[:4] + "..." + access_key[-4:]
    print(f"Access Key: {masked_key}")
    print(f"Region: {session.region_name}")
else:
    print("No credentials found!")

# 3. List all available profiles
print("\n" + "=" * 50)
print("ALL PROFILES IN ~/.aws/credentials")
print("=" * 50)
import configparser
import os

creds_path = os.path.expanduser('~/.aws/credentials')
if os.path.exists(creds_path):
    config = configparser.ConfigParser()
    config.read(creds_path)
    for section in config.sections():
        print(f"Profile: [{section}]")
else:
    print("No credentials file found!")

# 4. Test the connection
print("\n" + "=" * 50)
print("TESTING CONNECTION TO AWS")
print("=" * 50)
try:
    sts = boto3.client('sts')
    identity = sts.get_caller_identity()
    print(f"Account ID: {identity['Account']}")
    print(f"User ARN: {identity['Arn']}")
    print("✅ SUCCESS: Connected to AWS!")
except Exception as e:
    print(f"❌ ERROR: {e}")