import boto3
iam = boto3.client('iam') 

  # listing user in aws ie iam
"""def list_iam_users(): #i
 iam = boto3.client('iam') # object
 resp = iam.list_users() #variable
 user_list =[]

 for user in resp['Users']: # for each user u get from resp variable go down and append it to that empty list i created #looping through all the list of user
  #print(user['UserName'], user['Arn'],user['CreateDate']) # this will print the value of user
    user_list.append(user['UserName'])
 return user_list #i  
users = list_iam_users() #i
print(users)"""#i function ends here



# howto allow other people use our code we use def
def list_ec2_instance():
 ec2 = boto3.client('ec2', region_name='us-east-1') # object
 resp = ec2. describe_instances() # variable
 instance_list = []
#print(resp)
#print(resp['Reservations'])
#lets loop in the instance list ie go through instance list
 for inst in resp['Reservations']: # this will shw only the element reservation
    for instance in inst['Instances']:
      # print(instance['InstanceID'],instance['ImageID'],instance['KeyName'])
       # store the above information in csv file ie excel sheet
         instance_list.append([instance['InstanceID'],instance['ImageID'],instance['KeyName']])
         #print(instance_list) # use this without def at the beginin
    return instance_list  
 instance = ec2. describe_instances()
 print(instance)


 # how to stop and start ec2 instance in aws
def stop_instance(instances):
 ec2 = boto3.client('ec2', region_name='us-east-1')
# ec2.stop_instance(InstanceIds=['i-066e7ef0181798846']) or
 ec2.stop_instance(InstanceIds=instances)



def start_instance(instances):
  ec2 = boto3.client('ec2', region_name='us-east-1')
# ec2.start_instance(InstanceIds=['i-066e7ef0181798846']) or
  ec2.start_instance(InstanceIds=instances)