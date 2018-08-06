from app import app, db
from models import *
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView

admin = Admin(app)

admin.add_view(ModelView(Member,db.session))
admin.add_view(ModelView(Tech,db.session))
admin.add_view(ModelView(Project,db.session))
admin.add_view(ModelView(Section,db.session))
admin.add_view(ModelView(SocialMediaLink,db.session))