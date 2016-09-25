import os
from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .forms import ThreadForm
from .models import Thread, Reply
from datetime import datetime
from werkzeug.utils import secure_filename
								
				
@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
	posts = Thread.query.from_self().paginate(page, POSTS_PER_PAGE, False)

	return render_template('index.html',
						   title='Home',
						   posts=posts)						
	

@app.route('/thread', methods=['GET', 'POST'])
@app.route('/thread/<int:page>', methods=['GET', 'POST'])
def post(page=1):
	form = ThreadForm()
	if form.validate_on_submit():
		
		if form.image.has_file():
			filename = secure_filename(form.image.data.filename)
			form.image.data.save('app/static/img/' + filename)
		else:
			filename = None
		
		
		username = form.name.data
		
		if username is None or username == "":
			username = 'Anonymous'
			
		thread = Thread(popularity=1, subject=form.subject.data, name=username, image=filename, body=form.body.data, 
						timestamp=datetime.utcnow())
		db.session.add(thread)
		db.session.commit()
		flash('Submission successful!')
		return redirect(url_for('index'))
		
	posts = Thread.query.from_self().paginate(page, POSTS_PER_PAGE, False)
	
	return render_template('thread.html',
						   title='Start a new thread',
						   form=form,
						   posts=posts,)
						   

		
@app.route('/reply/<int:id>', methods=['GET', 'POST'])
def reply(id=1):
	form = ThreadForm()
	if form.validate_on_submit():
		
		if form.image.has_file():
			filename = secure_filename(form.image.data.filename)
			form.image.data.save('app/static/img/' + filename)
		else:
			filename = None
		
		
		username = form.name.data
		
		if username is None or username == "":
			username = 'Anonymous'
			
		reply = Reply(name=username, image=filename, body=form.body.data, parent_thread=id,
						timestamp=datetime.utcnow())
		db.session.add(reply)
		db.session.commit()
		flash('Submission successful!')
		return redirect(url_for('reply', id=id))
		
	post = Thread.query.get(id)
	
	return render_template('reply.html',
						   title='Reply here',
						   form=form,
						   post=post
						   )
						   
						   
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

	
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500