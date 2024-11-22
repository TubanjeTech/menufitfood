import os
from flask import Blueprint, app, render_template, redirect, request, flash, current_app, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
from app.models import Account, Restaurants
from . import db
from .forms import (AddCatForm, AddDCatForm, AddDepartmentForm, CreateRestaurantForm,
                    EditAccountForm, AccountForm, EditCattForm, EditDCattForm,
                    EditDepartmentForm, EditRestaurantForm, EditStaffForm,
                    SALoginForm, StaffForm)

managers = Blueprint('managers', __name__)

@managers.route('/')
def index():
    return render_template('index.html')

@managers.route('/rest-auth')
def restAuth():
    return render_template('manager/restauth.html')

@managers.route('/login', methods=['GET', 'POST'])
def mlogin():
    form = SALoginForm()
    return render_template('manager/login.html', form=form)

@managers.route('/mdashboard', methods=['GET', 'POST'])
def mDashboard():
    accounts = Account.query.all()
    form = AccountForm()
    forms = EditAccountForm()

    if form.validate_on_submit():
        # Extract data from the form
        account_name = form.account_name.data
        owner = form.owner.data
        phone = form.phone.data
        email = form.email.data
        location = form.location.data
        password = form.password.data

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create a new Account instance
        new_account = Account(
            account_name=account_name,
            owner=owner,
            phone=phone,
            email=email,
            location=location,
            password=hashed_password,
            status="Active"  # Default status
        )

        # Save the new account to the database
        try:
            db.session.add(new_account)
            db.session.commit()
            flash("Account successfully created!", "success")
            return redirect(url_for('managers.mDashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", "danger")

    return render_template('manager/dashboard.html', form=form, forms=forms, accounts=accounts)

@managers.route('/edit_account/<int:account_id>', methods=['GET', 'POST'])
def edit_account(account_id):
    # Fetch the account or return 404 if not found
    account = Account.query.get_or_404(account_id)

    # Initialize the form, pre-populated with current account data
    form = EditAccountForm(obj=account)

    if request.method == 'POST' and form.validate_on_submit():
        # Update the account with new values from the form
        form.populate_obj(account)

        try:
            # Commit changes to the database
            db.session.commit()
            flash('Account updated successfully!', 'success')
            return redirect(url_for('managers.mDashboard'))  # Adjust URL if needed
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating account: {e}', 'danger')

    # Render the edit account form
    return render_template('manager/edit_acc.html', form=form, account=account)

@managers.route('/delete_account/<int:account_id>', methods=['POST'])
def delete_account(account_id):
    # Fetch the account to delete using the account_id
    account = Account.query.get_or_404(account_id)
    
    try:
        # Delete the account from the database
        db.session.delete(account)
        db.session.commit()
        
        flash(f"Account '{account.account_name}' has been deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while trying to delete the account.", "danger")
        print(f"Error deleting account: {e}")
    
    # Redirect to the dashboard or account list page
    return redirect(url_for('managers.mDashboard'))

@managers.route('/crudrest', methods=['GET', 'POST'])
def crudrest():
    restaurants = Restaurants.query.all()
    form = CreateRestaurantForm()

    if form.validate_on_submit():
        rest_name = form.rest_name.data
        description = form.description.data
        email = form.email.data
        country_of_res = form.country_of_res.data
        state_or_prov = form.state_or_prov.data
        res_district = form.res_district.data
        account_id = form.account_id.data

        # Handle file upload for logo
        logo = form.logo.data
        logo_path = None  # Default to None if no logo is uploaded

        if logo:
            filename = secure_filename(logo.filename)  # Secure the file name
            upload_folder = os.path.join(current_app.static_folder, 'uploads', 'rest_images')  # Ensure path is inside static
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)  # Create the folder if it doesn't exist
            
            logo_path = os.path.join(upload_folder, filename)  # Full path for saving
            logo.save(logo_path)  # Save the file
            
            # Store the relative path to the logo in the database
            logo_path = f'uploads/rest_images/{filename}'

        # Create a new restaurant entry in the database
        new_restaurant = Restaurants(
            rest_name=rest_name,
            description=description,
            email=email,
            logo=logo_path,  # Save relative path
            country_of_res=country_of_res,
            state_or_prov=state_or_prov,
            res_district=res_district,
            account_id=account_id
        )

        # Add and commit the new restaurant to the database
        db.session.add(new_restaurant)
        db.session.commit()

        flash('Restaurant created successfully!', 'success')  # Flash success message
        return redirect(url_for('managers.crudrest'))  # Redirect back to the same page

    return render_template('manager/crudrest.html', form=form, restaurants=restaurants)


@managers.route('/edit_restaurant/<int:restaurant_id>', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    form = EditRestaurantForm(obj=restaurant)
    
    if form.validate_on_submit():
        # Check if a new logo is uploaded
        if form.logo.data:
            # Secure the file name
            logo_filename = secure_filename(form.logo.data.filename)
            upload_folder = current_app.config['UPLOAD_FOLDERS']['rest']  # Get the 'rest' path defined in the config

            # Ensure the upload folder exists inside static/uploads/
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)  # Create the folder if it doesn't exist
            
            logo_path = os.path.join(upload_folder, logo_filename)  # Define the full file path
            form.logo.data.save(logo_path)  # Save the uploaded file to the specified path

            # Update the restaurant's logo field with the new file name
            restaurant.logo = logo_filename

        # Update other restaurant details (excluding logo, which is already handled)
        form.populate_obj(restaurant)
        
        try:
            db.session.commit()
            flash('Restaurant updated successfully!', 'success')
            return redirect(url_for('managers.mDashboard'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating restaurant.', 'danger')

    return render_template('manager/edit_rest.html', form=form, restaurant=restaurant)

@managers.route('/delete_restaurant/<int:restaurant_id>', methods=['POST'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurants.query.get_or_404(restaurant_id)
    try:
        db.session.delete(restaurant)
        db.session.commit()
        flash('Restaurant deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting restaurant.', 'danger')
    
    return redirect(url_for('managers.mDashboard'))

@managers.route('/staff', methods=['GET', 'POST'])
def staff():
    forms = StaffForm()
    form = EditStaffForm()
    return render_template('manager/staff.html', form=form, forms=forms)

@managers.route('/deps', methods=['GET', 'POST'])
def deps():
    forms = AddDepartmentForm()
    form = EditDepartmentForm()
    return render_template('manager/deps.html', form=form, forms=forms)

@managers.route('/cat', methods=['GET', 'POST'])
def cat():
    forms = AddCatForm()
    form = EditCattForm()
    return render_template('manager/cat.html', form=form, forms=forms)

@managers.route('/dcat', methods=['GET', 'POST'])
def dcat():
    forms = AddDCatForm()
    form = EditDCattForm()
    return render_template('manager/dcat.html', form=form, forms=forms)

@managers.route('/manager-obr-report', methods=['GET', 'POST'])
def lsd_obr_report():
    return render_template('manager/lsd-obr-report.html')

@managers.route('/atr-obr-report', methods=['POST', 'GET'])
def atr_obr_report():
    return render_template('manager/atr-obr-report.html')

@managers.route('/shiftOne', methods=['POST', 'GET'])
def shiftOne():
    return render_template('manager/shift1.html')

@managers.route('/shiftTwo', methods=['POST', 'GET'])
def shiftTwo():
    return render_template('manager/shift2.html')

@managers.route('/stockStatus')
def stockStatus():
    return render_template('manager/stock-status.html')

@managers.route('/myMenu')
def myMenu():
    return render_template('manager/mymenu.html')

@managers.route('/crnt-sup', methods=['POST', 'GET'])
def crnt_sup():
    last_supplies = [
        {'product_name': 'Olive Oil', 'product_type': 'Ingredient', 'quantity': 20, 'price_bought': 50, 'supplier_name': 'Fresh Produce Inc.', 'time_supplied': '2024-11-05 14:30', 'recorded_by': 'Store Manager'},
        {'product_name': 'Beer', 'product_type': 'Ready Product', 'quantity': 100, 'price_bought': 200, 'supplier_name': 'Beverages Ltd.', 'time_supplied': '2024-11-04 12:00', 'recorded_by': 'Restaurant Owner'},
        {'product_name': 'Tomato Sauce', 'product_type': 'Ingredient', 'quantity': 30, 'price_bought': 60, 'supplier_name': 'Condiments Co.', 'time_supplied': '2024-11-03 10:00', 'recorded_by': 'Store Manager'},
        {'product_name': 'Pasta', 'product_type': 'Ingredient', 'quantity': 50, 'price_bought': 40, 'supplier_name': 'Italian Goods', 'time_supplied': '2024-11-02 09:30', 'recorded_by': 'Store Manager'},
        {'product_name': 'Lemonade', 'product_type': 'Ready Product', 'quantity': 200, 'price_bought': 300, 'supplier_name': 'Beverages Ltd.', 'time_supplied': '2024-11-01 11:00', 'recorded_by': 'Restaurant Owner'}
    ]
    return render_template('manager/current-supplies.html', supplies=last_supplies)
