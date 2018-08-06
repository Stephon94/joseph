from app import db, ma

# CONTENT SECTIONS
class Section(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))
	header = db.Column(db.String(50))
	content1 = db.Column(db.String(500))
	content2 = db.Column(db.String(500))
	content3 = db.Column(db.String(500))
	image = db.Column(db.String(50))
	bg_image = db.Column(db.String(50))

	def __unicode__(self):
		return self.name

class SectionSchema(ma.ModelSchema):
	class Meta:
		model = Section

class SocialMediaLink(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	icon = db.Column(db.String(50))
	name = db.Column(db.String(50))

	def __unicode__(self):
		return self.name

class SocialMediaLinkSchema(ma.ModelSchema):
	class Meta:
		model = SocialMediaLink

# DATA ITEMS
member_stack = db.Table('member_stack',
	db.Column('member_id', db.Integer, db.ForeignKey('member.id')),
	db.Column('tech_id', db.Integer, db.ForeignKey('tech.id'))
	)

project_stack = db.Table('project_stack',
	db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
	db.Column('tech_id', db.Integer, db.ForeignKey('tech.id'))
	)

project_section = db.Table('project_section',
	db.Column('project_id', db.Integer, db.ForeignKey('project.id')),
	db.Column('section_id', db.Integer, db.ForeignKey('section.id'))
	)

class Tech(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	icon = db.Column(db.String(100))
	name = db.Column(db.String(200))

	def __unicode__(self):
		return self.name

class TechSchema(ma.ModelSchema):
	class Meta:
		model = Tech

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	about = db.Column(db.String(100))
	linkedin = db.Column(db.String(100))
	stack = db.relationship('Tech', secondary=member_stack, backref=db.backref('members', lazy='dynamic'))

	def __unicode__(self):
		return self.name

class MemberSchema(ma.ModelSchema):
	class Meta:
		model = Member

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	image = db.Column(db.String(100))
	about = db.Column(db.String(250))
	url = db.Column(db.String(250))
	client_or_team = db.Column(db.String(250))
	stack = db.relationship('Tech', secondary=project_stack, backref=db.backref('projects', lazy='dynamic'))
	section = db.relationship('Section', secondary=project_section, backref=db.backref('projects', lazy='dynamic'))

	def __unicode__(self):
		return self.name

class ProjectSchema(ma.ModelSchema):
	class Meta:
		model = Project