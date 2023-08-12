import wtforms

from wtforms import validators
from wtforms.fields import DateField, StringField, PasswordField, IntegerField


class LogForm(wtforms.form.Form):
    log_text = StringField("Log", [validators.InputRequired()])
    quantity = IntegerField("Quantity", [validators.Optional()])
    date = DateField("Date", [validators.InputRequired()])
