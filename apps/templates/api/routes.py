# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Blueprint, render_template
from flask_login import login_required  # Only if you require user authentication
from jinja2 import TemplateNotFound

# Rename 'api' to 'blueprint'
blueprint = Blueprint('api', __name__, template_folder='api')

@blueprint.route('/api')
def api_docs():
    try:
        return render_template('api/api.html')
    except TemplateNotFound:
        return render_template('api/page-404.html'), 404
