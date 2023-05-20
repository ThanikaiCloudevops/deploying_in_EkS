import boto3

ecr_client = boto3.client('ecr')

repository_name = 'my_frst_project'
response = ecr_client.create_respository(repositoryName=repository_name)

kms = boto3.client('kms', region_name='us-east-1')


repository_url = response['repository']['repositoryUrl']['kms'] 
print(repository_url