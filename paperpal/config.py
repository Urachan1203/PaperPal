from paperpal.topic import Topic
import json, os

CONFIG_PATH = '/home/ubuntu/paperpal/config.json'

class Config:
    def __init__(self)->None:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f: config_json = json.load(f)
            self.registered_topics : list[Topic] = [Topic(topic_name) for topic_name in config_json['registered_topics']]
        else:  
            self.registered_topics : list[Topic] = []
    
    
    def to_json(self)->dict:
        print([topic.topic_name for topic in self.registered_topics])
        return {
            'registered_topics' : [topic.topic_name for topic in self.registered_topics]
        }
    
    def save_to_json(self)->None:
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self.to_json(), f, indent=4)
    
    def get_registered_topics(self) -> list[Topic]:
        return self.registered_topics
