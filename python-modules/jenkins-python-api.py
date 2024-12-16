import jenkins
import xml.etree.ElementTree as ET

 
"""server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops') #loggin to ur jenkins server
user = server.get_whoami()

print(user)"""




       # how to customise the above code error output messages so user out there will see only few word
"""try:
   #the server is an object
     
   #the server is an object
   server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops') #loggin to ur jenkins server
    #user is a variable
   user = server.get_whoami() # OR server.get_whoiam() # dictionary mthod
  # version = server.get_version() #method
   jobs = server.get_all_jobs()
   print(jobs,user['fullName'])  # how to get a full messade of a particular key in a variable in dictionary =print(variablename['keyname'])
   
except: 
    print("please double check your credential")  """

   # how to know which type or class a data belong to ie either(list, tuple, float, etc)

"""server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops') 
jobs = server.get_all_jobs()
print(type(jobs))"""

 # how to know the total number of element are in a particular list ie len(jobs),len(get_all_jobs)

"""server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops') 
jobs = server.get_all_jobs() # this will tell u in number how many jobs are in this jenkins server
print(len(jobs))"""


#how to print all the jobs runing in a jenkins server
"""server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops') 
jobs = server.get_all_jobs() # this will print out all the jobs in  this jenkins server
for x in jobs:    # (dictionary,loop type) this will print out all the jobs in  this jenkins server
    print(x)
    print('*'*100)""" # this will help u to separate each job from another using 100 star


    # how to differentiate b/w list and dictionary [] and {}, key value ie 'color': blue



    

      # how to use a key value  from dictionary to get it result ie 'fullname':, 'url':
    # this will tell u the name of that job n this jenkins server and the url of that job
"""try:
    # Connect to Jenkins server  # how to use a key value  from dictionary to get it result ie 'fullname':, 'url':
    # this will tell u the name of that job n this jenkins server and the url of that job
    server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops')

    # Job name
    JOB_NAME = 'Nodejs-app'

    # Fetch job information
    job_info = server.get_job_info(JOB_NAME)

    # Extract and print the job URL
    job_url = job_info['url']
    print(f"The URL of the job '{JOB_NAME}' is: {job_url}")

except jenkins.NotFoundException:
    print(f"Job '{JOB_NAME}' not found on the Jenkins server.")
except Exception as e:
    print(f"An error occurred: {e}")"""

   
   
    #how to get the names of all jobs runing on a jenkins server
"""try:
  server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops')   
  jobs = server.get_all_jobs()
  for x in jobs:
      print(x['fullname']) # or print(j.get('fullname'))
except:
      print("please double check your credential") """





       #how to get the URL of all jobs runing on a jenkins server

"""try:
  server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops')   
  jobs = server.get_all_jobs()
  for x in jobs:
      print(x['url']) #or print(j.get('fullname'))
except:
      print("please double check your credential") """

 
 
  # how to direct and output of key value of dictionary to a list using appen method

"""try:
  server = jenkins.Jenkins('http://54.237.237.41:8080', username='devops', password='devops')   
  jobs = server.get_all_jobs()
  job_list =[]
  for x in jobs:
      job_list.append(x.get('fullname'))  #all the fullname of all the jobs runing on our jenkins server will be extracted and real direct it to our empty list called job_list
  #print(job_list)
  print(server.get_job_config('geoapp'))    # this will show u the git link
except:
      print("please double check your credential") """


import jenkins
import xml.etree.ElementTree as ET
import csv

def get_jobs_with_github_links(jenkins_url, username, password):
    try:
        # Connect to Jenkins server
        server = jenkins.Jenkins(jenkins_url, username=username, password=password)
       # print(f"Connecting to Jenkins at: {jenkins_url}")

        # Get all jobs
        jobs = server.get_all_jobs()
        print(f"Total jobs fetched: {len(jobs)}")

        # List to store jobs with GitHub URLs and their links
        github_jobs_with_links = []

        for job in jobs:
            job_name = job['name']
            try:
                # Fetch job configuration
                job_config = server.get_job_config(job_name)
                # Parse XML configuration
                root = ET.fromstring(job_config)
                
                # Look for GitHub URL in the configuration
                github_url = None
                scm_node = root.find(".//scm")
                if scm_node is not None and 'github.com' in ET.tostring(scm_node, encoding='unicode'):
                    github_url = scm_node.find(".//url").text if scm_node.find(".//url") is not None else "URL not found"
                
                # If GitHub URL exists, add to the list as a tuple (job_name, github_url)
                if github_url:
                    github_jobs_with_links.append((job_name, github_url))

            except jenkins.NotFoundException:
               # print(f"Job {job_name} configuration not found. Skipping...")
                continue
            except Exception as e:
               # print(f"Error fetching config for {job_name}: {e}")
                continue

        return github_jobs_with_links

    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

# Example usage
if __name__ == "__main__":
    JENKINS_URL = "http://54.237.237.41:8080"
    USERNAME = "devops"
    PASSWORD = "devops"

    github_jobs = get_jobs_with_github_links(JENKINS_URL, USERNAME, PASSWORD)

    print("Jobs with GitHub URLs:")
    for job, url in github_jobs:
        print(f"{job}: {url}")
       

         # Write the jobs with GitHub URLs to a CSV file excel sheet
    print("Jobs with GitHub URLs:")
    with open("jenkins_inv.csv", 'w', newline='') as f:
        pen = csv.writer(f)
        pen.writerow(["JOB_NAME", "JOBS_GITHUB_URL"])  # This creates headers in the CSV file
        
        for job, url in github_jobs:
            pen.writerow([job, url])  # This writes each job and its GitHub URL to the file

    print("CSV file 'jenkins_inv.csv' has been created with job names and GitHub URLs.")




   
