from flask_login import LoginManager

admin_login_manager = LoginManager()

def setup_admin_login_manager(app):
    admin_login_manager.init_app(app)
    admin_login_manager.login_view = 'admin.alogin'

    @admin_login_manager.user_loader
    def load_super_admin(super_admin_id):
        # Implement logic to load super admin user if needed
        return None  # Example: Replace with actual super admin loading logic
