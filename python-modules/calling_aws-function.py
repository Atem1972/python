#import aws_apis  or
from aws_apis import list_ec2_id,start_instance, stop_instance

inst = list_ec2_id()
start_instance(inst)