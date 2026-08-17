# Add and Display Job Descriptions

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
        # Add the received job object
        self.job_descriptions.append(job_description)

    # Method to display job descriptions
    def display_job_descriptions(self):
        # Handle an empty collection
        if not self.job_descriptions:
            print("No job descriptions available")
            return

        # Display all job descriptions
        print("JOB DESCRIPTIONS")
        for job in self.job_descriptions:
            print(job)

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

# Display all job descriptions
manager.display_job_descriptions()