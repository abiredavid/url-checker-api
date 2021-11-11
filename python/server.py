from flask import Flask, request, jsonify
import json
from urllib.parse import urlparse


# Init app
app = Flask(__name__)

#data
db_file = open("../data/data.json")
db_dump = json.load(db_file)

INVALID_HOSTNAME = "hostname: {} does not exist in database."
INVALID_URL = "provided url: {} is invalid."

@app.route('/', methods=['GET'])
def home_page():
    return {
        'Page': 'Home',
        'msg': 'The URL checker API Home'
    }

@app.route('/urlinfo/1/<path:url_string>', methods=['GET'])
def url_info(url_string):
    hostname = urlparse(url_string).scheme

    if hostname:
        response_data = list(filter(lambda x:x["url"]==hostname,db_dump))
    else:
        return create_response(url_string, INVALID_URL.format(url_string), 400)

    if response_data:
        return response_data[0]
    else:
        return create_response(hostname, INVALID_HOSTNAME.format(hostname), 404)


def create_response(url, message, code):
    response_data = {
        'url': url,
        'msg': message
    }

    return response_data, code

if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)