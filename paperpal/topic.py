import sys
# sys.path.append("./")
# from paperpal.config import Config

class Topic:
    def __init__(self, topic_name : str) -> None:
        self.topic_name : str = topic_name
    
    # return index of duplicate topic, if not duplicate, return -1
    def is_duplicate(self, config) -> int:
        for idx, registered_topic in enumerate(config.registered_topics):
            if registered_topic.topic_name == self.topic_name: return idx
        return -1
