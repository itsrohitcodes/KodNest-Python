# Separate Functions Definition From Program Execution

def calculate_total(marks):
    return sum(marks)


def calculate_average(total, count):
    return total / count


if __name__ == "__main__":
    marks = [75, 85, 95]

    total = calculate_total(marks)
    average = calculate_average(total, len(marks))

    print("Total:", total)
    print("Average:", average)