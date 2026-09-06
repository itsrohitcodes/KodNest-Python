# Create a JobDescription from formatted text using a Alternative Constructor

class JobDescription:
    def __init__(
        self,
        role,
        company,
        minimum_experience,
        required_skills
    ):
        # Store all job information
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience
        self.required_skills = required_skills

    @classmethod
    # Create the from_text() alternative constructor
    def from_text(cls, data):
        role, company, minimum_experience, skills = data.split(";")
        role = role.strip()
        company = company.strip()
        minimum_experience = minimum_experience.strip()

        required_skills = [skill.strip() for skill in skills.split(",")]
        return cls(role.title(), company, int(minimum_experience), required_skills)


data = input()

# Create the JobDescription using from_text()
job = JobDescription.from_text(data)

# Print the stored job information
print(f"Role: {job.role}")
print(f"Company: {job.company}")
print(f"Minimum Experience: {job.minimum_experience} years")
print(f"Required Skills: {', '.join(job.required_skills)}")