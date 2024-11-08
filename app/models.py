from flask_sqlalchemy import SQLAlchemy
from . import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer, primary_key=True)
    fnam = db.Column(db.String(50), nullable=False)  # First name
    lname = db.Column(db.String(50), nullable=False)  # Last name
    email = db.Column(db.String(100), unique=True, nullable=False)  # Email address (unique)
    phone_no = db.Column(db.String(15), nullable=False)  # Phone number
    address = db.Column(db.String(255))  # Address
    profile_image = db.Column(db.String(255))  # Path or URL to profile image
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the owner joined
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for updates

    def __init__(self, fnam, lname, email, phone_no, address, profile_image):
        self.fnam = fnam
        self.lname = lname
        self.email = email
        self.phone_no = phone_no
        self.address = address
        self.profile_image = profile_image

    def __repr__(self):
        return f"<Owner {self.fnam} {self.lname} (ID: {self.id})>"

        
class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    biography = db.Column(db.Text)  # A brief overview of the restaurant
    description = db.Column(db.Text)  # Detailed description of the restaurant
    contact_no = db.Column(db.String(15))  # Contact number
    email = db.Column(db.String(100), unique=True)  # Email address
    web_url = db.Column(db.String(255))  # Website URL
    address = db.Column(db.String(255))  # Street address
    city = db.Column(db.String(100))  # City name
    state = db.Column(db.String(100))  # State or province
    zip_code = db.Column(db.String(20))  # Postal or ZIP code
    latitude = db.Column(db.Float)  # Latitude for location
    longitude = db.Column(db.Float)  # Longitude for location
    est_year = db.Column(db.Integer)  # Year established
    opening_hrs = db.Column(db.Time)  # Opening hours (time)
    closing_hrs = db.Column(db.Time)  # Closing hours (time)
    days_open = db.Column(db.String(50))  # Comma-separated list of days open (e.g., "Mon,Tue,Wed")
    rest_rating = db.Column(db.Float, default=0)  # Rating (0-5 scale)
    image = db.Column(db.String(255))  # Path or URL to restaurant image
    logo = db.Column(db.String(255))  # Path or URL to restaurant logo
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'), nullable=False)  # Foreign key to owner
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for creation
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for updates

    def __init__(self, name, biography, description, contact_no, email, web_url, address, city, state,
                 zip_code, latitude, longitude, est_year, opening_hrs, closing_hrs, days_open,
                 rest_rating, image, logo, owner_id):
        self.name = name
        self.biography = biography
        self.description = description
        self.contact_no = contact_no
        self.email = email
        self.web_url = web_url
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.latitude = latitude
        self.longitude = longitude
        self.est_year = est_year
        self.opening_hrs = opening_hrs
        self.closing_hrs = closing_hrs
        self.days_open = days_open
        self.rest_rating = rest_rating
        self.image = image
        self.logo = logo
        self.owner_id = owner_id

    def __repr__(self):
        return f"<Restaurant {self.name} (ID: {self.id})>"

class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each staff member
    username = db.Column(db.String(50), unique=True, nullable=False)  # Username (must be unique)
    staffcode = db.Column(db.String(20), unique=True, nullable=False)  # Unique staff code
    gender = db.Column(db.String(10))  # Gender of the staff
    location = db.Column(db.String(100))  # Location of the staff member
    age = db.Column(db.Integer)  # Age of the staff member
    shift = db.Column(db.String(50))  # Shift assigned to the staff
    working_days = db.Column(db.String(50))  # Days of the week the staff is scheduled to work
    role = db.Column(db.String(50))  # Role of the staff (e.g., waiter, manager)
    image = db.Column(db.String(255))  # Path or URL to the staff member's image
    registered_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the staff was registered
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to the restaurant

    restaurant = db.relationship('Restaurant', backref=db.backref('staff', lazy=True))  # Relationship to the Restaurant model

    def __init__(self, username, staffcode, gender, location, age, shift, working_days, role, image, restaurant_id):
        self.username = username
        self.staffcode = staffcode
        self.gender = gender
        self.location = location
        self.age = age
        self.shift = shift
        self.working_days = working_days
        self.role = role
        self.image = image
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f"<Staff {self.username} (ID: {self.id})>"

class Supplier(db.Model):
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each supplier
    sup_name = db.Column(db.String(100), nullable=False)  # Name of the supplier (required)
    phone_no = db.Column(db.String(15))  # Phone number of the supplier
    email = db.Column(db.String(100), unique=True)  # Email of the supplier (must be unique)
    location = db.Column(db.String(100))  # Location of the supplier
    city = db.Column(db.String(50))  # City of the supplier
    state = db.Column(db.String(50))  # State of the supplier
    created_by = db.Column(db.String(100))  # Who created the supplier entry (could be username or staff name)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to the restaurant
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the supplier was created
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  # Timestamp for last update

    restaurant = db.relationship('Restaurant', backref=db.backref('suppliers', lazy=True))  # Relationship to the Restaurant model

    def __init__(self, sup_name, phone_no, email, location, city, state, created_by, restaurant_id):
        self.sup_name = sup_name
        self.phone_no = phone_no
        self.email = email
        self.location = location
        self.city = city
        self.state = state
        self.created_by = created_by
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f"<Supplier {self.sup_name} (ID: {self.id})>"


class Supply(db.Model):
    __tablename__ = 'supplies'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each supply entry
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'), nullable=False)  # Foreign key to the Supplier
    recorded_by = db.Column(db.String(100), nullable=False)  # Who recorded the supply
    delivery_date = db.Column(db.DateTime, nullable=False)  # Date of delivery
    total_cost = db.Column(db.Float, nullable=False)  # Total cost of the supplies
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the supply entry was created

    # Relationship to the Supplier model
    supplier = db.relationship('Supplier', backref=db.backref('supplies', lazy=True))

    def __init__(self, supplier_id, recorded_by, delivery_date, total_cost):
        self.supplier_id = supplier_id
        self.recorded_by = recorded_by
        self.delivery_date = delivery_date
        self.total_cost = total_cost

    def __repr__(self):
        return f"<Supply ID: {self.id}, Supplier ID: {self.supplier_id}>"


class SupplyItem(db.Model):
    __tablename__ = 'supply_items'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each supply item
    supply_id = db.Column(db.Integer, db.ForeignKey('supplies.id'), nullable=False)  # Foreign key to the Supply
    item_name = db.Column(db.String(100), nullable=False)  # Name of the supply item
    quantity = db.Column(db.Float, nullable=False)  # Quantity of the supply item
    price_per_unit = db.Column(db.Float, nullable=False)  # Price per unit of the supply item
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the item entry was created

    # Relationship to the Supply model
    supply = db.relationship('Supply', backref=db.backref('items', lazy=True))

    def __init__(self, supply_id, item_name, quantity, price_per_unit):
        self.supply_id = supply_id
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __repr__(self):
        return f"<SupplyItem ID: {self.id}, Item: {self.item_name}, Quantity: {self.quantity}>"


class MenuItemCategory(db.Model):
    __tablename__ = 'menu_item_categories'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each category
    categ_name = db.Column(db.String(100), nullable=False)  # Name of the category
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the category was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for when the category was last updated

    def __init__(self, categ_name):
        self.categ_name = categ_name

    def __repr__(self):
        return f"<MenuItemCategory ID: {self.id}, Name: {self.categ_name}>"


class MenuItem(db.Model):
    __tablename__ = 'menu_items'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each menu item
    item_name = db.Column(db.String(100), nullable=False)  # Name of the menu item
    item_type = db.Column(db.String(50), nullable=False)  # Type of item (e.g., Ready product or Prepared Product)
    quantity = db.Column(db.Float, nullable=True)  # Quantity for ready products
    ingredients = db.Column(db.Text, nullable=True)  # List of ingredients for prepared products
    nutrition = db.Column(db.Text, nullable=True)  # Nutritional information
    ana_status = db.Column(db.String(20), nullable=False)  # Availability status (available or unavailable)
    ana_status_rsn = db.Column(db.String(255), nullable=True)  # Reason for unavailability
    ana_status_timeshot = db.Column(db.DateTime, nullable=True)  # Timestamp when the status was marked unavailable
    price = db.Column(db.Float, nullable=False)  # Price of the menu item
    menu_category = db.Column(db.Integer, db.ForeignKey('menu_item_categories.id'), nullable=False)  # Foreign key to menu item category
    printer_opt = db.Column(db.String(50), nullable=True)  # Printer option (e.g., kitchen, bar)
    department = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)  # Department the menu item belongs to
    updated_on = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for last update
    created_on = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the item was created

    # Relationship to the MenuItemCategory model
    category = db.relationship('MenuItemCategory', backref=db.backref('menu_items', lazy=True))
    department = db.relationship('Department', backref=db.backref('menu_items', lazy=True))

    def __init__(self, item_name, item_type, quantity, ingredients, nutrition, ana_status, price, menu_category, printer_opt, department):
        self.item_name = item_name
        self.item_type = item_type
        self.quantity = quantity
        self.ingredients = ingredients
        self.nutrition = nutrition
        self.ana_status = ana_status
        self.price = price
        self.menu_category = menu_category
        self.printer_opt = printer_opt
        self.department = department

    def __repr__(self):
        return f"<MenuItem ID: {self.id}, Name: {self.item_name}>"


class Department(db.Model):
    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each department
    categ_name = db.Column(db.String(100), nullable=False)  # Name of the department
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key to the restaurant
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the department was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for when the department was last updated

    # Relationship to the Restaurant model
    restaurant = db.relationship('Restaurant', backref=db.backref('departments', lazy=True))

    def __init__(self, categ_name, restaurant_id):
        self.categ_name = categ_name
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return f"<Department ID: {self.id}, Name: {self.categ_name}>"


class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each ingredient
    name = db.Column(db.String(100), nullable=False)  # Name of the ingredient
    quantity = db.Column(db.Float, nullable=True)  # Quantity of the ingredient available
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the ingredient was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for when the ingredient was last updated

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __repr__(self):
        return f"<Ingredient ID: {self.id}, Name: {self.name}>"


class MenuItemIngredient(db.Model):
    __tablename__ = 'menu_item_ingredients'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each menu item ingredient
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)  # Foreign key to the ingredient
    quantity = db.Column(db.Float, nullable=False)  # Quantity of the ingredient used in the menu item

    # Relationships
    menu_item = db.relationship('MenuItem', backref=db.backref('menu_item_ingredients', lazy=True))

    def __init__(self, menu_item_id, quantity):
        self.menu_item_id = menu_item_id
        self.quantity = quantity

    def __repr__(self):
        return f"<MenuItemIngredient ID: {self.id}, Menu Item ID: {self.menu_item_id}>"


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each order
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)  # Foreign key referencing the waiter handling the order
    table_id = db.Column(db.Integer, nullable=False)  # Identifier for the table where the order is placed
    menu_items = db.Column(db.JSON, nullable=False)  
    total_amount = db.Column(db.Numeric(10, 2), nullable=False) 
    item_preference = db.Column(db.Text, nullable=True)  # Special preferences or requests for items
    status = db.Column(db.String(10), nullable=False)  # Status of the payment ("paid" or "not paid")
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key linking to the restaurant
    order_time = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the order was placed
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for when the order was last updated
    discount = db.Column(db.Numeric(5, 2), nullable=True)  # Discount applied to the total amount
    payment_method = db.Column(db.String(10), nullable=True)  # Payment method used (e.g., "card", "cash", "mpesa")
    paid_at = db.Column(db.DateTime, nullable=True)  # Timestamp for when the payment was made

    # Relationships
    staff = db.relationship('Staff', backref='orders')
    restaurant = db.relationship('Restaurant', backref='orders')

    def __init__(self, staff_id, table_id, menu_items, total_amount, item_preference, status, restaurant_id, discount=None, payment_method=None):
        self.staff_id = staff_id
        self.table_id = table_id
        self.menu_items = menu_items
        self.total_amount = total_amount
        self.item_preference = item_preference
        self.status = status
        self.restaurant_id = restaurant_id
        self.discount = discount
        self.payment_method = payment_method

    def __repr__(self):
        return f"<Order ID: {self.id}, Status: {self.status}>"


class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each bill
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False) 
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipts.id'), nullable=False)
    bill_number = db.Column(db.String(20), unique=True, nullable=False)  # Unique bill number for reference
    total_before_discount = db.Column(db.Numeric(10, 2), nullable=False)  # Sum total of all item prices before discount
    discount = db.Column(db.Numeric(5, 2), nullable=True)  # Discount amount applied to the bill
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)  # Total amount after applying the discount
    tax = db.Column(db.Numeric(5, 2), nullable=True)  # Tax applied to the bill
    total_due = db.Column(db.Numeric(10, 2), nullable=False)  # Final amount to be paid (after discount and tax)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the bill was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for last update to the bill

    # Relationships
    order = db.relationship('Order', backref='bills')
    receipt = db.relationship('Order', backref='receipts')

    def __init__(self, order_id, receipt_id, bill_number, total_before_discount, discount, total_amount, tax, total_due):
        self.order_id = order_id
        self.receipt_id = receipt_id
        self.bill_number = bill_number
        self.total_before_discount = total_before_discount
        self.discount = discount
        self.total_amount = total_amount
        self.tax = tax
        self.total_due = total_due

    def __repr__(self):
        return f"<Bill ID: {self.id}, Bill Number: {self.bill_number}>"


class Receipt(db.Model):
    __tablename__ = 'receipts'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each receipt
    receipt_number = db.Column(db.String(20), unique=True, nullable=False)  # Unique receipt number for reference
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)  # Foreign key linking to the related order
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)  # Foreign key linking to the related restaurant
    table_number = db.Column(db.Integer, nullable=False)  # Table number associated with the order
    date_of_order = db.Column(db.Date, nullable=False)  # Date when the order was placed
    time_of_order = db.Column(db.Time, nullable=False)  # Time when the order was placed
    items = db.Column(db.JSON, nullable=False)  # JSON array storing item details
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)  # Total amount for the order
    payment_method = db.Column(db.String(10), nullable=True)  # Payment method used
    discount = db.Column(db.Numeric(5, 2), nullable=True)  # Discount applied to the order
    served_by = db.Column(db.String(50), nullable=False)  # Name of the waiter who served the order
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the receipt was generated
    restaurant_logo = db.Column(db.LargeBinary, nullable=True)  # Binary data to store the restaurant's logo
    restaurant_name = db.Column(db.String(100), nullable=False)  # Name of the restaurant
    restaurant_tel = db.Column(db.String(15), nullable=False)  # Restaurant's contact telephone number
    city = db.Column(db.String(50), nullable=False)  # City location of the restaurant
    country = db.Column(db.String(50), nullable=False)  # Country location of the restaurant
    barcode = db.Column(db.String(50), nullable=True)  # Barcode for the order
    footer_text = db.Column(db.Text, default='Thank you')  # Footer message on the receipt

    # Relationships
    order = db.relationship('Order', backref='receipts')
    restaurant = db.relationship('Restaurant', backref='receipts')

    def __init__(self, receipt_number, order_id, restaurant_id, table_number, date_of_order, time_of_order, items, total_amount, payment_method, discount, served_by, restaurant_name, restaurant_tel, city, country, barcode, footer_text):
        self.receipt_number = receipt_number
        self.order_id = order_id
        self.restaurant_id = restaurant_id
        self.table_number = table_number
        self.date_of_order = date_of_order
        self.time_of_order = time_of_order
        self.items = items
        self.total_amount = total_amount
        self.payment_method = payment_method
        self.discount = discount
        self.served_by = served_by
        self.restaurant_name = restaurant_name
        self.restaurant_tel = restaurant_tel
        self.city = city
        self.country = country
        self.barcode = barcode
        self.footer_text = footer_text

    def __repr__(self):
        return f"<Receipt ID: {self.id}, Receipt Number: {self.receipt_number}>"


class OrderNotification(db.Model):
    __tablename__ = 'order_notifications'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each notification
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)  # Foreign key linking to the related order
    message = db.Column(db.Text, nullable=False)  # Notification message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the notification was created
    is_read = db.Column(db.Boolean, default=False)  # Status indicating if the notification has been read

    # Relationships
    order = db.relationship('Order', backref='order_notifications')

    def __init__(self, order_id, message):
        self.order_id = order_id
        self.message = message

    def __repr__(self):
        return f"<OrderNotification ID: {self.id}, Order ID: {self.order_id}>"


class ReceiptNotification(db.Model):
    __tablename__ = 'receipt_notifications'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each notification
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipts.id'), nullable=False)  # Foreign key linking to the related receipt
    message = db.Column(db.Text, nullable=False)  # Notification message
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the notification was created
    is_read = db.Column(db.Boolean, default=False)  # Status indicating if the notification has been read

    # Relationships
    receipt = db.relationship('Receipt', backref='receipt_notifications')

    def __init__(self, receipt_id, message):
        self.receipt_id = receipt_id
        self.message = message

    def __repr__(self):
        return f"<ReceiptNotification ID: {self.id}, Receipt ID: {self.receipt_id}>"


class Offers(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each offer
    title = db.Column(db.String(100), nullable=False)  # Title of the offer
    description = db.Column(db.Text, nullable=False)  # Description of the offer
    discount_percentage = db.Column(db.Numeric(5, 2), nullable=False)  # Discount percentage for the offer
    start_date = db.Column(db.DateTime, nullable=False)  # Start date of the offer
    end_date = db.Column(db.DateTime, nullable=False)  # End date of the offer
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the offer was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for the last update to the offer

    def __init__(self, title, description, discount_percentage, start_date, end_date):
        self.title = title
        self.description = description
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def __repr__(self):
        return f"<Offer ID: {self.id}, Title: {self.title}>"


class OfferOrders(db.Model):
    __tablename__ = 'offer_orders'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each offer order
    offer_id = db.Column(db.Integer, db.ForeignKey('offers.id'), nullable=False)  # Foreign key linking to the related offer
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)  # Foreign key linking to the related order
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the offer order was created

    # Relationships
    offer = db.relationship('Offers', backref='offer_orders')
    order = db.relationship('Order', backref='offer_orders')

    def __init__(self, offer_id, order_id):
        self.offer_id = offer_id
        self.order_id = order_id

    def __repr__(self):
        return f"<OfferOrder ID: {self.id}, Offer ID: {self.offer_id}, Order ID: {self.order_id}>"


class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each event
    title = db.Column(db.String(100), nullable=False)  # Title of the event
    description = db.Column(db.Text, nullable=False)  # Description of the event
    event_date = db.Column(db.DateTime, nullable=False)  # Date and time of the event
    location = db.Column(db.String(200), nullable=False)  # Location of the event
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the event was created
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)  # Timestamp for the last update to the event

    def __init__(self, title, description, event_date, location):
        self.title = title
        self.description = description
        self.event_date = event_date
        self.location = location

    def __repr__(self):
        return f"<Event ID: {self.id}, Title: {self.title}>"



class EventApplications(db.Model):
    __tablename__ = 'event_applications'

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each event application
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)  # Foreign key linking to the related event
    applicant_name = db.Column(db.String(100), nullable=False)  # Name of the applicant
    applicant_email = db.Column(db.String(100), nullable=False)  # Email of the applicant
    application_date = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for when the application was submitted
    status = db.Column(db.String(20), default='pending')  # Status of the application (e.g., 'pending', 'approved', 'rejected')

    # Relationships
    event = db.relationship('Events', backref='event_applications')

    def __init__(self, event_id, applicant_name, applicant_email):
        self.event_id = event_id
        self.applicant_name = applicant_name
        self.applicant_email = applicant_email

    def __repr__(self):
        return f"<EventApplication ID: {self.id}, Event ID: {self.event_id}, Applicant: {self.applicant_name}>"

