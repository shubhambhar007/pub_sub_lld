from concurrent.futures import ThreadPoolExecutor
from topic import Topic
from threading import Lock

class PubSubSystem:
    def __init__(self):
        self.topics = {}
        self.executor = ThreadPoolExecutor()
        self.topics_lock = Lock()

    def create_topic(self, name):
        if name not in self.topics:
            self.topics[name] = Topic(name)
        return self.topics[name]
    
    def subscribe(self, topic_name, subscriber):
        with self.topics_lock:
            if topic_name in self.topics:
                topic = self.topics[topic_name]
                topic.add_subscriber(subscriber)
            else:
                raise ValueError(f"Topic '{topic_name}' does not exist.")
        
    def unsubscribe(self, topic_name, subscriber):
        with self.topics_lock:
            if topic_name in self.topics:
                topic = self.topics[topic_name]
                topic.remove_subscriber(subscriber)
            else:
                raise ValueError(f"Topic '{topic_name}' does not exist.")
    
    def publish(self, topic_name, message):
        topic = self.topics.get(topic_name)
        if topic:
            self.executor.submit(topic.publish, message)
        else:
            raise ValueError(f"Topic '{topic_name}' does not exist.")
    
    def shutdown(self):
        self.executor.shutdown(wait=True)
        with self.topics_lock:
            self.topics.clear()
        print("PubSubSystem has been shut down and all topics cleared.")

    def get_topics(self):
        return list(self.topics.keys())