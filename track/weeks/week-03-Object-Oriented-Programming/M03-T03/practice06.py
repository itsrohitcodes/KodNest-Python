# Override a Notification Method

class Notification:
    def send(self, message):
        print(f"General Notification: {message}")


class EmailNotification(Notification):
    # Override send()
    def send(self, message):
        print(f"Email Notification: {message}")


message = input().strip()

# Create both objects and call send()
msg1 = Notification()
msg2 = EmailNotification()


msg1.send(message)
msg2.send(message)
