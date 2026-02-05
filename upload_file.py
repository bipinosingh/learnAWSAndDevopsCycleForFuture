import boto3

s3 = boto3.client('s3')
filename = 'test.txt'

# Create a test file
with open(filename, 'w') as f:
    f.write('Test content from Python!')

# Upload to S3
s3.upload_file(filename, 'learnawsforlife1s3bucketawssite', 'uploaded-from-python.txt')
print(f"Uploaded {filename} to S3!")