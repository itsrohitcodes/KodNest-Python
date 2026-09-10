# Convert NotificationService into an Abstract Base Class

from abc import ABC, abstractmethod

class NotificationService(ABC):
    # Add abstract notify()
    @abstractmethod
    def notify(self):
        pass

class EmailNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_email(self):
        return f"Email: {self.message}"

    # Implement notify()
    def notify(self):
        email = self.send_email()

        return email

class SMSNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_sms(self):
        return f"SMS: {self.message}"

    # Implement notify()
    def notify(self):
        sms = self.send_sms()

        return sms

message = input()

# Create both objects and call notify()
email_notification = EmailNotificationService(message)
sms_notification = SMSNotificationService(message)

print(email_notification.notify())
print(sms_notification.notify())