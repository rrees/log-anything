import wtforms

from wtforms import validators
from wtforms.fields import DateField, StringField, PasswordField


class LogForm(wtforms.form.Form):
	log_text = StringField('Log', [validators.required()])
	log_date = DateField('Date', [validators.required()])


class LoginForm(wtforms.form.Form):
	username = StringField('Username', [validators.required()])
	password = PasswordField('Password', [validators.required()])