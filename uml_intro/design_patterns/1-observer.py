#!/usr/bin/env python3


class NewsSubject:
    def __init__(self):
        self._observers = {}

    def subscribe(self, observer, topics=None):
        self._observers[observer] = set(topics) if topics is not None else None

    def unsubscribe(self, observer):
        if observer in self._observers:
            del self._observers[observer]

    def notify(self, topic, data):
        for observer, topics in list(self._observers.items()):
            if topics is None or topic in topics:
                observer.update(topic, data)


class LogObserver:
    def update(self, topic, data):
        print(f"log:{topic}={data}")


class EmailObserver:
    def update(self, topic, data):
        print(f"email:{topic}={data}")


class SmsObserver:
    def update(self, topic, data):
        print(f"sms:{topic}={data}")


def main():
    subject = NewsSubject()

    log_obs = LogObserver()
    email_obs = EmailObserver()
    sms_obs = SmsObserver()

    subject.subscribe(log_obs, topics={"sports", "breaking"})
    subject.subscribe(email_obs, topics=None)
    # Registering SmsObserver to breaking topic only
    subject.subscribe(sms_obs, topics={"breaking"})

    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()
