import flask

from app import forms

def log():
	log_form = forms.LogForm(flask.request.form)
	if log_form.validate():
		pass
	return flask.redirect(flask.url_for('home'))
