import flask

from app import forms

def log():
	log_form = forms.LogForm(flask.request.form)
	if log_form.validate():
		pass
	return flask.redirect(flask.url_for('home'))


def login():
	login_form = forms.LoginForm(flask.request.form)
	if login_form.validate():
		return flask.redirect(flask.url_for('home'))

	return flask.redirect(flask.url_for('index'))