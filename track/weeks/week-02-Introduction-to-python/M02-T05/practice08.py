# Search for Job Description by ID

# Class for job description
class JobDescription:
    # Initialize the object
    def __init__(self, job_id, company, role):
        self.job_id = job_id
        self.company = company
        self.role = role

    # String representation of the object
    def __str__(self):
        return f"{self.job_id} - {self.company} - {self.role}"

# Class for placement manager
class PlacementManager:
    # Initialize the object
    def __init__(self):
        self.job_descriptions = []

    # Method to add a job description
    def add_job_description(self, job_description): 
        self.job_descriptions.append(job_description)

    # Method to find a job description by ID
    def find_job_by_id(self, job_id):
        # Search for and return the matching object
        for job in self.job_descriptions: 
            if job.job_id == job_id:
                return job
        # Return None if no match is found
        return None

# Create a PlacementManager object
manager = PlacementManager()

# Get the number of job descriptions
n = int(input())

# Loop n times to get job details
for _ in range(n):
    job_id = int(input())
    company = input().strip()
    role = input().strip()

    # Create a new object
    job = JobDescription(job_id, company, role)

    # Add the object to the manager
    manager.add_job_description(job)

# Get the ID to search for
required_id = int(input()) 

# Find the job description
result = manager.find_job_by_id(required_id)

# Display the result
if result is not None:
    print(result)
else:
    print(f"Job description with ID {required_id} not found")