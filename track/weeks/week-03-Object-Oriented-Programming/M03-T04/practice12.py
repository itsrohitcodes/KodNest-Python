# Build a Polymorphic Notification Runner

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def notify(self):
        pass


class EmailNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def notify(self):
        # Return email notification
        return f"Email: {self.message}"


class SMSNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def notify(self):
        # Return SMS notification
        return f"SMS: {self.message}"


def run_notifications(services):
    # Process all notification objects using one loop
    for notification in notifications:
        print(notification.notify())


message = input()

# Create both objects, store them in one list and run them
email = EmailNotificationService(message)
sms = SMSNotificationService(message)

notifications = [email, sms]

run_notifications(notifications)