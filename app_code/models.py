from app import db
from hashlib import md5
from sqlalchemy_utils import URLType
from furl import furl

class Thread(db.Model):

	id = db.Column(db.Integer, primary_key = True)
	popularity = db.Column(db.Integer)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	image = db.Column(URLType)
	subject = db.Column(db.String(64))
	name = db.Column(db.String(64))
	replies = db.relationship('Reply', backref='author', lazy='dynamic')
	
	
	def __repr__(self):
		return '<Thread %r>' % (self.id)
	
	
	@property
	def is_active(self):
		return True
		
	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  #python 3
		
		
	
	
class Reply(db.Model):
	
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	image = db.Column(URLType)
	name = db.Column(db.String(64))
	parent_thread = db.Column(db.Integer, db.ForeignKey('thread.id'))
	
	def __repr__(self):
		return '<Post %r>' % (self.id)
		