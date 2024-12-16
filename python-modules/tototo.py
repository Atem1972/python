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
       

         # Write the jobs with GitHub URLs to a CSV file
    print("Jobs with GitHub URLs:")
    with open("jenkins_inv.csv", 'w', newline='') as f:
        pen = csv.writer(f)
        pen.writerow(["JOB_NAME", "JOBS_GITHUB_URL"])  # This creates headers in the CSV file
        
        for job, url in github_jobs:
            pen.writerow([job, url])  # This writes each job and its GitHub URL to the file

    print("CSV file 'jenkins_inv.csv' has been created with job names and GitHub URLs.")


