from flask import Flask, request
from paperpal.topic import Topic
import paperpal.api as api
import paperpal.slack as slack

app = Flask(__name__)

@app.route('/api/addtopic', methods=['POST'])
def add_topic()->bool:
    add_topic_str : str = request.form.get('text')
    topic : Topic = Topic(add_topic_str)
    success : bool = api.add_topic(topic)
    if success : 
        slack.send_msg(f"add topic : {add_topic_str}")
        return True
    else : 
        slack.send_msg(f"failed to add topic : {add_topic_str}")
        return False


@app.route('/api/removetopic', methods=['POST'])
def remove_topic()->bool:
    remove_topic_str : str = request.form.get('text')
    topic : Topic = Topic(remove_topic_str)
    success : bool = api.remove_topic(topic)
    if success: 
        slack.send_msg(f"remove topic : {remove_topic_str}")
        return True
    else :
        slack.send_msg(f"failed to remove topic : {remove_topic_str}") 
        return False
    
@app.route('/api/gettopics', methods=['POST'])
def get_topics()->bool:
    topics : list[Topic] = api.get_topics()
    msg : str = "Registered Topics : "
    for topic in topics:
        msg += f"{topic.topic_name} "
    slack.send_msg(msg)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
