import os
from flask_admin import Admin
from .models import db, User, Contact, Group
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    class Mymodel(ModelView):
        column_display_pk = True

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Contact, db.session))
    admin.add_view(ModelView(Group, db.session))
