from concrete_subscriber import ConcreteSubscriber
from message import Message
from topic import Topic
from pub_sub_system import PubSubSystem

class PubSubDemo:
    @staticmethod
    def run_demo():
        pub_sub_system = PubSubSystem()

        #create topics
        topic1 = pub_sub_system.create_topic("Sports")
        topic2 = pub_sub_system.create_topic("Technology")
        print(f"Created topics: {pub_sub_system.get_topics()}")
        #create subscribers
        subscriber1 = ConcreteSubscriber("Alice")
        subscriber2 = ConcreteSubscriber("Bob")
        subscriber3 = ConcreteSubscriber("Charlie")
        #subscribe to topics
        pub_sub_system.subscribe("Sports", subscriber1)
        pub_sub_system.subscribe("Sports", subscriber2)
        pub_sub_system.subscribe("Technology", subscriber3)
        print("Subscribers added to topics.")
        #publish messages
        message1 = Message("Latest sports news!")
        message2 = Message("New tech gadget released!")
        pub_sub_system.publish("Sports", message1)
        pub_sub_system.publish("Technology", message2)
        print("Messages published.")
        #unsubscribe from topics
        pub_sub_system.unsubscribe("Sports", subscriber1)
        print("Alice unsubscribed from Sports topic.")
        #publish another message
        message3 = Message("More sports updates!")
        pub_sub_system.publish("Sports", message3)
        print("Another message published to Sports topic.")
        #shutdown the system
        pub_sub_system.shutdown()

if __name__ == "__main__":
    PubSubDemo.run_demo()
    print("PubSubDemo completed successfully.")