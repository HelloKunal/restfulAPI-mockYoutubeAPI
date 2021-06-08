from flask import Flask;
from flask_restful import Api, Resource, reqparse

# init api
app = Flask (__name__)
api = Api (app)

# creating a dict
#names = {"tim": {"age": 19, "gender" : "male"},
#		"bill" : {"age" : 70, "gender" : "male"}}
#
# making resource
#class HelloWorld (Resource):
#	# to handle get request, pull etc
#	def get (self, name):
#		# this what happens when get is send to url
#		return names [name]
#		# returning as json format becuase serializable
#
#	def post (self):
#
#		return {"data": "Posted!"}

# new request handler object according to guildlines
video_put_args = reqparse.RequestParser ()
video_put_args.add_argument ("name", type = str, help = "Name of the video is required", required = True)
video_put_args.add_argument ("views", type = int, help = "Views of the video", required = True)
video_put_args.add_argument ("likes", type = int, help = "Likes of the video", required = True)


videos = {}

class Video (Resource):
	def get (self, video_id):
		return videos [video_id]	

	def put (self, video_id):
		# argumnet parsis to find what fields are important
		# bad method for put
		#print (request.form ["likes"])
		#print (request.form)
		args = video_put_args.parse_args ()
		return {video_id : args}	

api.add_resource (Video, "/video/<int:video_id>")		

# defining the root 
# <> for defining parameter type
#api.add_resource (HelloWorld, "/helloworld/<string:name>")
# / stands for default url		

# debug false for production
if __name__ == "__main__":
	app.run (debug = True)