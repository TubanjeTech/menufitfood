from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FileField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, FileField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired

class SALoginForm(FlaskForm):
    username = StringField('Enter Username to login', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class StaffLoginForm(FlaskForm):
    # email must be unique
    email = StringField('Enter Email to login', validators=[InputRequired()])
    staff_code = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class AddStaffForm(FlaskForm):
    username = StringField(
        'Username', 
        validators=[DataRequired(), Length(min=2, max=50)]
    )
    
    gender = SelectField(
        'Gender', 
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], 
        validators=[DataRequired()]
    )
    
    location = StringField(
        'Location', 
        validators=[Optional(), Length(max=100)]
    )
    
    age = IntegerField(
        'Age', 
        validators=[Optional(), NumberRange(min=18, max=70)]
    )
    
    shift = SelectField(
        'Shift', 
        choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Night', 'Night')], 
        validators=[DataRequired()]
    )
    
    working_days = StringField(
        'Working Days', 
        validators=[Optional(), Length(max=50)]
    )
    
    image = FileField(
        'Profile Image', 
        validators=[Optional()]
    )
    
    submit = SubmitField('Submit')
