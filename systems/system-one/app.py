import json
from flask import Flask, request, Response
from flask_restplus import Resource, Api
from flask import jsonify
from validations import Validations as validations
from flask_api import status
from database import DatabaseA as db

app = Flask(__name__)
api = Api(app)

api = api.namespace('', description="System 1")

@api.route("/info/<cpf>", endpoint='info')
class userInfo(Resource):
	def get(self, cpf):
     
		if not validations.isValidCpf(cpf):
			return {'code': '1001', "message": 'Invalid CPF'}, status.HTTP_412_PRECONDITION_FAILED

		user = db.getUserInfo(cpf)
  
		return json.dumps(user.__dict__)

if __name__ == '__main__':
     app.run(port='5001', host='0.0.0.0')
