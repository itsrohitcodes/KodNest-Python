# Build a Candidate Profile with different access lables

class CandidateProfile:
    def __init__(self, name, email, score):
        # Create a public name attribute
        self.name = name
        # Create a protected email attribute
        self._email = email
        # Create a private score attribute
        self.__score = score

    def get_email(self):
        # Return the protected email
        return self._email

    def get_score(self):
        # Return the private score
        return self.__score

# Getting input from the user
name = input().strip()
email = input().strip()
score = int(input())

# Create one CandidateProfile object
candidate = CandidateProfile(name, email, score)

print("CANDIDATE PROFILE")
# Print the name directly
print(f"Name: {candidate.name}")
# Print the email using get_email()
print(f"Email: {candidate.get_email()}")
# Print the score using get_score()
print(f"Score: {candidate.get_score()}")