# Create Email and SMS Notification classes

class Notification:
    def send(self, message):
        return f"Message: {message}"


class EmailNotification(Notification):
    def send(self, message):
        # Reuse the parent method and add the email channel
        msg = super().send(message)
        return f"{msg} | Sent by Email"


class SMSNotification(Notification):
    def send(self, message):
        # Reuse the parent method and add the SMS channel
        msg = super().send(message)
        return f"{msg} | Sent by SMS"


message = input()

email = EmailNotification()
sms = SMSNotification()

print(email.send(message))
print(sms.send(message))