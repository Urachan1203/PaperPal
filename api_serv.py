import sys
sys.path.append("./")
from flask import Flask, request
from paperpal.topic import Topic
import paperpal.api as api
import paperpal.slack as slack

app = Flask(__name__)

@app.route('/api/addtopic', methods=['POST'])
def add_topic()->dict:
    add_topic_str : str = request.form.get('text')
    topic : Topic = Topic(add_topic_str)
    success : bool = api.add_topic(topic)
    if success : 
        # slack.send_msg(f"Add topic : {add_topic_str}")
        return {
        "response_type" : "in_channel",
        "text" : f"Added topic : {add_topic_str}"
        }
    else : 
        # slack.send_msg(f"Failed to add topic : {add_topic_str}")
        return {
        "response_type" : "in_channel",
        "text" : f"Failed to add topic : {add_topic_str} has already been registered."
        }


@app.route('/api/removetopic', methods=['POST'])
def remove_topic()->bool:
    remove_topic_str : str = request.form.get('text')
    topic : Topic = Topic(remove_topic_str)
    success : bool = api.remove_topic(topic)
    if success: 
        # slack.send_msg(f"Remove topic : {remove_topic_str}")
        return {
        "response_type" : "in_channel",
        "text" : f"Deleted topic : {remove_topic_str}"
	}
    else :
        # slack.send_msg(f"Failed to remove topic : {remove_topic_str}") 
        return {
        "response_type" : "in_channel",
        "text" : f"Failed to delete topic : {remove_topic_str} does not exist."
        }
    
@app.route('/api/gettopics', methods=['POST'])
def get_topics()->bool:
    topics : list[Topic] = api.get_topics()
    msg : str = "Registered topics : "
    for i, topic in enumerate(topics):
        msg += f"{topic.topic_name}"
        if i + 1 != len(topics) : msg += ", "
    return {
    "response_type" : "in_channel",
    "text" : f"{msg}"
    }
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
