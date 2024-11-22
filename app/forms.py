from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, IntegerField, SelectField, FileField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, FileField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.validators import DataRequired, Length, Email, Regexp
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

class BackOfficeLoginForm(FlaskForm):
    email = StringField('Enter Email to login', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class NewOrderForm(FlaskForm):
    table_number = IntegerField('Table Number', validators=[DataRequired()])
    number_of_people = IntegerField('Number of People', validators=[DataRequired(), NumberRange(min=1)])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    submit = SubmitField('Submit Order')


# START
class AccountForm(FlaskForm):
    account_name = StringField('Account Name', validators=[DataRequired(), Length(min=2, max=255)])
    owner = StringField('Owner', validators=[DataRequired(), Length(min=2, max=255)])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    location = StringField('Location', validators=[DataRequired(), Length(min=2, max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=255)])
    submit = SubmitField('Submit')

class EditAccountForm(FlaskForm):
    account_name = StringField('Account Name', validators=[DataRequired(), Length(max=100)])
    owner = StringField('Owner', validators=[DataRequired(), Length(max=100)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=15)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    location = StringField('Location', validators=[DataRequired(), Length(max=200)])

    submit = SubmitField('Save Changes')

class CreateRestaurantForm(FlaskForm):
    rest_name = StringField('Restaurant Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    logo = FileField('Restaurant Logo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    country_of_res = StringField('Country of Residence', validators=[DataRequired(), Length(max=100)])
    state_or_prov = StringField('State/Province', validators=[DataRequired(), Length(max=150)])
    res_district = StringField('District', validators=[DataRequired(), Length(max=150)])
    visited = IntegerField('Visited Count', default=0)
    
    submit = SubmitField('Create Restaurant')

class EditRestaurantForm(FlaskForm):
    rest_name = StringField('Restaurant Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    logo = FileField('Restaurant Logo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    country_of_res = StringField('Country of Residence', validators=[DataRequired(), Length(max=100)])
    state_or_prov = StringField('State/Province', validators=[DataRequired(), Length(max=150)])
    res_district = StringField('District', validators=[DataRequired(), Length(max=150)])
    visited = IntegerField('Visited Count', default=0)
    
    submit = SubmitField('Edit Restaurant')

class StaffForm(FlaskForm):
    staff_name = StringField('Staff Name', validators=[
        DataRequired(), Length(max=255)
    ])
    staff_restaurant = StringField('Restaurant', validators=[
        DataRequired(), Length(max=255)
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Length(max=255)
    ])
    staff_phone = StringField('Phone Number', validators=[
        DataRequired(), Length(max=255),
        Regexp(r'^\+?[1-9]\d{1,14}$', message="Invalid phone number format.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6)
    ])
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], validators=[DataRequired()])
    role = SelectField('Role', choices=[
        ('manager', 'Manager'),
        ('waiter', 'Waiter'),
        ('chef', 'Chef')
    ], validators=[DataRequired()])
    pin = StringField('PIN', validators=[
        DataRequired(), Length(min=4, max=8),
        Regexp(r'^\d+$', message="PIN must be numeric.")
    ])
    submit = SubmitField('Add Staff')


class EditStaffForm(FlaskForm):
    staff_name = StringField('Staff Name', validators=[
        DataRequired(), Length(max=255)
    ])
    staff_restaurant = StringField('Restaurant', validators=[
        DataRequired(), Length(max=255)
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Length(max=255)
    ])
    staff_phone = StringField('Phone Number', validators=[
        DataRequired(), Length(max=255),
        Regexp(r'^\+?[1-9]\d{1,14}$', message="Invalid phone number format.")
    ])
    password = PasswordField('Password', validators=[
        Length(min=6),  # Optional in edit form
    ])
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], validators=[DataRequired()])
    role = SelectField('Role', choices=[
        ('manager', 'Manager'),
        ('waiter', 'Waiter'),
        ('chef', 'Chef')
    ], validators=[DataRequired()])
    pin = StringField('PIN', validators=[
        DataRequired(), Length(min=4, max=8),
        Regexp(r'^\d+$', message="PIN must be numeric.")
    ])
    submit = SubmitField('Edit Staff')

class AddDepartmentForm(FlaskForm):
    dep_name = StringField(
        'Department Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Add Department')

class EditDepartmentForm(FlaskForm):
    dep_name = StringField(
        'Department Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Edit Department')
    
class AddCatForm(FlaskForm):
    category_name = StringField(
        'Category Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Add Category')

class EditCattForm(FlaskForm):
    category_name = StringField(
        'Category Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Edit Category')

class AddDCatForm(FlaskForm):
    menu_categoryname = StringField(
        'Add Dish Category Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    icon = StringField(
        'Add Dish Category Icon', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Add Dish Category')

class EditDCattForm(FlaskForm):
    menu_categoryname = StringField(
        'Edit Dish Category Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    icon = StringField(
        'Add Dish Category Icon', 
        validators=[DataRequired(), Length(max=100)]
    )
    submit = SubmitField('Edit Dish Category')