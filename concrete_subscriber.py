class ConcreteSubscriber:
    def __init__(self, name):
        self.name = name

    def on_message(self, message):
        print(f"{self.name} received message: {message.get_content()}")