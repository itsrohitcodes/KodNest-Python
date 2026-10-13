# Validate Employee Leave Request

class InvalidLeaveDaysError(Exception):
    pass

class InsufficientLeaveBalanceError(Exception):
    pass

leave_balance = int(input())
requested_days = int(input())

# Write your code here
try:
    if requested_days <= 0:
        raise InvalidLeaveDaysError("Leave days must be greater than 0")

    if requested_days > leave_balance:
        raise InsufficientLeaveBalanceError("Requested leave exceeds available balance")

    print("Leave request accepted")

except InvalidLeaveDaysError as e:
    print(e)

except InsufficientLeaveBalanceError as e:
    print(e)