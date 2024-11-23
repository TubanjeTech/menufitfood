from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, IntegerField, SelectField, FileField, DateField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, PasswordField, FileField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Email, EqualTo
from wtforms.validators import DataRequired, Length, Email, Regexp
from flask_wtf.file import FileAllowed, FileRequired

from app.models import Account, Restaurants

class SALoginForm(FlaskForm):
    username = StringField('Enter Username to login', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class StaffLoginForm(FlaskForm):
    # email must be unique
    email = StringField('Enter Email to login', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
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
    menu_type = TextAreaField('Describe your restaurant\'s menu type', validators=[DataRequired()])
    description = TextAreaField('Description of your restaurant', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    logo = FileField('Restaurant Logo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
    ])
    restaurant_profile_image= FileField('Restaurant Profile image', validators=[
    FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
        ])
    country_of_res = StringField('Country of Residence', validators=[DataRequired(), Length(max=100)])
    state_or_prov = StringField('State/Province', validators=[DataRequired(), Length(max=150)])
    res_district = StringField('District', validators=[DataRequired(), Length(max=150)])
    account_id = SelectField('Account', coerce=int, validators=[DataRequired()])

    submit = SubmitField('Create Restaurant')

    def __init__(self, *args, **kwargs):
        super(CreateRestaurantForm, self).__init__(*args, **kwargs)
        # Populate the account options with all accounts from the Account model
        self.account_id.choices = [(account.id, account.account_name) for account in Account.query.all()]

class EditRestaurantForm(FlaskForm):
    rest_name = StringField('Restaurant Name', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=100)])
    logo = FileField('Restaurant Logo', validators=[
    FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
        ])
    restaurant_profile_image= FileField('Restaurant Profile image', validators=[
    FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
        ])
    country_of_res = StringField('Country of Residence', validators=[DataRequired(), Length(max=100)])
    state_or_prov = StringField('State/Province', validators=[DataRequired(), Length(max=150)])
    res_district = StringField('District', validators=[DataRequired(), Length(max=150)])
    
    submit = SubmitField('Edit Restaurant')

class StaffForm(FlaskForm):
    restaurant_id = SelectField('Restaurant Name', coerce=int, validators=[DataRequired()])
    staff_name = StringField('Staff Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Length(max=255)])
    staff_phone = StringField('Phone Number', validators=[
        DataRequired(), Length(max=255), Regexp(r'^\+?[1-9]\d{1,14}$', message="Invalid phone number format.")
    ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    status = SelectField('Status', choices=[('active', 'Active'), ('inactive', 'Inactive')], validators=[DataRequired()])
    role = SelectField('Role', choices=[
        ('Stock_manager', 'Stock Manager'),
        ('waiter', 'Waiter'),
        ('cashier', 'Cashier')
    ], validators=[DataRequired()])
    submit = SubmitField('Add Staff')

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        # Populate restaurant_id choices
        self.restaurant_id.choices = [(r.id, r.rest_name) for r in Restaurants.query.all()]


class EditStaffForm(FlaskForm):
    staff_name = StringField('Staff Name', validators=[
        DataRequired(), Length(max=255)
    ])
    email = StringField('Email', validators=[
        DataRequired(), Email(), Length(max=255)
    ])
    staff_phone = StringField('Phone Number', validators=[
        DataRequired(), Length(max=15),
        Regexp(r'^\+?[1-9]\d{1,14}$', message="Invalid phone number format.")
    ])
    password = PasswordField('Password', validators=[
        Optional(), Length(min=6)  # Optional for editing
    ])
    status = SelectField('Status', choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], validators=[DataRequired()])
    role = SelectField('Role', choices=[
        ('stock_manager', 'Stock Manager'),
        ('waiter', 'Waiter'),
        ('cashier', 'Cashier')
    ], validators=[DataRequired()])
    submit_edit = SubmitField('Edit Staff')


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

    restaurant_id = SelectField('Restaurant Name', coerce=int, validators=[DataRequired()])
    
    submit = SubmitField('Add Dish Category')

    def __init__(self, *args, **kwargs):
        super(AddDCatForm, self).__init__(*args, **kwargs)
        # Populate restaurant_id choices
        self.restaurant_id.choices = [(r.id, r.rest_name) for r in Restaurants.query.all()]



class EditDCattForm(FlaskForm):
    menu_categoryname = StringField(
        'Edit Dish Category Name', 
        validators=[DataRequired(), Length(max=100)]
    )
    
    submit_dcat = SubmitField('Edit Dish Category')