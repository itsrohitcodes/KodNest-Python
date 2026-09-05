# Build a job description using static and class methods

class JobDescription:
    platform_name = "KodNest Jobs"

    def __init__(
        self,
        role,
        company,
        minimum_experience
    ):
        # Store the job information
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience

    # Create the is_valid_experience() static method
    @staticmethod
    def is_valid_experience(minimum_experience):
        return 0<= minimum_experience <= 20

    # Create the from_text() class method
    @classmethod
    def from_text(cls, data):
        role, company, minimum_experience = data.split("|")
        minimum_experience = int(minimum_experience)

        if not cls.is_valid_experience(minimum_experience):
            return None

        return cls(
            role.strip().title(),
            company.strip(),
            minimum_experience
        )


data = input()

# Create the job using from_text()
job = JobDescription.from_text(data)

# Print the job or the invalid message
if job is None:
    print("Invalid Experience")
else:
    print(f"Platform: {JobDescription.platform_name}")
    print(f"Role: {job.role}")
    print(f"Company: {job.company}")
    print(f"Minimum Experience: {job.minimum_experience} years")