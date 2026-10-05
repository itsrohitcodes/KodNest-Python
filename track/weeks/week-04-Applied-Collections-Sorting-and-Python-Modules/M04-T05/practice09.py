# Control Program Execution Using __main__

def get_result(mark):
    if mark >= 40:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    mark = 72
    result = get_result(mark)

    print("Mark:", mark)
    print("Result:", result)