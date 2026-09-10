# Process Unrelated Notifications Objects using Duck Typing

class EmailNotification:
    # Add constructor and send()
    def __init__(self, email):
        self.email = email

    def send(self):
        return f"Email: {self.email}"


class SMSNotification:
    # Add constructor and send()
    def __init__(self, sms):
        self.sms = sms

    def send(self):
        return f"SMS: {self.sms}"


class PushNotification:
    # Add constructor and send()
    def __init__(self, push):
        self.push = push

    def send(self):
        return f"Push: {self.push}"


def send_notifications(notifications):
    # Process every object using send()
    for notification in notifications:
        print(notification.send())


message = input()

# Create objects, store them in a list, and call send_notifications()
notifications = [
    EmailNotification(message),
    SMSNotification(message),
    PushNotification(message)
]

send_notifications(notifications)