from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from cumulus import db
from cumulus.models import User,Posting
from cumulus.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from cumulus.users.picture_handler import add_profile_pic


#############################
## CHECKLIST
#############################

# REGISTER -- Complete
# LOGIN -- Complete
# LOGOUT -- Complete
# ACCOUNT (UPDATE UserForm)
# USER'S LIST OF POSTINGS

users = Blueprint('users',__name__)

#
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

#
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Log in success!')
            next = request.args.get('next')

            if next==None or not next[0]=='/':
                next = url_for('core.index')
            
            return redirect(next)

    return render_template('login.html',form=form)

#
@users.route('/logout')
def logout():
    logout_user()

    return redirect(url_for("core.index"))