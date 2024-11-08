import time
import os
from flask import Blueprint, current_app, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Staff
from .forms import StaffLoginForm
from . import db


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/about-us')
def aboutUs():
    return render_template('about.html')

@routes.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')

@routes.route('/contact-us')
def contactUs():
    return render_template('contact.html')

@routes.route('/slogin')
def slogin():
    form = StaffLoginForm()
    return render_template('staff/login.html', form=form)

@routes.route('/smDashboard')
def smDashboard():
    return render_template('staff/storemanagerdash.html')

@routes.route('/myMenu')
def myMenu():
    return render_template('staff/mymenu.html')

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

@routes.route('/wdc', methods=['POST', 'GET'])
def mdc():
    return render_template('staff/tables.html')

@routes.route('/adc')
def adc():
    return render_template('staff/cashierdash.html')

@routes.route('/smenu', methods=['POST', 'GET'])
def smenu():
    return render_template('staff/menu.html')
