import datetime
from . import db
from datetime import datetime
from sqlalchemy import (
    Column, Enum, Integer, String, Text, DateTime, Float, ForeignKey, Boolean, func
)
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class Admin(db.Model, UserMixin):
    __tablename__ = 'admin'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(255), nullable=False)
    username = db.Column(String(255), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)
    type = db.Column(String(255), nullable=False)
    status = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True)
    account_id = db.Column(Integer, db.ForeignKey('account.id'), nullable=False)
    firstname = db.Column(String(255), nullable=False)
    lastname = db.Column(String(255), nullable=False)
    email = db.Column(String(255), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)
    role = db.Column(String(255), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Account(db.Model):
    __tablename__ = 'account'
    
    id = db.Column(db.Integer, primary_key=True)  
    account_name = db.Column(db.String(255), nullable=False)  
    owner = db.Column(db.String(255), nullable=False)  
    phone = db.Column(db.String(20), nullable=False)  
    email = db.Column(db.String(255), nullable=False, unique=True)  
    location = db.Column(db.String(255), nullable=False)  
    password = db.Column(db.String(255), nullable=False)  
    status = db.Column(db.String(255), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  
    
    # Relationship with Restaurants (One-to-many: one account can have many restaurants)
    restaurants = db.relationship('Restaurants', back_populates='account', lazy=True)
    
    def __repr__(self):
        return f'<Account {self.account_name}>'


class Restaurants(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    rest_name = db.Column(db.String(100), nullable=False)
    menu_type = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    logo = db.Column(db.String(200), nullable=False)
    country_of_res = db.Column(db.String(100), nullable=False)
    state_or_prov = db.Column(db.String(150), nullable=False)
    res_district = db.Column(db.String(150), nullable=False)
    visited = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())

    # Relationship to the Account model (Many-to-one: each restaurant belongs to one account)
    account = db.relationship('Account', back_populates='restaurants')

    # Relationship with Staff (one-to-many: one restaurant can have many staff members)
    staff = db.relationship('Staff', back_populates='restaurant', lazy=True)

    
class RestaurantType(db.Model):
    __tablename__ = 'restaurant_type'
    id = db.Column(Integer, primary_key=True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    menu_type = db.Column(Text, nullable=False)
    recorded_at = db.Column(DateTime, nullable=False, default=func.now())

class RestaurantDetails(db.Model):
    __tablename__ = 'restaurant_details'
    id = db.Column(Integer, primary_key=True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    details = db.Column(Text, nullable=False)
    logo = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    status = db.Column(Text, nullable=False)

class Assistance(db.Model):
    __tablename__ = 'assistance'
    id = db.Column(Integer, primary_key=True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())
    status = db.Column(Text, nullable=False)

class Departments(db.Model):
    __tablename__ = 'departments'
    id = db.Column(Integer, primary_key=True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    dep_name = db.Column(String(100), nullable=False)
    status = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    staff_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    staff_phone = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now())
    status = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False)
    pin = db.Column(db.Text, nullable=False)

    # Add the relationship to the Restaurants model
    restaurant = db.relationship('Restaurants', back_populates='staff')


class Sales(db.Model):
    __tablename__ = 'sales'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(Integer, db.ForeignKey('account.id'), nullable=False)
    item_id = db.Column(Integer, nullable=False)
    item_name = db.Column(String(255), nullable=False)
    quantity = db.Column(Integer, nullable=False)
    price = db.Column(Float, nullable=False)
    profit = db.Column(Float, nullable=False)
    total_price = db.Column(Float, nullable=False)
    staff = db.Column(String(255), nullable=False)
    status = db.Column(String(255), nullable=False)
    receipt = db.Column(Integer, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    dish_id = db.Column(Integer, db.ForeignKey('dishes.id'), nullable=False)
    ingredient_id = db.Column(Integer, db.ForeignKey('ingredients.id'), nullable=False)
    quantity = db.Column(Integer, nullable=False)
    store = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class ReceiptPrinter(db.Model):
    __tablename__ = 'receipt_printer'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(Integer, nullable=False)
    status = db.Column(Text, nullable=False)

class StoreLogs(db.Model):
    __tablename__ = 'store_logs'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(Integer, nullable=False)
    dish_id = db.Column(Integer, nullable=False)
    store_field = db.Column(Text, nullable=False)
    qty = db.Column(Integer, nullable=False)
    requested = db.Column(Integer, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Stock(db.Model):
    __tablename__ = 'stock'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    dish_id = db.Column(Integer, db.ForeignKey('dishes.id'), nullable=False)
    main = db.Column(Integer, nullable=False)
    main_qty = db.Column(Integer, nullable=False)
    kitchen = db.Column(Integer, nullable=False)
    kitchen_qty = db.Column(Integer, nullable=False)
    bar = db.Column(Integer, nullable=False)
    bar_qty = db.Column(Integer, nullable=False)
    other1 = db.Column(Integer, nullable=False)
    other1_qty = db.Column(Integer, nullable=False)
    other2 = db.Column(Integer, nullable=False)
    other2_qty = db.Column(Integer, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Expenses(db.Model):
    __tablename__ = 'expences'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    item_name = db.Column(Text, nullable=False)
    stock_type = db.Column(Text, nullable=False)
    qty_consumed = db.Column(Integer, nullable=False)
    qty_instock = db.Column(Integer, nullable=False)
    cost = db.Column(Float, nullable=False)
    value = db.Column(Float, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class ReceiptLogs(db.Model):
    __tablename__ = 'receipt_logs'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(Integer, db.ForeignKey('staff.id'), nullable=False)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    receipt_id = db.Column(Integer, db.ForeignKey('receipt.id'), nullable=False)
    amount = db.Column(Float, nullable=False)
    payment_mode = db.Column(Text, nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    receipt_number = db.Column(Integer, nullable=False)
    tableno = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(Integer, db.ForeignKey('restaurants.id'), nullable=False)
    amount = db.Column(Float, nullable=False)
    status = db.Column(Text, nullable=False)
    cashier_id = db.Column(Integer, db.ForeignKey('staff.id'), nullable=False)
    created_at = db.Column(DateTime, nullable=False, default=func.now())

class Proforma(db.Model):
    __tablename__ = 'proforma'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    receipt = db.Column(db.Integer, db.ForeignKey('receipt.id'), nullable=False)  # Foreign key linking to receipt
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key linking to restaurants
    tableno = db.Column(db.Integer, nullable=False)  # Table number associated with the proforma
    amount = db.Column(db.Float, nullable=False)  # Total amount
    status = db.Column(db.Text, nullable=False)  # Status of the proforma
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the proforma was created

class Purchases(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dishes.id'), nullable=False)  # Foreign key to dishes
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of dish purchased
    supplier = db.Column(db.Text, nullable=False)  # Supplier name
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the purchase was made

class PaymentMode(db.Model):
    __tablename__ = 'payment_mode'
    id = db.Column(db.Integer, primary_key=True)
    neworder_id = db.Column(db.Integer, db.ForeignKey('neworder.id'), nullable=False)  # Foreign key to neworder
    mode = db.Column(db.Text, nullable=False)  # Payment mode (e.g., Credit Card, Mpesa, etc.)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the payment mode was created

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    menu_ordered = db.Column(db.String(50), db.ForeignKey('menues.id'), nullable=False)  # Foreign key to menus
    quantity = db.Column(db.Integer, nullable=False) 
    tableno = db.Column(db.Integer, nullable=False)
    ordered_by = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)  # Staff member who placed the order
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to restaurants
    status = db.Column(db.String(20), nullable=False)  # Status of the order (e.g., Pending, Completed)
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the order was created

class NewOrder(db.Model):
    __tablename__ = 'neworder'
    id = db.Column(db.Integer, primary_key=True)
    dish = db.Column(db.String(255), nullable=False)  # Dish being ordered
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to restaurants
    staff = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)  # Staff member who created the order
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the order was created
    status = db.Column(db.String(255), nullable=False)  # Status of the order
    quantity = db.Column(db.Integer, nullable=False)  # Quantity of the dish ordered
    numberofpeople = db.Column(db.Integer, nullable=False)  # Number of people for the order
    tableno = db.Column(db.Text, nullable=False)  # Table number associated with the order
    price = db.Column(db.Integer, nullable=False)  # Price of the dish ordered
    preferences = db.Column(db.Text, nullable=False)  # Customer preferences for the dish
    totalprice = db.Column(db.Integer, nullable=False)  # Total price of the order
    phone = db.Column(db.Integer, nullable=False)  # Customer's phone number
    takeaway_counter = db.Column(db.Integer, nullable=False)  # Counter number for takeaway
    receipt = db.Column(db.Integer, db.ForeignKey('receipt.id'), nullable=False)  # Foreign key to receipt
    seen = db.Column(db.String(255), nullable=False)  # Status whether the order has been seen by the staff
    seen_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the order was seen by staff

class Menues(db.Model):
    __tablename__ = 'menues'
    id = db.Column(db.String(150), primary_key=True)
    dishes_ref = db.Column(db.Integer, db.ForeignKey('dishes.id'), nullable=False)  # Foreign key to dishes
    contents = db.Column(db.Text, nullable=False)  # Menu contents (description of dishes)
    warnings = db.Column(db.Text, nullable=False)  # Any warnings related to dishes
    protein = db.Column(db.Integer, nullable=False)  # Amount of protein in the dish



class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)  # Foreign key to account
    category_name = db.Column(db.String(100), nullable=False, unique=True)  # Unique category name
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the category was created

    items = db.relationship("Item", back_populates="category")

class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)  # Foreign key to account
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)  # Foreign key to category
    item_name = db.Column(db.String(255), nullable=False)  # Name of the item
    img = db.Column(db.String(255), nullable=False)  # Image of the item
    item_description = db.Column(db.Text, nullable=False)  # Description of the item
    qty = db.Column(db.Integer, nullable=False)  # Quantity in stock
    buying = db.Column(db.String(255), nullable=False)  # Buying price or cost of the item
    selling = db.Column(db.String(255), nullable=False)  # Selling price of the item
    reorder = db.Column(db.Integer, nullable=False)  # Reorder level for stock management
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Timestamp when the item was created

    category = db.relationship("Category", back_populates="items")

class Ingredients(db.Model):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    menu = db.Column(db.Integer, nullable=False)  # Menu associated with the ingredient
    name = db.Column(db.String(100), nullable=False)  # Ingredient name
    image = db.Column(db.String(100), nullable=False)  # Image of the ingredient
    created_at = db.Column(db.Integer, nullable=False)  # Timestamp when the ingredient was created

class MenuCategories(db.Model):
    __tablename__ = 'menu_categories'
    id = db.Column(db.Integer, primary_key=True)
    menu_categoryname = db.Column(db.String(100), nullable=False)  # Category name
    icon = db.Column(db.String(30), nullable=False)  # Icon for the category
    visited = db.Column(db.Integer, nullable=False, default=0)  # Number of times visited
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to restaurants
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())  # Created at timestamp

    # Relationships
    dishes = db.relationship('Dishes', backref='menu_category', lazy=True)

class Dishes(db.Model):
    __tablename__ = 'dishes'
    id = db.Column(db.Integer, primary_key=True)
    restaurant = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to restaurants
    dishes_name = db.Column(db.String(100), nullable=False)  # Name of the dish
    menu_categories_id = db.Column(db.Integer, db.ForeignKey('menu_categories.id'), nullable=False)  # Foreign key to menu_categories

    # Enum for menu options
    menu_option = db.Column(Enum('takeaway', 'room', 'direct_table', name='menu_options_enum'), nullable=False)

    price = db.Column(db.Integer, nullable=False)  # Price of the dish
    cost = db.Column(db.Integer, nullable=False)  # Cost of the dish
    description = db.Column(db.String(100), nullable=False)  # Description of the dish
    printer = db.Column(db.String(50), nullable=False)  # Printer assigned to the dish
    weight = db.Column(db.Float, nullable=False)  # Weight of the dish
    portion_size = db.Column(db.String(50), nullable=False)  # Portion size of the dish
    delivery_fee = db.Column(db.Integer, nullable=False)  # Delivery fee for the dish
    created_at = db.Column(db.DateTime, nullable=False, default=func.now()) 


