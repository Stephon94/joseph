from app import app, db
from flask import request, jsonify, make_response
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

@app.route('/', methods=["GET"])
def index():
	print "We Work a little"
	return "Hello World"

@app.route('/getinterface', methods=["GET"])
def get_interface():

	sections = Section.query.all()
	section_schema = SectionSchema(many=True)
	sections = section_schema.dump(sections).data

	projects = Project.query.all()
	project_schema = ProjectSchema(many=True)
	projects = project_schema.dump(projects).data

	members = Member.query.all()
	member_schema = MemberSchema(many=True)
	members = project_schema.dump(members).data

	social = SocialMediaLink.query.all()
	social_schema = SocialMediaLinkSchema(many=True)
	social = social_schema.dump(social).data

	return jsonify({"sections": sections,
					"members": members,
					"projects": projects})
