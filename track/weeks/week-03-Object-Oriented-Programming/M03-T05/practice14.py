# Generate a Plain English Explanation from the Program

class Manager:
    def generate_explanation(self, match_count, required_count, missing_count):
        # Write your code here
        if required_count == 0:
            match_score = 0
        else:
            match_score = (match_count / required_count) * 100

        return f"The student matches {match_count} out of {required_count} required skills. Match Score: {match_score}%. Missing skills: {missing_count}."


match_count = int(input())
required_count = int(input())
missing_count = int(input())

manager = Manager()
print(manager.generate_explanation(match_count, required_count, missing_count))
