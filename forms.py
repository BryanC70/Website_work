from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import secrets

class RegistrationForm(FlaskForm):
#username = StringField('Username')
#email = StringField('Email')
#password = PasswordField('Password')
#confirm_password = PasswordField('Confirm Password')

  username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])

  email = StringField('Email',
                      validators=[DataRequired(), Email()])

  password = PasswordField('Password', validators=[DataRequired()])

  confirm_password = PasswordField('Confirm Password',
                                  validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  print(secrets.token_hex(16))