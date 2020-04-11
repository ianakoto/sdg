from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from json import dumps
from flask_jsonpify import jsonify

import src.estimator as mymodule
from collections import namedtuple
import json

from dicttoxml import dicttoxml

app = Flask(__name__)

api = Api(app)

CORS(app)


parser = reqparse.RequestParser()



@app.route("/")
def hello():
    return jsonify({'text':'Hello World!'})

class Employees(Resource):

    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 


class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)   

class Post_JsonData(Resource):  
    def post(self):
        
        parser.add_argument('region', type=str, location='json')
        parser.add_argument('periodType', type=str, location='json')
        parser.add_argument('timeToElapse', type=str, location='json')
        parser.add_argument('reportedCases', type=str, location='json')
        parser.add_argument('population', type=str, location='json')
        parser.add_argument('totalHospitalBeds', type=str, location='json')
        args = parser.parse_args() 

        region_data=str(args.region).replace("'", '"')
        args['region']= json.loads(region_data);

        result = mymodule.estimator(args)

        return jsonify(result)    

class Post_XmlData(Resource):  
    def post(self):
        
        parser.add_argument('region', type=str, location='json')
        parser.add_argument('periodType', type=str, location='json')
        parser.add_argument('timeToElapse', type=str, location='json')
        parser.add_argument('reportedCases', type=str, location='json')
        parser.add_argument('population', type=str, location='json')
        parser.add_argument('totalHospitalBeds', type=str, location='json')
        args = parser.parse_args() 

        region_data=str(args.region).replace("'", '"')
        args['region']= json.loads(region_data);

        result = mymodule.estimator(args)

        return dicttoxml(result)    




api.add_resource(Employees, '/employees')
api.add_resource(Employees_Name, '/employees/<employee_id>')
api.add_resource(Post_JsonData,'/api/v1/on-covid-19')
api.add_resource(Post_JsonData,'/api/v1/on-covid-19/json')
api.add_resource(Post_XmlData,'/api/v1/on-covid-19/xml')






if __name__ == '__main__':
    app.run(port=5000)