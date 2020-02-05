import json
from flask import Flask, request, Response
from flask_restplus import Resource, Api
from flask import jsonify
from validations import Validations as validations
from flask_api import status
from mocks import UserMock as userMock

app = Flask(__name__)
api = Api(app)

api = api.namespace('', description="System 1")

@api.route("/user-info/<cpf>", endpoint='user-info')
class userInfo(Resource):
	def get(self, cpf):
     
		if not validations.isValidCpf(cpf):
			return {'code': '1001', "message": 'Invalid CPF'}, status.HTTP_412_PRECONDITION_FAILED

		user = userMock.mockedUserInfos()
  
		return json.dumps(user.__dict__)

if __name__ == '__main__':
     app.run(port='5002', host='0.0.0.0')
