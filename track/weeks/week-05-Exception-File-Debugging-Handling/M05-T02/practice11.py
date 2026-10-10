# Validate Ticket Booking Count

tickets = int(input())

# Write your code here
try:
    if tickets <= 0 or tickets > 6:
        raise ValueError("Tickets must be between 1 and 6")

    print("Valid ticket count")

except ValueError as e:
    print(e)