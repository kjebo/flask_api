from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


names = {
    "Kjell": {"age":51, "gender": "M"},
    "Leena" : {"age":47, "gender": "F"},
}
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    def post(self):
        return {"data": "Posted"}

api.add_resource(HelloWorld, "/hello/<string:name>")

if __name__ == "__main_old__":
    app.run(debug=True)

