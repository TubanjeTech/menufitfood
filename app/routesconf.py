from flask_login import LoginManager
from .models import Staff


staff_login_manager = LoginManager()

def setup_staff_login_manager(app):
    staff_login_manager.init_app(app)
    staff_login_manager.login_view = 'routes.slogin'
    staff_login_manager.login_message = "Please log in to access this page."
    staff_login_manager.login_message_category = "warning"

    @staff_login_manager.user_loader
    def load_user(staff_id):
        return Staff.query.get(int(staff_id))
