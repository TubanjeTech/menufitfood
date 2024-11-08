from flask_login import LoginManager
from .models import Owner

managers_login_manager = LoginManager()

def setup_managers_login_manager(app):
    managers_login_manager.init_app(app)
    managers_login_manager.login_view = 'manager.mlogin'

    @managers_login_manager.user_loader
    def load_super_admin(super_admin_id):
       
        return Owner.query.get(int(owner_id))  
