from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import time
import os
from flask import Blueprint, current_app, jsonify, render_template, redirect, request, session, url_for, flash, g
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Account, Restaurants, Staff
from .forms import StaffLoginForm, NewOrderForm, BackOfficeLoginForm
from . import db
from flask_socketio import SocketIO, emit


routes = Blueprint('routes', __name__)

def check_inactive_accounts():
    three_days_ago = datetime.utcnow() - timedelta(days=3)
    inactive_accounts = Account.query.filter(
        Account.last_login < three_days_ago,
        Account.status != "Inactive"
    ).all()

    for account in inactive_accounts:
        account.status = "Inactive"

    db.session.commit()
    print(f"Checked and updated {len(inactive_accounts)} inactive accounts.")

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(check_inactive_accounts, 'interval', hours=24)  # Run every 24 hours
scheduler.start()

@routes.route('/load_more_restaurants', methods=['POST'])
def load_more_restaurants():
    offset = int(request.json.get('offset', 0))  # Offset for pagination
    limit = 6
    restaurants = Restaurants.query.offset(offset).limit(limit).all()  # Fetch restaurants with offset and limit
    
    restaurants_data = [
        {
            "id": restaurant.id,
            "name": restaurant.rest_name,
            "description": restaurant.description,
            "image_url": url_for('static', filename=restaurant.restaurant_profile_image)  # Reference the saved path
        }
        for restaurant in restaurants
    ]
    return jsonify(restaurants=restaurants_data)

@routes.route('/')
def index():
    restaurants = Restaurants.query.limit(6).all()  
    return render_template('index.html', restaurants=restaurants)

@routes.route('/about-us')
def aboutUs():
    return render_template('about.html')

@routes.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

@routes.route('/contact-us')
def contactUs():
    return render_template('contact.html')

@routes.route('/slogin', methods=['GET', 'POST'])
def slogin():
    form = StaffLoginForm()
    if form.validate_on_submit():
        staff = Staff.query.filter_by(email=form.email.data).first()
        if staff and check_password_hash(staff.password, form.password.data):
            # Use Flask-Login to log in the user
            login_user(staff)
            
            # Store additional session data, if needed
            session['rest_name'] = staff.restaurant.rest_name
            
            flash(f"Welcome {staff.staff_name}!", "success")
            return redirect(url_for('routes.home'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('staff/login.html', form=form)


@routes.route('/slogout')
@login_required
def slogout():
    # Logout the user
    logout_user()
    # Clear additional session data
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('routes.slogin'))

@routes.route('/alogin', methods=['GET', 'POST'])
def alogin():
    form = BackOfficeLoginForm()
    if form.validate_on_submit():
        # Query the account by email
        account = Account.query.filter_by(email=form.email.data).first()
        
        if account and check_password_hash(account.password, form.password.data):
            # Update last_login and status
            account.last_login = datetime.utcnow()
            account.status = "Active"
            db.session.commit()

            # Store account ID in session
            session['account_id'] = account.id
            flash("Login successful!", "success")
            return redirect(url_for('routes.backoffice'))
        else:
            flash("Invalid email or password.", "danger")
    return render_template('staff/account_login.html', form=form)


@routes.route('/backoffice')
def backoffice():
    if 'account_id' in session:
        # Fetch the logged-in account details
        account = Account.query.get(session['account_id'])
        
        if account:
            return render_template('staff/backoffice.html', account=account)
    
    flash("Please log in to access this page.", "danger")
    return redirect(url_for('managers.login'))


@routes.route('/smDashboard')
def smDashboard():
    return render_template('staff/storemanagerdash.html')

@routes.route('/home')
@login_required
def home():
    form = BackOfficeLoginForm()
    
    # Use Flask-Login's `current_user`
    staff = current_user.staff_name
    rest_name = session.get('rest_name', 'Unknown Restaurant')

    return render_template('staff/home.html', form=form, staff=staff, rest_name=rest_name)

@routes.route('/tables', methods=['POST', 'GET'])
@login_required
def tables():
    tables = [i + 1 for i in range(30)]
     # Fetch staff name from the session
    staff_name = session.get('staff_name', 'Unknown Staff')

    return render_template('staff/tables.html', tables=tables, staff_name=staff_name)

@routes.route('/staff')
def staff_list():
    staff_members = Staff.query.all()
    return render_template('staff/list.html', staff=staff_members)


@routes.route('/smenu', methods=['POST', 'GET'])
@login_required
def smenu():
    table_number = request.args.get('table_number')  # Get the table number from query parameters
    staff_name = session.get('staff_name', 'Unknown Staff')

    return render_template('staff/menu.html', table_number=table_number, staff_name=staff_name)

@routes.route('/vieworder')
@login_required
def vieworder():
    form = BackOfficeLoginForm()
    return render_template('staff/vieworder.html', form=form)

@routes.route('/backofflogin')
@login_required
def backofflogin():
    form = BackOfficeLoginForm()
    return render_template('staff/backofflogin.html', form=form)

@routes.route('/neworder')
def neworder():
    form = NewOrderForm()
    return render_template('staff/neworder.html', form=form)

@routes.route('/allorders')
def allorders():
    return render_template('staff/allorders.html')

@routes.route('/alldishes')
def alldishes():
    return render_template('staff/alldishes.html')

@routes.route('/cat')
def cat():
    return render_template('staff/categories.html')

@routes.route('/expe')
def expe():
    return render_template('staff/expense.html')

@routes.route('/tkaw')
def tkaw():
    return render_template('staff/takeaways.html')

@routes.route('/stockStatus')
def stockStatus():
    return render_template('staff/stock-status.html')

@routes.route('/crnt-supply')
def crnt_supply():
    last_supplies = [
        {'product_name': 'Olive Oil', 'product_type': 'Ingredient', 'quantity': 20, 'price_bought': 50, 'supplier_name': 'Fresh Produce Inc.', 'time_supplied': '2024-11-05 14:30', 'recorded_by': 'Store Manager'},
        {'product_name': 'Beer', 'product_type': 'Ready Product', 'quantity': 100, 'price_bought': 200, 'supplier_name': 'Beverages Ltd.', 'time_supplied': '2024-11-04 12:00', 'recorded_by': 'Restaurant Owner'},
        {'product_name': 'Tomato Sauce', 'product_type': 'Ingredient', 'quantity': 30, 'price_bought': 60, 'supplier_name': 'Condiments Co.', 'time_supplied': '2024-11-03 10:00', 'recorded_by': 'Store Manager'},
        {'product_name': 'Pasta', 'product_type': 'Ingredient', 'quantity': 50, 'price_bought': 40, 'supplier_name': 'Italian Goods', 'time_supplied': '2024-11-02 09:30', 'recorded_by': 'Store Manager'},
        {'product_name': 'Soda', 'product_type': 'Ready Product', 'quantity': 200, 'price_bought': 150, 'supplier_name': 'Beverages Ltd.', 'time_supplied': '2024-11-01 14:00', 'recorded_by': 'Restaurant Owner'},
        {'product_name': 'Bottled Water', 'product_type': 'Ready Product', 'quantity': 300, 'price_bought': 100, 'supplier_name': 'Aqua Suppliers', 'time_supplied': '2024-10-31 16:00', 'recorded_by': 'Store Manager'},
        {'product_name': 'Cheese', 'product_type': 'Ingredient', 'quantity': 25, 'price_bought': 75, 'supplier_name': 'Dairy Farmers', 'time_supplied': '2024-10-30 11:00', 'recorded_by': 'Store Manager'},
        {'product_name': 'Wine', 'product_type': 'Ready Product', 'quantity': 50, 'price_bought': 500, 'supplier_name': 'Vineyard Co.', 'time_supplied': '2024-10-29 15:30', 'recorded_by': 'Restaurant Owner'},
        {'product_name': 'Chicken', 'product_type': 'Ingredient', 'quantity': 40, 'price_bought': 200, 'supplier_name': 'Poultry Farms', 'time_supplied': '2024-10-28 13:00', 'recorded_by': 'Store Manager'},
        {'product_name': 'Flour', 'product_type': 'Ingredient', 'quantity': 100, 'price_bought': 50, 'supplier_name': 'Grain Suppliers', 'time_supplied': '2024-10-27 10:30', 'recorded_by': 'Store Manager'}
    ]
    return render_template('staff/crnt-sup.html', last_supplies=last_supplies)


@routes.route('/team')
def team():
    return render_template('staff/+staff.html')

@routes.route('/adc')
def adc():
    return render_template('staff/cashierdash.html')

@routes.route('/order')
def order():
    return render_template('staff/order.html')

@routes.route('/bill')
def bill():
    return render_template('staff/bill.html')

@routes.route('/receipt')
def receipt():
    return render_template('staff/receipt.html')
