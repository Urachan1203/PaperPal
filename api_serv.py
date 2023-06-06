from flask import Flask, request
from paperpal.topic import Topic
import paperpal.api as api

app = Flask(__name__)

@app.route('/api/addtopic', methods=['POST'])
def add_topic()->bool:
    add_topic_str : str = request.form.get('text')
    topic : Topic = Topic(add_topic_str)
    success : bool = api.add_topic(topic)
    if success : return True
    else : return False


@app.route('/api/removetopic', methods=['POST'])
def remove_topic()->bool:
    remove_topic_str : str = request.form.get('text')
    topic : Topic = Topic(remove_topic_str)
    success : bool = api.remove_topic(topic)
    if success: return True
    else : return False
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=12345)
