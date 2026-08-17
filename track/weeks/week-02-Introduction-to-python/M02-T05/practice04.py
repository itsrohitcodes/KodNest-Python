# Create and Display Multiple Job Descriptions

# Create JobDescription class
class JobDescription:
    # Initialize the object
    def __init__(
        self,
        job_id,
        company,
        role,
        location = "Remote",
        is_active = True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.is_active = is_active

    # String representation of the object
    def __str__(self):
        status="Active" if self.is_active else "Closed"
        return(
            f"{self.company} | "
            f"{self.job_id} | "
            f"{self.role} | "
            f"{self.location} | "
            f"{status}"
        )

# Create job_one using keyword arguments
job_one = JobDescription(
    job_id = "501",
    company = "TechNova",
    role = "Python Developer",
    location = "Bengaluru",
    is_active = True
)

# Create job_two using keyword arguments
job_two = JobDescription(
    job_id = "502",
    company = "CodeWorks",
    role = "Java Developer",
    location = "Hyderabad",
    is_active = True)

# Create job_three using keyword arguments
job_three = JobDescription(
    job_id = "503",
    company = "CloudNine",
    role = "Support Engineer",
    location = "Remote",
    is_active = False
)

# Store all three objects in this list
job_descriptions = []
job_descriptions.append(job_one)
job_descriptions.append(job_two)
job_descriptions.append(job_three)

# Print every object using a for loop
for i in job_descriptions:
    print(i)