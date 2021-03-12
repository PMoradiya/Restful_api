#!/usr/bin/python3
"""
author : Pradip Moradiya
Purpose: Simple REST API
"""
import csv
import logging
import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# allows REST service from other languages
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


# End-points Definition
@app.route("/top10vulnerabilities/", methods=['GET'])
@cross_origin()
def get_vulnerabilities_per_host():
    logging.debug('get_vulnerabilities_per_host - start')
    host = request.args.get('hostip', type=str)
    if not host:
        return json.dumps({"message":"hostip is mandatory"})
    page = request.args.get('page', 1, type=int)
    result = {}
    with open('docs/vulnerabilities.csv', 'r') as f:
        reader = csv.DictReader(f,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for each_record in reader:
            if each_record['host'] == host:
                vul = each_record['vulnerability']
                result[vul] = result.get(vul, 0) + int(each_record['risk_score'])
    
    result = dict(sorted(result.items(), key=lambda item: (item[1],item[0]), reverse=True)[(page-1)*10:page*10])
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    
    return json.dumps(result)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

