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

@users.route('/register',methods=['Get','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        deb.session.commit()
        flash('Thanks for registering!')
        return redirect(url_for('user.login'))

    return render_template('register.html',form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))