from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from cumulus import db
from cumulus.models import User,Posting
from cumulus.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from cumulus.users.picture_handler import add_profile_pic


#############################
## CHECKLIST
#############################

# REGISTER
# LOGIN
# LOGOUT -- Complete
# ACCOUNT (UPDATE UserForm)
# USER'S LIST OF POSTINGS

users = Blueprint('users',__name__)



@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))