from datetime import datetime


class LoggingMixin:

    def log_action(self, action):
        print(f"{action} action is performed at {datetime.now()}")