import boto3
s3 = boto3.resource(service_name ='s3',
    region_name='us-east-1',
    aws_access_key_id=
    aws_secret_access_key=
)
for i in s3.buckets.all():
    print(i)
print("before buckets ")
print("after buckets")
s3.create_bucket(Bucket='kanchiawsuday')
for i in s3.buckets.all():
    print(i)
s3_resource.Object(bucket_name="kanchiawsuday", key="/home/uk/Pictures/s.png")
    
