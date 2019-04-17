class PushButtonLedHandler:
    def __init__(self):
        self.status = 'OFF'

    def is_on(self):
        return self.status == 'ON'

    def on(self):
        self.status = 'ON'
