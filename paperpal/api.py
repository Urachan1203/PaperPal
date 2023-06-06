from paperpal.config import Config
from paperpal.topic import Topic

def add_topic(topic : Topic)->bool:
    config : Config = Config()
    if topic.is_duplicate(config) == -1:
        config.registered_topics.append(topic)
        config.save_to_json()
        return True
    else:
        return False
    
def remove_topic(topic : Topic)->bool:
    config : Config = Config()
    idx : int = topic.is_duplicate(config)
    if idx == -1: return False
    else:
        config.registered_topics.pop(idx)
        config.save_to_json()
        return True

def get_topics()->list[Topic]:
    config : Config = Config()
    return config.registered_topics
