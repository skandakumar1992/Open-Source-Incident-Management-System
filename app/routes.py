# app/routes.py
from flask import Blueprint, render_template, request
from .models import db, User, Incident
from .email_utils import send_email

bp = Blueprint('main', __name__)  # <-- This is the 'bp' your __init__.py expects

@bp.route('/')
def index():
    return "Hello, Incident Management!"

# Example route
@bp.route('/incidents')
def incidents():
    incidents = Incident.query.all()
    return render_template('incidents.html', incidents=incidents)

