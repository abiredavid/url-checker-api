from flask import *
import json
import re

app = Flask(__name__)
# Load data file in memory to speed up lookup
db_file = open("../data/data.json")
db_dump = json.load(db_file)

@app.route('/', methods=['GET'])
def home_page():
    response_data = {
        'Page': 'Home',
        'msg': 'The URL checker API Home'
    }
    json_dump = json.dumps(response_data)
    
    return json_dump

@app.route('/urlinfo/1/<string:hostname_and_port>/<string:path_and_qstr>', methods=['GET'])
def url_info(hostname_and_port, path_and_qstr):
    hostname = re.sub(':\d*', '', hostname_and_port)
    print(hostname)
    
    response_data = list(filter(lambda x:x["url"]==hostname,db_dump))
    print(len(response_data))
    
    if response_data:
        return(response_data[0])
        
    else:
        response_data = {
            'url': hostname,
            'msg': 'hostname ' + hostname + ' does not exist in the database'
        }
        json_dump = json.dumps(response_data)
        
        return json_dump, 404
        
if __name__ == '__main__':
    app.run(port=9009)