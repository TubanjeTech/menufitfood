import os
import time
from dotenv import load_dotenv
from flask import Blueprint, app, current_app, render_template, redirect, send_from_directory, url_for, flash
from flask_login import login_user, logout_user, login_required, UserMixin, current_user
from .adminconf import admin_login_manager
from .models import Staff
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask import current_app

load_dotenv() 

admins = Blueprint('admins', __name__)

class SuperAdmin(UserMixin):
    def __init__(self, id):
        self.id = id

@admin_login_manager.user_loader
def load_super_admin(super_admin_id):
    return SuperAdmin(id=super_admin_id)

@admins.route('/analytics')
def Analytics():
    return render_template('admin/analytics.html')