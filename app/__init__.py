import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, emit


# Initialize SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = '187199737472396ekm&&65782fyfvd87tg8g8w7tg8wgg8g44ujb987ybd09nghf12fhg34vv5hvhjj86vgcvg%&vgc8yvh8y7frd4xc8ltc'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:37472396@localhost/letsgomff'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Upload folders configuration
    app.config['UPLOAD_FOLDERS'] = {
        'rest': os.path.join(app.static_folder, 'uploads', 'rest_images'),
        'menu': os.path.join(app.static_folder, 'uploads', 'menu_media'),
        'staff': os.path.join(app.static_folder, 'uploads', 'staff_images'),
    }

    # Ensure upload folders exist
    for folder in app.config['UPLOAD_FOLDERS'].values():
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    

    # Import and setup login managers
    from .routesconf import setup_staff_login_manager
    # from .managerconf import setup_managers_login_manager
    # from .adminconf import setup_admin_login_manager

    setup_staff_login_manager(app)
    # setup_admin_login_manager(app)
    # setup_managers_login_manager(app)

    # Register blueprints
    from .routes import routes as main_blueprint
    from .managers import managers as manager_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(manager_blueprint, url_prefix='/manager')
    
    from .models import Account, User, Restaurants, RestaurantType, RestaurantDetails, Assistance, Staff, Sales, Recipe, ReceiptPrinter, StoreLogs, Stock, Expenses, ReceiptLogs, Receipt, Proforma, Purchases, PaymentMode, Orders, NewOrder, Menues, Item


    return app
