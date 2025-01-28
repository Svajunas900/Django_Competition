from wtforms import Form, StringField, PasswordField, validators, TextAreaField

class LoginForm(Form):
  username = StringField("Username", [validators.Length(min=4, max=25)])
  password = PasswordField("Password", [validators.Length(min=4, max=25)])


class TemplateForm(Form):
  text = TextAreaField("text")
  