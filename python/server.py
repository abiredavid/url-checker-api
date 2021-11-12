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

@app.route('/urlinfo/1/<path:url>', methods=['GET'])
def url_info(url):

    hostname = convert_url_to_hostname(url)

    if hostname:
        response_data = get_url_info_if_exists(hostname)
    else:
        return create_response(url, INVALID_URL.format(url), 400)

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


def get_url_info_if_exists(hostname):
    return list(filter(lambda x:x["url"]==hostname,db_dump))


def convert_url_to_hostname(url):
    return urlparse(url + "/").scheme


if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)