from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ThreadForm(Form):
	name = StringField('name')
	subject = StringField('subject')
	body = TextAreaField('body', validators=[DataRequired()])
	image = FileField('Choose an image')
	